import numpy as np
from Impacto import Impacto

INTENSIDADE = {
    "BAIXO": 0.3,
    "MEDIO": 0.5,
    "ALTO": 0.8
}
# 0 - Umidade, 1 - Fertilidade, 2 - Biodiversidade, 3 - Vegetação, 4 - Solo

#DESMATAMENTO: Biodiversidade, Vegetação
x = INTENSIDADE["ALTO"]
mDesmatamento = np.eye(5)
mDesmatamento[2,2] = 1 - x
mDesmatamento[3,3] = 1 - x
desmatamento = Impacto("Desmatamento", mDesmatamento)

#IRRIGAÇÃO IRRESPONSÁVEL: Fertilidade
x = INTENSIDADE["BAIXO"]
mIrrigacao = np.eye(5)
mIrrigacao[1,1] = 1 - x
irrigacao = Impacto("Irrigação irresponsável", mIrrigacao)

#SOBREPASTOREIO: Solo, Vegetação
x = INTENSIDADE["MEDIO"]
mSobrepastoreio = np.eye(5)
mSobrepastoreio[4,4] = 1 - x
mSobrepastoreio[3,3] = 1 - x
sobrepastoreio = Impacto("Sobrepastoreio", mSobrepastoreio)

#MANEJO INCORRETO: Biodiversidade, Fertilidade
x = INTENSIDADE["MEDIO"]
mManejo = np.eye(5)
mManejo[2,2] = 1 - x
mManejo[1,1] = 1 - x
manejo = Impacto("Manejo incorreto da terra", mManejo)

#MUDANÇAS CLIMÁTICAS: Umidade
x = INTENSIDADE["ALTO"]
mMudancas = np.eye(5)
mMudancas[0,0] = 1 - x
mudancas = Impacto("Mudanças Climáticas", mMudancas)