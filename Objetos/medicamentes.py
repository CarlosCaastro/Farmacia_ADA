class Medicamento:
    '''
    Classe principal de medicamentos de onde as classes Medicamentos Quimioterápicos e Medicamentos Fitoterápicos
    irão herdar seus atributos e métodos principais.
    '''

    def __init__(self,nome:str,principal_composto:str,laboratorio:str,descricao:str,necessita_receita:str = "Não",valor: float = 0.0) ->None:
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.necessita_receita = necessita_receita
        self.__valor = valor

    @property
    def get_valor(self) -> float:
        return self.__valor
    
    @get_valor.setter
    def set_valor(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self.__valor = novo_valor
        else:
            print("O valor do medicamento não pode ser negativo.")
    
    def __repr__(self) -> str:
        receita = "Sim" if self.necessita_receita else "Não"
        return f'Nome: {self.nome}\nPrincipal Composto: {self.principal_composto}\nLaboratório: {self.laboratorio}\nDescrição: {self.descricao}\nNecessita Receita: {receita}\nValor: {self.__valor:.2f}'
    
class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome: str, principal_composto: str, laboratorio: str, descricao: str, necessita_receita: str = "Sim", valor: float = 0.0) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, necessita_receita, valor)
    
    @Medicamento.set_valor.setter
    def valor(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self._Medicamento__valor = novo_valor
        else:
            print("O valor do medicamento não pode ser negativo.")

class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome: str, principal_composto: str, laboratorio: str, descricao: str, necessita_receita: str = "Não", valor: float = 0.0) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, necessita_receita, valor)
    
    @Medicamento.set_valor.setter
    def valor(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self._Medicamento__valor = novo_valor
        else:
            print("O valor do medicamento não pode ser negativo.")