class Laboratorio:
    '''
    Classe para gerar os objetos de laboratório.
    '''

    def __init__(self, nome: str, endereco: str, ddd:str,telefone: str, cidade: str, estado: str) -> None:

        if len(ddd) != 2:
            raise ValueError("O DDD deve conter exatamente dois caracteres.")
        
        if ddd == "00":
            raise ValueError("O DDD não pode ser '00'.")
        
        self.nome = nome
        self.endereco = endereco
        self.ddd = ddd
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self) -> str:
        return f'Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nCidade: {self.cidade}\nEstado: {self.estado}'
