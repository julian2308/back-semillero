import pandas as pd

print("xd")

# leer el archivo de excel
datos = pd.read_excel('prueba2.xlsx', sheet_name="Sheet1",header=7, skipfooter=4)
outfile = 'resultados.txt'
file = open(outfile, 'w')
file.write(f'Promedio: {datos["Tasa de cambio representativa del mercado (TRM)"].mean()}\n')
file.write(f'Máximo: {datos["Tasa de cambio representativa del mercado (TRM)"].max()}\n')
file.write(f'Mínimo: {datos["Tasa de cambio representativa del mercado (TRM)"].min()}\n')
file.close()

