from abc import ABC
from .pessoa import Pessoa

class Funcionario(ABC,Pessoa):
    def __init__(self, numero):
        super().__init__(self)
        self.numero = numero


    def obter_numero(self):
        return self.numero