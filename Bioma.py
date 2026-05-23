import numpy as np
from Estado import Estado
from Gatilho import Gatilho

class Bioma:

    def __init__(self, nome, estadoInicial, recuperacao):
        self.nome = nome
        self.estado = Estado(*estadoInicial)
        self.recuperacao = np.array(recuperacao)
        self.fatorManual = []
        self.gatilhos = []

    def addGatilho(self, gatilho):
        self.gatilhos.append(gatilho)
    
    def ciclo(self):
        if self.estado["Solo"] > 0.3:
            self.estado.valores += self.recuperacao
        
        for f in self.fatorManual:
            f.atua(self.estado)

        for g in self.gatilhos:
            impacto = g.gatilho(self.estado)
            if impacto:
                impacto.atua(self.estado)
        self.estado.clip()