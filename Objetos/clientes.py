from datetime import date,datetime
import re

PADRAO_CPF = 11
VALIDADOR_NOME = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'

class Cliente:
    '''
    A classe cliente irá receber informações de CPF no formato xxxxxxxxxxx, sem caracteres especiais ou caracteres de texo.
    A informação de nome não pode conter valores númericos.
    Os valores de data precisam ser inseridor no formado dd/mm/yyyy
    '''

    def __init__(self,cpf:str,nome:str,data_nascimento:str) -> None:
        cpf = self.__normalizador_cpf(cpf)

        if self.__validador_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError ("CPF inválido. Digite somente os números do CPF ou complete o CPF.")
        
        if self.__validador_nome(nome):
            self.nome = nome
        else:
            raise ValueError("Nome inválido. Digite o nome, sem nenhum  número e sem caracter especial.")
        
        try:
            self.data_nascimento = self.__transform_data(data_nascimento)
        except ValueError:
            raise ValueError("Data inválida. Digite a data no formato dd/mm/yyyy")

    def __repr__(self) -> str:
        return f'CPF: {self.cpf}\nNome: {self.nome}\nData de Nascimento: {self.data_nascimento}'

    def __normalizador_cpf (self,cpf:str) -> str:
        return ''.join(filter(str.isdigit,cpf))

    def __validador_cpf(self,cpf:str) -> bool:
        return len(cpf) == PADRAO_CPF

    def __validador_nome(self, nome: str) -> bool:
        return re.match(VALIDADOR_NOME, nome) is not None

    def __transform_data(self,data) -> date:
        return datetime.strptime(data, '%d/%m/%Y').date()