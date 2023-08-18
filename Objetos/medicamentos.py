class Medicamento:
    '''
    Classe principal de medicamentos de onde as classes Medicamentos Quimioterápicos e Medicamentos Fitoterápicos
    irão herdar seus atributos e métodos principais.
    '''

    def __init__(self,nome:str,principal_composto:str,laboratorio:str,descricao:str,valor: float = 0.0) ->None:
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        if not isinstance(valor, (float, int)):
            raise ValueError("O valor do medicamento deve ser um número.")
        self.__valor = float(valor)

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
        return f'Nome: {self.nome}\nPrincipal Composto: {self.principal_composto}\nLaboratório: {self.laboratorio}\nDescrição: {self.descricao}\nValor: {self.__valor:.2f}'
    
class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome: str, principal_composto: str, laboratorio: str, descricao: str, valor: float = 0.0, necessita_receita:str = "Sim") -> None:
        self.necessita_receita = necessita_receita
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
        
    def __repr__(self) -> str:
        return f'Nome: {self.nome}\nPrincipal Composto: {self.principal_composto}\nLaboratório: {self.laboratorio}\nDescrição: {self.descricao}\nValor: {self.get_valor:.2f}\nNecessita Receita: {self.necessita_receita}'
    
    @property
    def get_valor(self) -> float:
        return self._Medicamento__valor

    @Medicamento.set_valor.setter
    def valor(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self._Medicamento__valor = novo_valor
        else:
            print("O valor do medicamento não pode ser negativo.")

class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome: str, principal_composto: str, laboratorio: str, descricao: str, valor: float = 0.0) -> None:
        super().__init__(nome, principal_composto, laboratorio, descricao, valor)
    
    @property
    def get_valor(self) -> float:
        return self._Medicamento__valor

    @Medicamento.set_valor.setter
    def valor(self, novo_valor: float) -> None:
        if novo_valor >= 0:
            self._Medicamento__valor = novo_valor
        else:
            print("O valor do medicamento não pode ser negativo.")