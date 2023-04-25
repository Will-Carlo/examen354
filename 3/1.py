import pandas as pd

# cargar el archivo csv
dataset = pd.read_csv('C:/Users/ASUS/Documents/umsa - informática/2023 I/01. INF 354/1erParcial354/1/dataset.csv')

# eliminar columnas irrelevantes
columnas_a_eliminar = ['columna1', 'columna3']
dataset = dataset.drop(columnas_a_eliminar, axis=1)

# imprimir el conjunto de datos
print(dataset.head())
