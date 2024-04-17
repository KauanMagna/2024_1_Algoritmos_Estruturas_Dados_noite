class Bicicleta:
    def __init__(self, marca, rodas, modelo, num_marchas, bagageiro):
        super().__init__(marca, rodas, modelo)
        self.num_marchas = num_marchas
        self.bagageiro = bagageiro

    def __str__(self):
        super().__init__() + "\nQtd Marchas: " + str(self.num_marchas) + "\nBagageiro: " + self.bagageiro

    