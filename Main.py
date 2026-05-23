import numpy as np
import itertools
from Bioma import Bioma
from Gatilho import Gatilho
from Impacto import Impacto
import FatorImpacto
import FatorRecuperacao
# 0 - Umidade, 1 - Fertilidade, 2 - Biodiversidade, 3 - Vegetação, 4 - Solo
if __name__== "__main__":

    #Queimadas

    mQueimadas = np.eye(5)
    mQueimadas[0,0] = 0.2 #x = 0.8
    mQueimadas[3,3] = 0.2 #x = 0.8
    mQueimadas[4,4] = 0.2 #x = 0.8
    queimadas = Impacto("Queimadas", mQueimadas)

    gatilhoQueimadas = Gatilho(
        nome="Queimadas",
        condicao=lambda est: est["Umidade"] < 0.3,
        impacto=queimadas
    )

    #Erosão

    mErosao = np.eye(5)
    mErosao[1,1] = 0.2 #x = 0.8
    mErosao[4,4] = 0.2 #x = 0.8
    erosao = Impacto("Erosão", mErosao)

    gatilhoErosao = Gatilho(
        nome="Erosão",
        condicao=lambda est: est["Vegetação"] < 0.3,
        impacto=erosao
    )

    #Teste
    caatinga = Bioma("Caatinga", [0.8, 0.7, 0.5, 0.7, 0.8], [0.01]*5)
    #Gatilhos
    caatinga.addGatilho(gatilhoQueimadas)
    caatinga.addGatilho(gatilhoErosao)
    #Fatores Impacto
    caatinga.fatorManual.append(FatorImpacto.desmatamento)
    caatinga.fatorManual.append(FatorImpacto.mudancas)
    caatinga.fatorManual.append(FatorImpacto.irrigacao)
    #Fatores Recuperação
    caatinga.fatorManual.append(FatorRecuperacao.barragem)
    caatinga.fatorManual.append(FatorRecuperacao.reflorestamento)

    for ano in itertools.count(0, 1):
        if caatinga.estado["Solo"] > 0.3:
            caatinga.ciclo()
            print(f"Ano {ano}: {np.round(caatinga.estado.valores, 2)}")
        else:
            print(f"Ano {ano}: solo irrecuperável, simulação encerrada.")
            break