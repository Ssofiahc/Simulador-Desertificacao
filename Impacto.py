import numpy as np
"""
Classe Impacto: atualiza o estado do bioma.
-nome: nome do impacto;
-matriz: matriz(5x5) que multiplica valores de estado atuais, gerando degradação ou melhoria;
-incremento: array somado diretamente aos índices;
-recorrente: impacto constante ou de ocorrência única (até o momento todos os impactos são contínuos)

"""
class Impacto:

    def __init__(self, nome, matriz, incremento = None, recorrente = True):
        self.nome = nome
        self.matriz = np.array(matriz)
        #Se não existir incremento -> incremento = [0, 0, 0, 0, 0]
        self.incremento = np.array(incremento) if incremento else np.zeros(5)
        self.recorrente = recorrente
    
    """ Atualiza a matriz valores -> calcula a multiplicação das matrizes np.dot(matriz * valores) e soma o incremento 
    (só altera em algo caso estejam sendo utilizadas cisternas, que somam diretamente 0.1 na umidade) 
    """
    def atua(self, estado):
        estado.valores = np.dot(self.matriz, estado.valores) + self.incremento
        estado.clip()