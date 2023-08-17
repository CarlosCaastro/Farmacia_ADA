from clientes import Cliente
from laboratorio import Laboratorio
from medicamentos import MedicamentoQuimioterapico, MedicamentoFitoterapico, Medicamento
from vendas import Vendas
import re
from datetime import date,datetime

class Cadastro:
    '''
    A ideia dessa classe é armazenar tudo que foi feito nas outras classes, clientes, vendas e medicamentos.
    Logo uma venda não poderá ser feita de um medicamento que não está cadastrado e um cliente sem cadastro não poderá comprar na farmácia.
    No entanto poderá ser feito o cadastro na hora da compra tanto do cliente quanto do medicamento (porém esse último não faz tanto sentido)
    '''

    def __init__(self) -> None:
        self.cadastro = {}
    
    def cadastrar(self, cpf:str, nome:str, data_nascimento:str) -> None:
        if cpf in self.cadastro:
            print("Cliente já cadastrado.")
        else:
            cliente = Cliente(cpf,nome,data_nascimento)
            self.cadastro[cpf] = cliente

    def alterar_cadastro(self,cpf:str) -> None:

        if cpf not in self.cadastro:
            print("CPF não cadastrado.")
        
        cliente = self.cadastro[cpf]
        alteracao = int(input("Digite o número referente ao que deseja Alterar:\n1 - Alterar nome Cadastrato\n 2 - Alterar Data de Nascimento:"))
        
        if alteracao == 1:
            novo_nome = str(input('Digite o novo nome: '))
            if not self.__validador_nome(novo_nome):
                raise ValueError("Nome inválido. Digite o nome, sem nenhum  número e sem caracter especial.")
            else:
                cliente.nome = novo_nome
        elif alteracao == 2:
            nova_data = str(input('Digite a nova data de nascimento dd/mm/yyyy: '))
            try:
                cliente.data_nascimento = self.__transform_data(nova_data)
            except ValueError:
                raise ValueError("Data inválida. Digite a data no formato dd/mm/yyyy")

        self.cadastro[cliente.cpf] = cliente
    
    def __validador_nome(self, nome: str) -> bool:
        regex = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'
        return re.match(regex, nome) is not None
    
    def __transform_data(self,data) -> date:
        return datetime.strptime(data, '%d/%m/%Y').date()

    def __repr__(self) -> str:
        repr_str = ""
        for cpf, cliente in self.cadastro.items():
            repr_str += f'CPF: {cpf}\n{cliente}\n'
        return repr_str

    def mostrar_cadastro(self) -> None:
        cadastro_ordenado = sorted(self.cadastro.values(), key=lambda objeto: objeto.nome)
        
        print("Lista de Cadastrados (Ordenados por Nome):")
        for obj in cadastro_ordenado:
            print(obj)
    
class CadastroLaboratorio(Cadastro):
    def __init__(self) -> None:
        self.cadastros_labo = {}

    def cadastrar(self, nome: str, endereco: str, ddd:str,telefone: str, cidade: str, estado: str) -> None:

        if nome in self.cadastros_labo:
            print("Laboratório já cadastrado.")
        else:
            chave = nome + endereco
            laboratorio = Laboratorio(nome,endereco,ddd,telefone,cidade,estado)
            self.cadastros_labo[chave] = laboratorio

    def alterar_cadastro(self,nome:str,endereco: str) -> None:
        chave = nome + endereco
        if chave not in self.cadastros_labo:
            print("Loja não cadastrado.")
        
        labo = self.cadastros_labo[chave]
        alteracao = int(input("""Digite o número referente ao que deseja Alterar:
                1 - Alterar nome da Loja. 
                2 - Alterar Endereço da Loja.
                3 - Alterar DDD cadastrado.
                4 - Alterar Telefone cadastrato.
                5 - Alterar Cidade cadastrada.
                6 - Alterar Estado cadastrado da Loja                  
                """))
        if alteracao == 1:
            novo_nome = input('Digite o novo nome: ')
            labo.nome = novo_nome
        elif alteracao == 2:
            novo_endereco = input('Digite o novo endereço: ')
            labo.endereco = novo_endereco
        elif alteracao == 3:
            novo_ddd = input('Digite o novo DDD: ')
            if len(novo_ddd) != 2:
                raise ValueError("O DDD deve conter exatamente dois caracteres.")
            elif novo_ddd == "00":
                raise ValueError("O DDD não pode ser '00'.")
            labo.ddd = novo_ddd.zfill(3)
        elif alteracao == 4:
            novo_telefone = input('Digite o novo Telefone: ')
            if len(novo_telefone) != 9:
                raise ValueError("O numero de telefone precisa conter nove caracteres. Verifique se não esqueceu de colocar o digito 9 na frente.")
            labo.telefone = novo_telefone
        elif alteracao == 5:
            novo_cidade = input('Digite o novo Cidade: ')
            labo.cidade = novo_cidade
        elif alteracao == 6:
            novo_estado = input('Digite o novo Estado: ')
            labo.estado = novo_estado

        self.cadastros_labo[chave] = labo

    def __repr__(self) -> str:
        repr_str = ""
        i = 0
        for labo in self.cadastros_labo.values():
            i += 1
            repr_str += f'Loja Cadastrada {i}: \n{labo}\n'
        return repr_str
    
    def mostrar_cadastro(self) -> None:
        cadastro_ordenado = sorted(self.cadastros_labo.values(), key=lambda objeto: objeto.nome)
        print("Lista de Cadastrados (Ordenados por Nome):")
        for obj in cadastro_ordenado:
            print(obj)

class CadastroMedicamento(Cadastro):
    
    def __init__(self) -> None:
        self.cadastros_medicamentos = {}
    
    def cadastrar(self, nome: str, tipo: str, principal_composto: str, laboratorio: str, descricao: str, valor: float = 0.0) -> None:
        chave = nome
        if nome in self.cadastros_medicamentos:
            print("Medicamento já cadastrado.")
        else:
            if tipo.lower() == "1":
                medicamento = MedicamentoQuimioterapico(nome, principal_composto, laboratorio, descricao, valor)
            elif tipo.lower() == "2":
                medicamento = MedicamentoFitoterapico(nome, principal_composto, laboratorio, descricao, valor)
            else:
                raise ValueError("Tipo de medicamento inválido.")
            self.cadastros_medicamentos[chave] = medicamento
    
    def alterar_cadastro(self, nome: str, laboratorio:str) -> None:
        chave = nome
        if nome not in self.cadastros_medicamentos:
            print("Medicamento não cadastrado.")
        
        medicamento = self.cadastros_medicamentos[chave]
        alteracao = int(input("""Digite o número referente ao que deseja Alterar:
                1 - Alterar nome do Medicamento.
                2 - Alterar Principal Composto.
                3 - Alterar Laboratório.
                4 - Alterar Descrição.
                5 - Alterar Valor.
                """))
        
        if alteracao == 1:
            novo_nome = input('Digite o novo nome: ')
            medicamento.nome = novo_nome
        elif alteracao == 2:
            novo_composto = input('Digite o novo composto: ')
            medicamento.principal_composto = novo_composto
        elif alteracao == 3:
            novo_laboratorio = input('Digite o novo laboratório: ')
            medicamento.laboratorio = novo_laboratorio
        elif alteracao == 4:
            nova_descricao = input('Digite a nova descrição: ')
            medicamento.descricao = nova_descricao
        elif alteracao == 5:
            novo_valor = float(input('Digite o novo valor: '))
            if not isinstance(novo_valor, (float, int)):
                raise ValueError("O valor do medicamento deve ser um número.")
            medicamento.set_valor = novo_valor
        
        self.cadastros_medicamentos[chave] = medicamento

    def __repr__(self) -> str:
        repr_str = ""
        i = 0
        for medicamento in self.cadastros_medicamentos.values():
            i += 1
            repr_str += f'Medicamento Cadastrado {i}: \n{medicamento}\n'
        return repr_str
    
    def mostrar_cadastro(self) -> None:
        cadastro_ordenado = sorted(self.cadastros_medicamentos.values(), key=lambda objeto: objeto.nome)
        print("Lista de Medicamentos Cadastrados (Ordenados por Nome):")
        for obj in cadastro_ordenado:
            print(obj)

class CadastroVenda(Cadastro):
    def __init__(self):
        super().__init__()
        self.vendas = []

    def realizar_venda(self, cadastro_cliente:Cadastro,cpf_cliente: str, produtos: list[Medicamento]):
        if cpf_cliente not in cadastro_cliente.cadastro:
            print("Cliente não cadastrado. Venda não pode ser realizada.")
            return

        cliente = cadastro_cliente.cadastro[cpf_cliente] #:Cliente

        venda = Vendas(cliente, produtos)

        if not venda.verificar_receita():
            return

        valor_final = venda.aplicar_descontos()
        self.vendas.append(venda)
        print("Venda realizada com sucesso!")
        print("Valor Total da Venda:", venda.valor_total)
        print("Valor Final com Descontos:", valor_final)

    def emitir_relatorio_vendas(self):
        for idx, venda in enumerate(self.vendas, start=1):
            print(f"Venda {idx}:\n{venda}\n")

