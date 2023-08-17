from cadastro import Cadastro, CadastroMedicamento, CadastroVenda, CadastroLaboratorio
from medicamentos import MedicamentoQuimioterapico, MedicamentoFitoterapico
from atendimento import Atendimento

def exibir_menu():
    print("\n===== Menu =====")
    print("1. Cadastrar Cliente")
    print("2. Alterar Cadastro de Cliente")
    print("3. Cadastrar Laboratório")
    print("4. Alterar Cadastro de Laboratório")
    print("5. Cadastrar Medicamento")
    print("6. Alterar Cadastro de Medicamento")
    print("7. Realizar Venda")
    print("8. Relatórios")
    print("0. Sair")

cadastro_clientes = Cadastro()
cadastro_laboratorios = CadastroLaboratorio()
cadastro_medicamentos = CadastroMedicamento()
cadastro_vendas = CadastroVenda()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o programa.")
        atendimento_atual = Atendimento()
        atendimento_atual.calcular_estatisticas(cadastro_vendas.vendas)
        atendimento_atual.exibir_estatisticas()
        break

    elif opcao == "1":
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/yyyy): ")
        cadastro_clientes.cadastrar(cpf, nome, data_nascimento)

    elif opcao == "2":
        cpf = input("Digite o CPF do cliente que deseja alterar: ")
        cadastro_clientes.alterar_cadastro(cpf)

    elif opcao == "3":
        nome = input("Digite o nome do laboratório: ")
        endereco = input("Digite o endereço do laboratório: ")
        ddd = input("Digite o DDD do laboratório: ")
        telefone = input("Digite o telefone do laboratório: ")
        cidade = input("Digite a cidade do laboratório: ")
        estado = input("Digite o estado do laboratório: ")
        cadastro_laboratorios.cadastrar(nome, endereco, ddd, telefone, cidade, estado)

    elif opcao == "4":
        nome = input("Digite o nome do laboratório que deseja alterar: ")
        endereco = input("Digite o endereço do laboratório que deseja alterar: ")
        cadastro_laboratorios.alterar_cadastro(nome, endereco)

    elif opcao == "5":
        nome = input("Digite o nome do medicamento: ")
        tipo = input("Digite o tipo do medicamento (1 para Quimioterápico, 2 para Fitoterápico): ")
        principal_composto = input("Digite o principal composto do medicamento: ")
        laboratorio = input("Digite o laboratório do medicamento: ")
        descricao = input("Digite a descrição do medicamento: ")
        valor = float(input("Digite o valor do medicamento: "))
        cadastro_medicamentos.cadastrar(nome, tipo, principal_composto, laboratorio, descricao, valor)

    elif opcao == "6":
        nome = input("Digite o nome do medicamento que deseja alterar: ")
        laboratorio = input("Digite o laboratório do medicamento que deseja alterar: ")
        cadastro_medicamentos.alterar_cadastro(nome, laboratorio)

    elif opcao == "7":
        cpf_cliente = input("Digite o CPF do cliente que realizará a compra: ")
        produtos = []
        while True:
            nome_produto = input("Digite o nome do medicamento que será adicionado à compra (0 para finalizar): ")
            if nome_produto == "0":
                break
            if nome_produto in cadastro_medicamentos.cadastros_medicamentos:
                produtos.append(cadastro_medicamentos.cadastros_medicamentos[nome_produto])
            else:
                print("Medicamento não cadastrado.")
        cadastro_vendas.realizar_venda(cpf_cliente, produtos)

    elif opcao == "8":
        print("\n===== Relatórios =====")
        print("1. Listagem de Clientes")
        print("2. Listagem de Laboratórios (ordem alfabética)")
        print("3. Listagem de Medicamentos (ordem alfabética)")
        print("4. Listagem de Medicamentos Quimioterápicos")
        print("5. Listagem de Medicamentos Fitoterápicos")
        print("6. Estatísticas dos Atendimentos do Dia")
        print("0. Sair")
        
        relatorio_opcao = input("Escolha uma opção de relatório: ")

        if relatorio_opcao == "1":
            cadastro_clientes.mostrar_cadastro()
        elif relatorio_opcao == "2":
            cadastro_laboratorios.mostrar_cadastro()
        elif relatorio_opcao == "3":
            cadastro_medicamentos.mostrar_cadastro()
        elif relatorio_opcao == "4":
            for medicamento in cadastro_medicamentos.cadastros_medicamentos.values():
                if isinstance(medicamento, MedicamentoQuimioterapico):
                    print(medicamento)
        elif relatorio_opcao == "5":
            for medicamento in cadastro_medicamentos.cadastros_medicamentos.values():
                if isinstance(medicamento, MedicamentoFitoterapico):
                    print(medicamento)
        elif relatorio_opcao == "6":
            print(cadastro_vendas)
        elif relatorio_opcao == "0":
            continue

    else:
        print("Opção inválida. Digite um número entre 0 e 8.")
