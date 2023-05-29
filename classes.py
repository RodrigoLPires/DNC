# class Carro():
#     def __init__(self, marca, modelo, cor):
#         self.marca = marca
#         self.modelo = modelo
#         self.cor = cor
    
#     def display(self):
#         tipo = self
#         print("O objeto é", tipo, self)

# obj = Carro(marca='Renault', modelo='Sandero', cor='Prata')

# print(Carro.display(obj.modelo))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_csv('C:\\Users\\Rodri\\OneDrive\\Área de Trabalho\\Produção por Tecnologia.csv')
df = pd.DataFrame(arquivo)

novo = pd.DataFrame(
    [
        [1,2,3],
        [4,5,6]
    ]
)

plt.xticks(novo[2], novo[0])
plt.show()