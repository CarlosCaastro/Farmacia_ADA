from clientes import Cliente

class Cadastro:
    '''
    A ideia dessa classe é armazenar tudo que foi feito nas outras classes, clientes, vendas e medicamentos.
    Logo uma venda não poderá ser feita de um medicamento que não está cadastrado e um cliente sem cadastro não poderá comprar na farmácia.
    No entanto poderá ser feito o cadastro na hora da compra tanto do cliente quanto do medicamento (porém esse último não faz tanto sentido)
    '''

    def __init__(self) -> None:
        self.cadastro = {}
    
    def cadastrar_cliente(self, cpf:str, nome:str, data_nascimento:str) -> None:
        if cpf in self.cadastro:
            print("Cliente já cadastrado.")
        else:
            cliente = Cliente(cpf,nome,data_nascimento)
            self.cadastro[cpf] = cliente

    def alterar_cadastro(self,cpf:str) -> None:

        if cpf not in self.cadastro:
            print("CPF não cadastrado.")
        
        cliente = self.cadastro[cpf]
        alteracao = input(int("Digite o número referente ao que deseja Alterar:\n1 - Alterar nome Cadastrato\n 2 - Alterar Data de Nascimento:"))
        
        if alteracao == 1:
            novo_nome = input('Digite o novo nome: ')
            cliente.nome = novo_nome
        elif alteracao == 2:
            nova_data = input('Digite a nova data de nascimento: ')
            cliente.data_nascimento = nova_data

        self.cadastro[cliente.cpf] = cliente
    
    def __repr__(self) -> str:
        repr_str = ""
        for cpf, cliente in self.cadastro.items():
            repr_str += f'CPF: {cpf}\n{cliente}\n'
        return repr_str