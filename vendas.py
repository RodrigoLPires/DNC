import pandas as pd
import numpy as np

caminho = "C:\\Users\\Rodri\\OneDrive\\Área de Trabalho\\Ciência de Dados\\Teste Tabelas\\Vendas.xlsx"

vendas = pd.read_excel(caminho)

coluna_produto = vendas["Produto"]
coluna_nulo = pd.notnull(vendas["Produto"])
verdade = vendas.Produto == "Geladeira Duplex"
vendas.rename(columns={"Unnamed: 12": "Coluna em Branco 1", "Unnamed: 13": "Coluna em Branco 2"}, inplace = True)

print(vendas.info())
# type(vendas)
# vendas.info()