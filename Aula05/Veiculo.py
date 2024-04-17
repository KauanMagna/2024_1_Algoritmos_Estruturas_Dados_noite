from Categoria import Categoria 

class Veiculo:

    def __init__(self, marca = "BYD", ano = 2018, cat = Categoria("SUV") ):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.categoria = cat

# Método STR é para retornar o conteúdo string do Objeto
    def __str__(self):
        texto = "\nVeículo: \nMarca: " + self.marca + "\nAno: " + str(self.ano)
        texto += "\nCategoria: " + self.categoria.nome
        return texto

    def imprimir(self):
        print(self)
