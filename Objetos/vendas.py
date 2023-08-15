class Vendas:
    def __init__(self, data_hora_venda, cliente, produtos_vendidos, valor_total):
        self.data_hora_venda = data_hora_venda
        self.cliente = cliente
        self.produtos_vendidos = produtos_vendidos
        self.valor_total = valor_total

    def __repr__(self):
        return f'Data e Hora da Venda: {self.data_hora_venda}\nCliente: {self.cliente.nome}\nProdutos Vendidos: {self.produtos_vendidos}\nValor Total: R${self.valor_total:.2f}'

