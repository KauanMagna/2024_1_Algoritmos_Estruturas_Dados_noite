class Veiculo:
    def __init__(self, marca, rodas, modelo):
        self.marca = marca
        self.qtd_rodas = rodas
        self.modelo = modelo 
        self.velocidade = 0

    def __str__(self):
        texto = "\nMarca: " + self.marca
        texto += "\nQtd Rodas: " + str(self.qtd_rodas)
        texto += "\nModelo: " + self.modelo
        texto += "\nVelocidade Atual: " + str(self.velocidade) + " Km/h"
        return texto

    def acelerar(self, aceleracao):
        vel = self.velocidade
        vel += aceleracao
        self.velocidade = vel

    def frear(self, freio):
        vel = self.velocidade
        if vel - freio >= 0:
            vel -= freio
            self.velocidade = vel
        elif vel - freio < 0:
            self.velocidade = 0
        


