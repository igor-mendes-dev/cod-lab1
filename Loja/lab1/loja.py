class loja:
    def __init__(self,gestor,vendedores,clientes,itens):
        self.gestor = gestor
        self.vendedores = vendedores
        self.clientes = clientes
        self.itens = itens
    
    def obter_gestor(self):
        return self.gestor
    

    def obter_vendedores(self):
        lista_ven = []
        lista_ven.append(self.vendedores)
        return lista_ven
    

    def obter_cliente(self):
        lista_c = []
        lista_c.append(self.clientes)
        return lista_c

    def obter_itens(self):
        pass
     
    
    def registrar_gestor(self,nome,numero_de_funcionario):
        self.nome = nome
        self.numero_de_funcionario = numero_de_funcionario
    

    def registrar_vendedor(self,nome,numero_de_funcionario):
        self.nome = nome
        self.numero_de_funcionario = numero_de_funcionario

    
    def registrar_cliente(self,nome,numero_de_cliente):
        self.nome = nome
        self.numero_de_cliente = numero_de_cliente

     
    def registrar_item(self,nome):
        self.nome = nome
    
    def registrar_fatura(self, numero_de_cliente,itens,numero_de_funcionario_do_vendedor,ano,mes,dia):
        self.numero_de_cliente = numero_de_cliente
        self.itens = itens 
        self.numero_de_funcionario_do_vendedor = numero_de_funcionario_do_vendedor
        self.ano = ano
        self.mes = mes
        self.dia = dia

    
    def obter_fatura_cliente(self,numero_de_cliente):
        self.numero_cliente = numero_de_cliente

    
    def obter_fatura_vendedor(self,numero_de_funcionario):
        self.numero_de_funcionario = numero_de_funcionario





        
        

        
        




