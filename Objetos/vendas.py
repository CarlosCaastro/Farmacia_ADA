from datetime import datetime
from medicamentos import Medicamento,MedicamentoQuimioterapico
from clientes import Cliente

DESCONTO_IDADE = 0.2
DESCONTO_VALOR = 0.1

class Vendas:
    def __init__(self, cliente:Cliente, produtos: list[Medicamento]):
        self.cliente = cliente
        self.produtos = produtos
        self.data_hora = datetime.now()
        self.valor_total = sum(produto.get_valor for produto in produtos)
        self.valor_com_desconto = self.aplicar_descontos()
    
    def calcular_idade(self) -> int:
        hoje = datetime.now().date()
        idade = hoje.year - self.cliente.data_nascimento.year - ((hoje.month, hoje.day) < (self.cliente.data_nascimento.month, self.cliente.data_nascimento.day))
        return idade
    
    def aplicar_descontos(self) -> float:
        idade = self.calcular_idade()
        valor_desconto = 0.0
        
        if idade > 65:
            valor_desconto = self.valor_total * DESCONTO_IDADE
        if self.valor_total > 150:
            valor_desconto = max(valor_desconto, self.valor_total * DESCONTO_VALOR)
        
        valor_final = self.valor_total - valor_desconto
        return valor_final

    def verificar_receita(self) -> bool:
        for produto in self.produtos:
            if isinstance(produto, MedicamentoQuimioterapico):
                resposta = input(f"Você verificou a receita para o medicamento controlado '{produto.nome}'? (S/N): ")
                if resposta.lower() == "n":
                    print("Venda cancelada devido à falta de verificação de receita.")
                    return False
        return True
    
    def __repr__(self) -> str:
        produtos_descricao = ", ".join(produto.nome for produto in self.produtos)
        return f"\nData/Hora: {self.data_hora}\nCliente: {self.cliente.nome}\nValor Total: R${self.valor_com_desconto:.2f}\nProdutos: {produtos_descricao}"