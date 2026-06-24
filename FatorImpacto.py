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
taxa = x * 0.5
mDesmatamento = np.eye(5)
mDesmatamento[2,2] = 1 - taxa
mDesmatamento[3,3] = 1 - taxa
desmatamento = Impacto("Desmatamento", mDesmatamento)

#IRRIGAÇÃO INADEQUADA: Fertilidade
x = INTENSIDADE["BAIXO"]
taxa = x * 0.5
mIrrigacao = np.eye(5)
mIrrigacao[1,1] = 1 - taxa
irrigacao = Impacto("Irrigação inadequada", mIrrigacao)

#SOBREPASTOREIO: Solo, Vegetação
x = INTENSIDADE["MEDIO"]
taxa = x * 0.5
mSobrepastoreio = np.eye(5)
mSobrepastoreio[4,4] = 1 - taxa
mSobrepastoreio[3,3] = 1 - taxa
sobrepastoreio = Impacto("Sobrepastoreio", mSobrepastoreio)

#MANEJO INCORRETO: Biodiversidade, Fertilidade
x = INTENSIDADE["MEDIO"]
taxa = x * 0.5
mManejo = np.eye(5)
mManejo[2,2] = 1 - taxa
mManejo[1,1] = 1 - taxa
manejo = Impacto("Manejo incorreto da terra", mManejo)

#MUDANÇAS CLIMÁTICAS: Umidade
x = INTENSIDADE["ALTO"]
taxa = x * 0.5
mMudancas = np.eye(5)
mMudancas[0,0] = 1 - taxa
mudancas = Impacto("Mudanças Climáticas", mMudancas)