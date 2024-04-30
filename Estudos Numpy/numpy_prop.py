import numpy as np

#ex 1==============================================================
arr = np.linspace(0,1, 21)
print(arr)

#ex 2==============================================================
ar1 = np.arange(0, 51, 2)   #cria array de pares de 0-50
ar2 = np.arange(100, 50, -2)   #cria array de pares de 100-50
arf = np.sort(np.concatenate([ar1,ar2]))   #concatena e ordena
print(arf)  

#ex 3=========================================================================
print(np.flip(arf)) #decrescente

#ex4==============================================================
matriz1s = np.ones([3, 4]) #matriz de 1s 
array1D = matriz1s.reshape(-1)  #transforma em um array 1D
print(array1D)

#ex5---------------------------------------------------------------------------------
m = np.zeros([3,7]) #criando matriz de 0s
x,y = m.shape  #extraindo linhas,colunas
var = x*y  #encontrando numero de elementos

if(var%2 == 0):
    print("Essa matriz viraria um vetor com numero par de elementos")

else:
    print("Essa matriz viraria um vetor com numero impar de elementos")
