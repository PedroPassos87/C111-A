import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# plot simples
x = np.array([1,2,3,4])
y = x*2                         #broadcasting
y2 = x*x

#Plot 2 graficos mesma imagem
#plt.xlabel('Valores de X')
#plt.ylabel('Valores de Y')
#plt.plot(x,y, '.-m',x,y2,'*c--')
#plt.show()

#Plot 2 graficos separados
#plt.subplot(1,2,1)           #linha,coluna,lock
#plt.title('linear')
#plt.plot(x,y,'m-')
#plt.subplot(1,2,2)
#plt.title('exponencial')
#plt.plot(x,y2,'c--')
#plt.show()


#SCATTER PLOT
df = pd.read_csv('c:/Users/peaga/Documents/Estudos/C111/Estudos Matplot/paises.csv', delimiter=';')       #lendo dataset
df2 = df.nlargest(6, 'Area (sq. mi.)')        #extraindo dados somente dos 6 maiores paises do mundo

#Plotando qual pais possui a maior renda per capita e o tamanho de cada ponto ilustra o tamanho do pais
plt.scatter(x= df2['Country'],y=df2['Area (sq. mi.)'], s=df2['GDP ($ per capita)']/100)       #x,y e size
plt.show()
