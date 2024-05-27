import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# plot simples
x = np.array([1,2,3,4])
y = x*2                         #broadcasting
y2 = x*x

#Plot 2 graficos mesma imagem
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.plot(x,y, '.-m',x,y2,'*c--')
plt.show()

#Plot 2 graficos separados
plt.subplot(1,2,1)           #linha,coluna,lock
plt.title('linear')
plt.plot(x,y,'m-')
plt.subplot(1,2,2)
plt.title('exponencial')
plt.plot(x,y2,'c--')
plt.show()
