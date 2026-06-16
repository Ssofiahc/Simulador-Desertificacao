import numpy as np

class Estado:

    def __init__(self, umidade, fertilidade, biodiversidade, vegetacao, solo):
        self.valores = np.array([umidade, fertilidade, biodiversidade, vegetacao, solo], dtype= float)
        self.labels = ["Umidade", "Fertilidade", "Biodiversidade", "Vegetação", "Solo"]

    def clip(self):
        self.valores = np.clip(self.valores, 0, 1)

    def __getitem__(self, item):
        id = self.labels.index(item)
        return self.valores[id]
    
    def __str__(self):
        return "|".join([f"{l}: {v:.2f}" for l, v in zip(self.labels, self.valores)])