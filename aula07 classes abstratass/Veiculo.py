from abc import ABC, abstractmethod

# class Veiculo( metaclass = ABCMeta ):
class Veiculo(ABC):
    def __init__(self, modelo, ano):
        self.modelo = modelo 
        self.ano = ano

# Aproveitamento de código?
    @abstractmethod
    def ligar(self, chave):
        pass 

    def imprimir(self):
        print(F"Modelo: {self.modelo}")
        print(F"Ano: {self.ano}")

    def desligar(self):
        print(f"Veículo desligado")

    
