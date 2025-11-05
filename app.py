# ¿Cual seria el precio de venta al que tendria
# que poner mi vivienda para que este alineado con el mercado?

# 1-Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

# 2-Importacion de fuentes de datos
df_data = pd.read_excel(r'files\viviendas_Madrid.xlsx', sheet_name='Datos_Históricos')

print(df_data.info())

print(df_data.head())

# 3-Analisis de datos (EDA) y Preprocesado

# 3.1-Analisis de valores nulos. Comprobar cuantos valores nulos existen en cada columna
print(df_data.isnull().sum())

# 3.2-Eliminar variables que tienen un alto porvcentaje de registros con valores nulos
df_var = df_data.isnull().sum()
porcentaje_eliminacion = 0.1  # 10%
df_var = df_var[df_var < porcentaje_eliminacion * len(
    df_data)]  # Nos quedamos con las variables que tienen menos del 10% de valores nulos
lista_variables_ok = df_var.index # Lista de variables que se quedan
df_data = df_data[lista_variables_ok] # filtramos el dataframe original y nos quedamos solo con las variables ok
print(df_data.head())

# 3.3-Eliminar registros que tienen valores nulos en las variables restantes(se podria interpolar)
df_data = df_data.dropna()

print(df_data.isnull().sum())  # Comprobamos que ya no hay valores nulos

print(df_data.describe().transpose())  # Descripcion estadistica de las variables numericas
