import numpy as np
from Estado import Estado
from Gatilho import Gatilho
"""
Classe Bioma: referente ao bioma que será analisado.
-nome: nome do bioma;
-estado: instância da classe Estado que contém o estado atual do bioma;
-recuperacao: array com os valores de regeneração natural que acontecem todo ano;
-fatorManual: armazena fatores de impacto, recuperação e enfrentamento
-gatilhos: lista de instâncias de gatilho

"""
class Bioma:

    def __init__(self, nome, estadoInicial, recuperacao):
        self.nome = nome
        self.estado = Estado(*estadoInicial)
        self.recuperacao = np.array(recuperacao)
        self.fatorManual = []
        self.gatilhos = []

    # Insere os gatilhos na lista de gatilhos
    def addGatilho(self, gatilho):
        self.gatilhos.append(gatilho)
    
    # Ciclo de um ano

    def ciclo(self):
        if self.estado["Solo"] > 0.3:
            self.estado.valores += self.recuperacao
        
        """ Diferencia e executa os fatores impacto/recuperação de fatores enfrentamento a partir do atributo "efeito" 
        (somente os enfrentamentos possuem)"""

        # Fator enfrentamento:
        for f in self.fatorManual:
            if hasattr(f, "efeito"):
                if f.fator in self.fatorManual:
                    f.atua(self.estado)
                else:
                    f.desativa()

        # Fator impacto/recuperação
        for f in self.fatorManual:
            if not hasattr(f, "efeito"):
                f.atua(self.estado)

        # Executa os gatilhos:
        impactos_atuando = []
        for g in self.gatilhos:
            impacto = g.gatilho(self.estado)
            if impacto:
                impactos_atuando.append(impacto)

        for impacto in impactos_atuando:
            impacto.atua(self.estado)
        
        # Chama método clip() da classe Estado -> limita valores a [0, 1]
        self.estado.clip()