import numpy as np
import itertools
from Bioma import Bioma
from Gatilho import Gatilho
from Impacto import Impacto
import FatorImpacto
import FatorRecuperacao
from Estado import Estado
from FatorEnfrentamento import fatorEnfrentamento
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

    #TESTE:

    # 0 - Umidade, 1 - Fertilidade, 2 - Biodiversidade, 3 - Vegetação, 4 - Solo
    caatinga = Bioma("Caatinga", [0.5, 0.6, 0.5, 0.7, 0.6], [0.01]*5)

    #Gatilhos:

    caatinga.addGatilho(gatilhoQueimadas)
    caatinga.addGatilho(gatilhoErosao)

    #Fatores Impacto:

    caatinga.fatorManual.append(FatorImpacto.desmatamento)
    #caatinga.fatorManual.append(FatorImpacto.irrigacao)
    #caatinga.fatorManual.append(FatorImpacto.sobrepastoreio)
    #caatinga.fatorManual.append(FatorImpacto.manejo)
    #caatinga.fatorManual.append(FatorImpacto.mudancas)
    

    #Fatores Recuperação:

    caatinga.fatorManual.append(FatorRecuperacao.reflorestamento)
    #caatinga.fatorManual.append(FatorRecuperacao.barragem)
    #caatinga.fatorManual.append(FatorRecuperacao.cisterna)
    #caatinga.fatorManual.append(FatorRecuperacao.sistemas)
    #caatinga.fatorManual.append(FatorRecuperacao.agriculturaConservacao)

    #Fatores Enfrentamento:

    #Pesquisa: cerca de 90% do desmatamento na caatinga é ilegal, portanto a fiscalisação rigoroza diminuiria o impacto em 90% (0.9)
    fiscalizacao = fatorEnfrentamento("Fiscalização Rigorosa", FatorImpacto.desmatamento, 0.9)
    educacao = fatorEnfrentamento("Educação", FatorImpacto.manejo, 0.2)
    #Pesquisa: pastejo rotativo reduzirá em 80% o sobrepastoreio
    pastejo_rotativo = fatorEnfrentamento("Pastejo Rotativo", FatorImpacto.sobrepastoreio, 0.8)

    for ano in itertools.count(0, 1):
        if np.all(caatinga.estado.valores > 0.3):

            #Bioma suportou mais de dois anos: politicas públicas (Fiscalização, Educação, )
            if ano == 2:

                caatinga.fatorManual.append(fiscalizacao)
                caatinga.fatorManual.append(educacao)

                if FatorImpacto.desmatamento in caatinga.fatorManual:
                    print("Fisacalização rigorosa iniciada!")

                if FatorImpacto.manejo in caatinga.fatorManual:
                    print("Educação iniciada!")

            caatinga.ciclo()
            print(f"ano: {ano} - {caatinga.estado}")

            #Caso todos os valores atinjam o máximo (1), simulação encerra 
            if np.all(caatinga.estado.valores == 1):
                print(f"Ano {ano}: bioma completamente recuperado, simulação encerrada.")
                break
            
        else:
            print(f"Ano {ano}: bioma irrecuperável, simulação encerrada.")
            break