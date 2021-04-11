from abc import ABC

class Pessoa(ABC):
    def __init__(self,pessoa):
        self.pessoa = pessoa
    
    def obter_pessoa(self):
        return self.pessoa
        


