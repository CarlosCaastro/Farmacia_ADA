from medicamentos import MedicamentoQuimioterapico, MedicamentoFitoterapico

class Atendimento:
    def __init__(self):
        self.produtos_vendidos = {}
        self.pessoas_atendidas = 0
        self.total_quimioterapicos = 0
        self.total_fitoterapicos = 0

    def calcular_estatisticas(self, vendas):
        for venda in vendas:
            for produto in venda.produtos:
                if produto.nome in self.produtos_vendidos:
                    self.produtos_vendidos[produto.nome]["quantidade"] += 1
                    self.produtos_vendidos[produto.nome]["valor_total"] += produto.get_valor
                else:
                    self.produtos_vendidos[produto.nome] = {
                        "quantidade": 1,
                        "valor_total": produto.get_valor
                    }
                if isinstance(produto, MedicamentoQuimioterapico):
                    self.total_quimioterapicos += 1
                elif isinstance(produto, MedicamentoFitoterapico):
                    self.total_fitoterapicos += 1
            self.pessoas_atendidas += 1

    def exibir_estatisticas(self):
        print("Remédio mais vendido:")
        mais_vendido = max(self.produtos_vendidos, key=lambda x: self.produtos_vendidos[x]["quantidade"])
        quantidade_mais_vendido = self.produtos_vendidos[mais_vendido]["quantidade"]
        valor_total_mais_vendido = self.produtos_vendidos[mais_vendido]["valor_total"]
        print(f"{mais_vendido}: Quantidade: {quantidade_mais_vendido}, Valor Total: R${valor_total_mais_vendido:.2f}")

        print("Quantidade de pessoas atendidas:", self.pessoas_atendidas)
        print("Número de remédios Quimioterápicos vendidos:", self.total_quimioterapicos)
        print("Número de remédios Fitoterápicos vendidos:", self.total_fitoterapicos)

        print("===== Fim do Relatório =====")
