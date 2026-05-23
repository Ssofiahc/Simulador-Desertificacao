import numpy as np

class Impacto:

    def __init__(self, nome, matriz, incremento = None, recorrente = True):
        self.nome = nome
        self.matriz = np.array(matriz)
        self.incremento = np.array(incremento) if incremento else np.zeros(5)
        self.recorrente = recorrente

    def atua(self, estado):
        estado.valores = np.dot(self.matriz, estado.valores) + self.incremento
        estado.clip()