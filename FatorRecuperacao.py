import numpy as np
from Impacto import Impacto

RECUPERACAO = {
    "BAIXA": 0.1,
    "MEDIA": 0.25,
    "ALTA": 0.4
}
"""
Fatores de recuperação:
    Reflorestamento - Efeito geral
    Barragem Subterrânea - Recuperação da umidade do solo
    Cisternas - Alivia a pressão sobre fontes naturais
    Educação ambiental - Efeito geral a longo prazo
    Agric de conservação - Preserva a Fertilidade do solo
    Sistemas agroflorestais - Redução de temperaturas e conserva a umidade do solo
"""

# 0 - Umidade, 1 - Fertilidade, 2 - Biodiversidade, 3 - Vegetação, 4 - Solo

#REFLORESTAMENTO: Biodiversidade, Vegetação, Solo
x = RECUPERACAO["ALTA"]
mReflorestamento = np.eye(5)
mReflorestamento[2,2] = 1 + x
mReflorestamento[3,3] = 1 + x
mReflorestamento[4,4] = 1 + (x/2)
reflorestamento = Impacto("Reflorestamento", mReflorestamento)

#BARRAGEM: Umidade, Solo
x = RECUPERACAO["MEDIA"]
mBarragem = np.eye(5)
mBarragem[0,0] = 1 + x
mBarragem[4,4] = 1 + x
barragem = Impacto("Barragem Subterrânea", mBarragem)

#CISTERNA
cisterna = Impacto("Cisternas", np.eye(5), incremento=[0.1, 0, 0, 0, 0])

#EDUCAÇÃO: Solo
"""
x = RECUPERACAO["BAIXA"]
mEducacao = np.eye(5)
mEducacao[4,4] = 1 + x
educacao = Impacto("Educação", mEducacao)
"""

#AGRICULTURA DE CONSERVAÇÃO: Fertilidade, Solo
x = RECUPERACAO["MEDIA"]
mAgric = np.eye(5)
mAgric[1,1] = 1 + x
mAgric[4,4] = 1 + x
agriculturaConservacao = Impacto("Agricultura de conservação", mAgric)

#SISTEMAS AGROFLORESTAIS: Umidade, Solo
x = RECUPERACAO["MEDIA"]
mSistemas = np.eye(5)
mSistemas[0,0] = 1 + x
mSistemas[4,4] = 1 + x
sistemas = Impacto("Sistemas agroflorestais", mSistemas)