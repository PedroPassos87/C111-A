import numpy as np

#1
arr = np.loadtxt('projetoC111A/paises.csv', delimiter=';', dtype=str, encoding='utf-8')
arr2 = arr[:,:4].copy()
print(arr2)

#2
array_regiao = arr[1:,1].copy() #excluindo cabeçalho 
print("Quantidade de regioes:",np.unique(array_regiao).size)
print(np.unique(array_regiao))  #printando regioes

#3
literacy =  arr[1:,9].astype(float)
print("Porcentagem de alfabetismo:",np.mean(literacy),"%")

#4
cond = np.char.find(array_regiao, 'NORTHERN AMERICA') >= 0
print("Numero de paises da america do sul:",array_regiao[cond].size)

#5
cond2 = np.char.find(array_regiao, 'LATIN AMER. & CARIB') >= 0
gdp = arr[1:,8][cond2].astype(float)

print("Maior renda america latina:",np.max(gdp))
