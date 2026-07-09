import numpy as np
"""
Classe Gatilho: eventos ativados quando sem cumpre a condição definida
-nome: nome do gatilho;
-condicao: condição para ativar o gatilho;
-impacto: impacto do gatilho;
-ativo: booleano, alterna entre True (gatilho ativado) e False (gatilho desativado)

"""
class Gatilho:
    def __init__(self, nome, condicao, impacto):
        self.nome = nome
        self.condicao = condicao
        self.impacto = impacto
        self.ativo = False
    
    # Avalia a condição, e ativa o gatilho se ela for validada
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