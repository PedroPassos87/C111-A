import numpy as np

#1------------
np.random.seed(5) #valores aleatorios serão iguais independente da maquina
arr = np.random.rand(10)
arr = arr*100
arr2 = arr.astype(int)
print(arr2)


#2--------------
np.random.seed(10) #valores aleatorios serão iguais independente da maquina
mtz = np.random.randint(1, 51, size=(4, 4))
print(mtz)

#3------------
mediaL = np.mean(mtz, axis=1)
print("\nMédia de cada linha:")
print(mediaL)

maiorL = np.max(mediaL)
print("\nMaior média entre as linhas:", maiorL)

mediaC = np.mean(mtz, axis=0)
print("\nMédia de cada coluna:")
print(mediaC)

maiorC = np.max(mediaC)
print("\nMaior média entre as colunas:", maiorC)

#4-------------
print(np.unique(mtz, return_counts=True))

arr3, cont = np.unique(mtz, return_counts=True)
cond = cont >= 2
print("Aparecem duas ou mais:",arr3[cond])


