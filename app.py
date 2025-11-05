#¿Cual seria el precio de venta al que tendria
#que poner mi vivienda para que este alineado con el mercado?

#1-Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

#2-Importacion de fuentes de datos
df_data = pd.read_excel(r'files\viviendas_Madrid.xlsx',sheet_name='Datos_Históricos')

print(df_data.info())

print(df_data.head())



