#¿Cual seria el precio de venta al que tendria
#que poner mi vivienda para que este alineado con el mercado?

#1-Importacion de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#2-Importacion de fuentes de datos
data = pd.read_csv(r'files\houses_Madrid.csv')
print(data.head())