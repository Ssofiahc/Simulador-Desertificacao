import matplotlib.pyplot as plt

def gera_grafico(anos, umidade, fertilidade, biodiversidade, vegetacao, solo, nome_bioma):
    plt.figure(figsize=(11, 6))
    
    plt.plot(anos, umidade, label="Umidade", marker="o", linewidth=2)
    plt.plot(anos, fertilidade, label="Fertilidade", marker="s", linewidth=2)
    plt.plot(anos, biodiversidade, label="Biodiversidade", marker="^", linewidth=2)
    plt.plot(anos, vegetacao, label="Vegetação", marker="x", linewidth=2)
    plt.plot(anos, solo, label="Solo", marker="d", linewidth=2)

    plt.title(f"Gráfico da simulação do processo de desertificação no bioma {nome_bioma}", fontsize=14, fontweight='bold')
    plt.xlabel("Tempo (Anos)", fontsize=11)
    plt.ylabel("Índice de Integridade (0.0 - 1.0)", fontsize=11)
    plt.ylim(0, 1.05)
    plt.legend(loc="lower left")
    plt.grid(True, linestyle='--', alpha=0.5)

    nome_grafico_saida = f"grafico_{nome_bioma.lower()}.png"
    plt.savefig(nome_grafico_saida, dpi=300, bbox_inches='tight')