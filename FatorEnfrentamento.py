import numpy as np

class fatorEnfrentamento:

#Ações mais bruscas que interrompem ou diminuem um fator de impacto
#Exemplo: Fiscalização rigorosa contra desmatamento ilegal

    def __init__(self, nome, fator, efeito):
        self.nome = nome
        self.fator = fator
        self.efeito = efeito
        self.m_original = fator.matriz.copy()

    def atua(self, estado):
        m_i = np.eye(5)
        self.fator.matriz = m_i - (self.m_original - 1) * (1 - self.efeito)
    
    def desativa(self):
        self.fator.matriz = self.m_original.copy()