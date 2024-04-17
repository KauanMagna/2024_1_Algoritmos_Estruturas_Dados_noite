from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca, ano, cat, qtd_portas):
        super().__init__(marca, ano, cat)
        self.qtd_portas = qtd_portas

    def __str__(self):
        return super().__str__() + "\nPortas: " + str(self.qtd_portas)

    def imprimir(self):
        print("-----Carro-----")
        super().imprimir()
        print("\nPortas: " + str(self.qtd_portas))

        #print(self)

        #print( self.__str__() )
        
