class Laboratorio:
    '''
    Classe para gerar os objetos de laboratório.
    '''

    def __init__(self, nome: str, endereco: str, ddd:str,telefone: str, cidade: str, estado: str) -> None:

        if len(ddd) != 2:
            raise ValueError("O DDD deve conter exatamente dois caracteres.")
        
        elif ddd == "00":
            raise ValueError("O DDD não pode ser '00'.")

        elif len(telefone) != 9:
            raise ValueError("O numero de telefone precisa conter nove caracteres. Verifique se não esqueceu de colocar o digito 9 na frente.")
        
        self.nome = nome
        self.endereco = endereco
        self.ddd = ddd.zfill(3)
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def __repr__(self) -> str:
        return f'Nome: {self.nome}\nEndereço: {self.endereco}\nDDD: {self.ddd}\nTelefone: {self.telefone}\nCidade: {self.cidade}\nEstado: {self.estado}'