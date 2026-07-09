import argparse
import json
import os
import sys

# Valida o arquivo json, que contém as informações de entrada para o simulador
def valida():
    
    # Descreve o que o programa faz e retorna mensagem de ajuda para mostrar como executar o programa
    parser = argparse.ArgumentParser(
        description="Simulador do Processo de Desertificação no Brasil.",
        epilog="Exemplo: python Main.py configuracao.json"
    )
    parser.add_argument("arquivo_json", help="Informe o caminho para o arquivo de configuração")

    args = parser.parse_args()
    caminho = args.arquivo_json

    #Se não terminar com ".json" retorna erro
    if not caminho.lower().endswith(".json"):
        print("ERRO! Por favor, forneça um arquivo '.json'")
        sys.exit(1)
    
    #Se não for um arquivo (se for uma pasta, por exemplo) retorna erro
    if not os.path.isfile(caminho):
        print("""ERRO! Arquivo não encontrado.
              Confira se ele possui o nome correto e se está na mesma pasta do programa.""")
        sys.exit(1)
    
    # Testa o arquivo, se tiver erro de formatação JSON ou outro outro problema retorna erro
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
        
    except json.JSONDecodeError as erro:
        print(f"ERRO! O arquivo '{caminho}' possui erros de formatação JSON.")
        print(f"Corrija: {erro}")
        sys.exit(1)

    except Exception as erro:
        print(f"Erro ao tentar ler o arquivo '{caminho}': {erro}")
        sys.exit(1)