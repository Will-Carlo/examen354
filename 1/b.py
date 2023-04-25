import pandas as pd
import numpy as np

# Carga del archivo csv en un DataFrame
df = pd.read_csv('C:/Users/ASUS/Documents/umsa - informática/2023 I/01. INF 354/1erParcial354/1/dataset.csv')

# Cálculo de la media con numpy
mean = np.mean(df, axis=0)

# Cálculo de la moda con pandas
mode = df.mode()

# Cálculo de los cuartiles y percentiles con numpy
quartiles = np.percentile(df, [25, 50, 75], axis=0)
percentiles = np.percentile(df, [10, 25, 50, 75, 90], axis=0)

