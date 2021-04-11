from .pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self,nome,numero,faturas):
        super().__init__(nome)
        faturas = []
        self.faturas = faturas
        self.numero = numero

    def obter_faturas(self,faturas):
        self.faturas.append(faturas)
        return self.faturas
    

    def obter_numero(self,numero):
        return self.obter_numero
    



    