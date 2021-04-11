from .funcionario import Funcionario

class Vendedor(Funcionario):
    def __init__(self,faturas):
        self.faturas = faturas    


    def obter_faturas(self,inicio, fim):
        obter_fat = []
        self.inicio = inicio
        self.fim = fim

        obter_fat.append(self.inicio,self.fim)
        return obter_fat
        



    
    
    
    


        
    



       
   
        
        
        
        
        

    


