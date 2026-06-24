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
            if hasattr(f, "efeito"):
                if f.fator in self.fatorManual:
                    f.atua(self.estado)
                else:
                    f.desativa()

        for f in self.fatorManual:
            if not hasattr(f, "efeito"):
                f.atua(self.estado)


        impactos_atuando = []
        for g in self.gatilhos:
            impacto = g.gatilho(self.estado)
            if impacto:
                impactos_atuando.append(impacto)

        for impacto in impactos_atuando:
            impacto.atua(self.estado)
            
        self.estado.clip()