import numpy as np
"""
Classe Estado: 'gerencia' os valores de saúde do bioma.
-valores: array float que contém os 5 índices do estado do bioma (umidade, fertilidade, biodiversidade, vegetação e solo);
-labels: lista de strings com os nomes dos índices -> facilita a busca

"""
class Estado:

    def __init__(self, umidade, fertilidade, biodiversidade, vegetacao, solo):
        self.valores = np.array([umidade, fertilidade, biodiversidade, vegetacao, solo], dtype= float)
        self.labels = ["Umidade", "Fertilidade", "Biodiversidade", "Vegetação", "Solo"]

    # Limita os índices de valores ao intervalo [0, 1]
    def clip(self):
        self.valores = np.clip(self.valores, 0, 1)

    # Relaciona labels e valores por meio de um id
    def __getitem__(self, item):
        id = self.labels.index(item)
        return self.valores[id]
    
    # Método toString
    def __str__(self):
        return "|".join([f"{l}: {v:.2f}" for l, v in zip(self.labels, self.valores)])