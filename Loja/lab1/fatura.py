class Fatura:
    def __init__(self, numero, data, cliente, vendedor, itens):
        self.numero = numero 
        self.data = data
        self.cliente = cliente
        self.vendedor = vendedor
        self.itens = itens

    def obter_numero(self):
        return self.numero 


    def obter_data(self):
        return self.data    
    
    def obter_cliente(self):
        return self.cliente
    

    def obter_vendedor(self):
        return self.vendedor
    
    def obter_itens(self):
        return self.itens
