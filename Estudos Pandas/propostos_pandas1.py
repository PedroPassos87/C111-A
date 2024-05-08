import pandas as pd
import numpy as np

df = pd.read_csv('Estudos Pandas/paises.csv',delimiter=';')
#print(df)

#Mostrando paises da oceania 
oceania = df[df['Region'].str.contains('OCEANIA')]
print(oceania['Country'])
print('Quantidade de países na oceania:',oceania['Country'].size)

print('*************************')

#Media da taxa de alfabetização do mundo
media = df['Literacy (%)'].mean()
print('Media da taxa de alfabetizacao no mundo:',media)


# Encontrar o país com a maior população
maior_pais = df.loc[df['Population'].idxmax(), ['Country','Region']]

print("País com a maior população:", maior_pais)

print('******************************')

#Paises que nao possuem costa maritima
cond = df['Coastline (coast/area ratio)'] == 0.00
costa = df.loc[cond,'Country']
print('Países sem costa maritima:', costa)


