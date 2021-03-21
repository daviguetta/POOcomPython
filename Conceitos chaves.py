
#CLASSE EM PYTHON
class Carro():

# __init__ CONSTRUTOR DO PYTHON - METODO PARA A ATRIBUIÇÃO DE ATRIBUTOS PARA UMA INSTÂNCIA
# "def" define um metodo dentro da classe
    def __init__(self,arg,arg2):
        self.Atributo1 = arg
        self.Atributo2 = arg2

    def getAtributo1():
        return self.Atributo1

# HERANÇA

# Classe PAI
class Veiculo():

    def __init__(self, initMarca, initModelo, initAreaDeAtuacao):
        self.Marca = initMarca
        self.Modelo = initModelo
        self.AreaDeAtuação = initAreaDeAtuacao

# Classe FILHA
# Invoca a classe pai como parâmetro
class Carro(Veiculo):

    def __init__(self, initMarca, initModelo, initAreaDeAtuacao):

        #super() é responsavel por invocar a herança da classe pai
        super().__init__(initMarca, initModelo, initAreaDeAtuação)

    