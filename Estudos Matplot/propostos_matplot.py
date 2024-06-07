import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('c:/Users/peaga/Documents/Estudos/C111/Estudos Matplot/space.csv', delimiter=';')       #lendo dataset

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