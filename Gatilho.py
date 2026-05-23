import numpy as np

class Gatilho:
    def __init__(self, nome, condicao, impacto):
        self.nome = nome
        self.condicao = condicao
        self.impacto = impacto
        self.ativo = False
    
    def gatilho(self, estado):
        if self.condicao(estado):
            if not self.ativo:
                self.ativo = True
                print(f"Evento {self.nome} ativado!")
            return self.impacto
        else:
            if self.ativo:
                self.ativo = False
                print(f"Evento {self.nome} desativado!")
            return None