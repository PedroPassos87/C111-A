import pandas as pd
import numpy as np

#SERIES 1D
dic = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(dic)
s2 = pd.Series(data=[20,30,40],index=['b', 'c', 'd'])
print(s + s2)                              #Adding two series with different indixes, a exists in S but not in S2 so it is added to the new Series with NaN 
print(s.add(s2, fill_value=0))             #Adding two series with different indexes and filling the missing values with zero
                                           #usar funções pré prontas do numpy  para realizar operações entre series com elementos nulos


print(s['a'])
print(s[['b', 'c']])                       #primeiro par de [] é a series, o segundo [] é a lista de valores que quero ver


print(s[s > 10])                           #condicional

#DATAFRAME 2D

df =  pd.DataFrame(columns=['X', 'Y', 'Z'], index= ['A', 'B','C'], data= np.random.randint(1,50, [3,3])) 

print(df)

print(df.loc['B','C'], ['X', 'Y', 'Z'])       #slicing
print(df.iloc[1:,:])                          #slicing

#ler um dataset no pandas
dfp = pd.read_csv('paises.csv',delimiter=';')
print(dfp)

#colunas do dataset
print(dfp.columns)

#Apenas nomes dos paises
print(df['Country'])

# 3 primeiros paises
print(df.head(3))

# ultimos 3 paises
print(df.tail(3))
