import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# cargar el archivo csv
dataset = pd.read_csv('C:/Users/ASUS/Documents/umsa - informática/2023 I/01. INF 354/1erParcial354/1/dataset.csv')

# codificar variables categóricas
encoder = OneHotEncoder()
categoricas = ['columna3']
encoder.fit(dataset[categoricas])
encoded = pd.DataFrame(encoder.transform(dataset[categoricas]).toarray(), columns=encoder.get_feature_names())
dataset = pd.concat([dataset, encoded], axis=1).drop(categoricas, axis=1)

# imprimir el conjunto de datos
print(dataset.head())
