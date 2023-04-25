import matplotlib.pyplot as plt
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


# Gráfico de barras para la media de cada columna
plt.bar(df.columns, mean)
plt.title('Media de cada columna')
plt.xlabel('Columnas')
plt.ylabel('Media')
plt.show()

# Gráfico de barras para la moda de cada columna
plt.bar(df.columns, mode.iloc[0])
plt.title('Moda de cada columna')
plt.xlabel('Columnas')
plt.ylabel('Moda')
plt.show()

# Gráfico de caja para los cuartiles de cada columna
plt.boxplot(df)
plt.title('Cuartiles de cada columna')
plt.xlabel('Columnas')
plt.ylabel('Valores')
plt.show()

# Gráfico de línea para los percentiles de cada columna
plt.plot(np.percentile(df, [10, 25, 50, 75, 90], axis=0))
plt.title('Percentiles de cada columna')
plt.xlabel('Columnas')
plt.ylabel('Valores')
plt.legend(['P10', 'P25', 'P50', 'P75', 'P90'])
plt.show()
