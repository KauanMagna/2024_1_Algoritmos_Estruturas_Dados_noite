from abc import ABC, abstractmethod

class Conta_bancaria(ABC):
    def __init__(self):
        self.nome = None 
        self.flow = 0

    @abstractmethod
    def depositar(self, valor):
        pass

    def cadastrar(self, nome):
        self.nome = nome

    