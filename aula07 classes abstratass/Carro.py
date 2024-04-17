from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano, n_portas):
        super().__init__(modelo, ano) #caso o parâmetro seja default no need to declare
        self.qtd_portas = n_portas

    def ligar(self, chave):
        if chave == 1234:
            print("Carro ligado")
        else:
            print("Não foi possível ligar o carro")

    def imprimir(self):
        super.imprimir()
        print(f"Quantidade de portas: {self.qtd_portas}")

        