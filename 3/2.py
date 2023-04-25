import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# cargar el archivo csv
dataset = pd.read_csv('C:/Users/ASUS/Documents/umsa - informática/2023 I/01. INF 354/1erParcial354/1/dataset.csv')

# normalizar valores numéricos
scaler = MinMaxScaler()
dataset[['columna1', 'columna2']] = scaler.fit_transform(dataset[['columna1', 'columna2']])

# imprimir el conjunto de datos
print(dataset.head())
