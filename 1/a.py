import csv

# Lectura del archivo csv
with open('C:/Users/ASUS/Documents/umsa - informática/2023 I/01. INF 354/1erParcial354/1/dataset.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader) # Encabezado de las columnas
    data = list(reader) # Lista de los datos

# Separación de cada columna en una lista
column1 = [int(row[0]) for row in data]
#column2 = [int(row[1]) for row in data]
#column3 = [int(row[2]) for row in data]
#column4 = [int(row[3]) for row in data]
column5 = [int(row[4]) for row in data]
#column6 = [int(row[5]) for row in data]
column7 = [int(row[6]) for row in data]
#column8 = [int(row[7]) for row in data]
column9 = [int(row[8]) for row in data]
#column10 = [int(row[9]) for row in data]
#column11 = [int(row[10]) for row in data]

# Cálculo de la media
mean_column1 = sum(column1) / len(column1)
#mean_column2 = sum(column2) / len(column2)
#mean_column3 = sum(column3) / len(column3)
#mean_column4 = sum(column4) / len(column4)
mean_column5 = sum(column5) / len(column5)
#mean_column6 = sum(column6) / len(column6)
mean_column7 = sum(column7) / len(column7)
#mean_column8 = sum(column8) / len(column8)
mean_column9 = sum(column9) / len(column9)
#mean_column10 = sum(column10) / len(column10)
#mean_column11 = sum(column11) / len(column11)

# Cálculo de la moda
def calculate_mode(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    mode = max(count, key=count.get)
    return mode

mode_column1 = calculate_mode(column1)
#mode_column2 = calculate_mode(column2)
#mode_column3 = calculate_mode(column3)
#mode_column4 = calculate_mode(column4)
mode_column5 = calculate_mode(column5)
#mode_column6 = calculate_mode(column6)
mode_column7 = calculate_mode(column7)
#mode_column8 = calculate_mode(column8)
mode_column9 = calculate_mode(column9)
#mode_column10 = calculate_mode(column10)
#mode_column11 = calculate_mode(column11)

# Cálculo de los cuartiles
def calculate_quartiles(lst):
    sorted_lst = sorted(lst)
    q1 = sorted_lst[int(len(sorted_lst) * 0.25)]
    q2 = sorted_lst[int(len(sorted_lst) * 0.5)]
    q3 = sorted_lst[int(len(sorted_lst) * 0.75)]
    return q1, q2, q3

q1_column1, q2_column1, q3_column1 = calculate_quartiles(column1)
#q1_column2, q2_column2, q3_column2 = calculate_quartiles(column2)
#q1_column3, q2_column3, q3_column3 = calculate_quartiles(column3)
#q1_column4, q2_column4, q3_column4 = calculate_quartiles(column4)
q1_column5, q2_column5, q3_column5 = calculate_quartiles(column5)
#q1_column6, q2_column6, q3_column6 = calculate_quartiles(column6)
q1_column7, q2_column7, q3_column7 = calculate_quartiles(column7)
#q1_column8, q2_column8, q3_column8 = calculate_quartiles(column8)
q1_column9, q2_column9, q3_column9 = calculate_quartiles(column9)
#q1_column10, q2_column10, q3_column10 = calculate_quartiles(column10)
#q1_column10, q2_column10, q3_column10 = calculate_quartiles(column11)



# Cálculo de los percentiles
p10_column1 = sorted(column1)[int(len(column1) * 0.1)]
p25_column1 = sorted(column1)[int(len(column1) * 0.25)]
p50_column1 = sorted(column1)[int(len(column1) * 0.5)]
p75_column1 = sorted(column1)[int(len(column1) * 0.75)]
p90_column1 = sorted(column1)[int(len(column1) * 0.9)]
