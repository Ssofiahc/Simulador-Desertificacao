import numpy as np
import itertools
from Bioma import Bioma
from Gatilho import Gatilho
from Impacto import Impacto
from Estado import Estado
from Validacao_json import valida
from Gera_grafico import gera_grafico
import FatorImpacto
import FatorRecuperacao
from FatorEnfrentamento import fatorEnfrentamento

# 0.Umidade 1.fertilidade 2.Biodivesidade 3.Vegetação 4.Solo

if __name__== "__main__":

    # Configurações da simulação:
    config = valida()
    print(f"Configuração do bioma '{config.get('nome_bioma', 'Desconhecido')}' foi bem sucedida!")

    # "Tradução" do JSON para o Python
    # Mapas:
    mapa_impacto = {
        "desmatamento": FatorImpacto.desmatamento,
        "irrigacao": FatorImpacto.irrigacao,
        "sobrepastoreio": FatorImpacto.sobrepastoreio,
        "manejo": FatorImpacto.manejo,
        "mudancas": FatorImpacto.mudancas
    }

    mapa_recuperacao = {
        "reflorestamento": FatorRecuperacao.reflorestamento,
        "barragem": FatorRecuperacao.barragem,
        "cisterna": FatorRecuperacao.cisterna,
        "sistemas": FatorRecuperacao.sistemas,
        "agricultura": FatorRecuperacao.agriculturaConservacao
    }

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
    mErosao[1,1] = 0.3 #x = 0.8
    mErosao[4,4] = 0.3 #x = 0.8
    erosao = Impacto("Erosão", mErosao)

    gatilhoErosao = Gatilho(
        nome="Erosão",
        condicao=lambda est: est["Vegetação"] < 0.3,
        impacto=erosao
    )

    bioma = Bioma(
        config["nome_bioma"],
        config["estado_inicial"],
        config["taxa_recuperacao"]
    )

    for nome_impacto in config.get("impacto_inicial", []):
        if nome_impacto in mapa_impacto:
            bioma.fatorManual.append(mapa_impacto[nome_impacto])

    for nome_recuperacao in config.get("recuperacao_inicial", []):
        if nome_recuperacao in mapa_recuperacao:
            bioma.fatorManual.append(mapa_recuperacao[nome_recuperacao])

    print("Estado Inicial:", bioma.estado)
    print("")

    #Gatilhos:

    bioma.addGatilho(gatilhoQueimadas)
    bioma.addGatilho(gatilhoErosao)

    #Fatores Enfrentamento:

    #Pesquisa: cerca de 90% do desmatamento na caatinga é ilegal, portanto a fiscalisação rigoroza diminuiria o impacto em 90% (0.9)
    fiscalizacao = fatorEnfrentamento("Fiscalização Rigorosa", FatorImpacto.desmatamento, 0.9)

    educacao = fatorEnfrentamento("Educação", FatorImpacto.manejo, 0.2)

    #Pesquisa: pastejo rotativo reduzirá em 80% o sobrepastoreio
    pastejo_rotativo = fatorEnfrentamento("Pastejo Rotativo", FatorImpacto.sobrepastoreio, 0.8)

    #Armazenando os dados para o gráfico de saída:
    historico_anos = []
    historico_umidade = []
    historico_fertilidade = []
    historico_biodiversidade = []
    historico_vegetacao = []
    historico_solo = []

    for ano in itertools.count(0, 1):
        if np.all(bioma.estado.valores > 0.3):

            #Bioma suportou mais de dois anos: politicas públicas (Fiscalização, Educação, Pastejo Rotativo)
            if ano == 2:

                bioma.fatorManual.append(fiscalizacao)
                bioma.fatorManual.append(educacao)
                bioma.fatorManual.append(pastejo_rotativo)

                if FatorImpacto.desmatamento in bioma.fatorManual:
                    print("Fisacalização rigorosa iniciada!")

                if FatorImpacto.manejo in bioma.fatorManual:
                    print("Educação iniciada!")

                if FatorImpacto.sobrepastoreio in bioma.fatorManual:
                    print("Pastejo Rotativo iniciado!")

            bioma.ciclo()
            print(f"ano: {ano} - {bioma.estado}")

            historico_anos.append(ano)
            historico_umidade.append(bioma.estado["Umidade"])
            historico_fertilidade.append(bioma.estado["Fertilidade"])
            historico_biodiversidade.append(bioma.estado["Biodiversidade"])
            historico_vegetacao.append(bioma.estado["Vegetação"])
            historico_solo.append(bioma.estado["Solo"])

            #Caso todos os valores atinjam o máximo (1), simulação encerra 
            if np.all(bioma.estado.valores == 1):
                print(f"Ano {ano}: bioma completamente recuperado, simulação encerrada.")
                break
            
        else:
            print(f"Ano {ano}: bioma irrecuperável, simulação encerrada.")
            break
        
    print("")
    print("Construindo gráfico!")
    
    gera_grafico(
        historico_anos, 
        historico_umidade, 
        historico_fertilidade, 
        historico_biodiversidade, 
        historico_vegetacao, 
        historico_solo, 
        bioma.nome
    )

    print("Gráfico concluido!")