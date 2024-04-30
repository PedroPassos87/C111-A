import numpy as np

#numeros aleatorios
#random

#arr = np.random.randint(1,11,15)  #gerar 15 numeros inteiros e aleatorios de 1 a 10
#Ex saida: [ 7  3  1  7  2  2 10  6  7  9  3  7  2  9  8]

#seed = um valor escalar que alimenta o algoritmo de geração de numeros aleatorios
np.random.seed(10) #valores aleatorios serão iguais independente da maquina
arr = np.random.randint(1,11,15)
#print(arr)

# extraindo elementos unicos
#print(np.unique(arr, return_counts=True))

# OPERAÇOES EM MATRIZES
mtz = arr.reshape(3,5)
print(mtz)
#print(mtz.sum(axis=1)[0]) #somatória dos valores por linhas retornando somente a da primeira linha

#BROADCASTING = operação entre um array e um escalar
#print(mtz*0.5)

#CONDICIONAIS
print(np.unique(mtz[mtz%2==0]))

# ANALISE TEXTUAL
# char
arr = np.array(['Pedro','Arthur', 'Ana', 'Maciel'])
print(np.char.find(arr, 'a'))
cond = np.char.find(arr, 'a') >= 0
print(arr[cond])