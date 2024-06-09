import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('space.csv', delimiter=';')       #lendo dataset

print(df.columns)

usa = df[df['Location'].str.contains('USA')]['Company Name'].nunique()
china = df[df['Location'].str.contains('China')]['Company Name'].nunique()

# Criar o gráfico de barras
labels = ['USA', 'China']
counts = [usa, china]

plt.bar(labels, counts, color=['cyan', 'red'])
plt.xlabel('País')
plt.ylabel('Q.Empresas')
plt.show()


#-------------------------------XXXX-------------------------------#

df2 = pd.read_csv('paises.csv', delimiter=';')

death = df2[df2['Region'].str.contains('NORTHERN AMERICA')]['Deathrate']
birth = df2[df2['Region'].str.contains('NORTHERN AMERICA')]['Birthrate']
#Plot 2 graficos separados
plt.subplot(1,2,1) 
plt.plot(death,'m-')
plt.subplot(1,2,2)
plt.plot(birth,'c--')
plt.show()