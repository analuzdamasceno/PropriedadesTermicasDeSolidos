from extracaoDados import*
from modulo1 import*
from modulo2 import*
from modulo3 import*
import warnings
import numpy as np
import matplotlib.pyplot as plt

#o numpy gera um aviso de estar usando o exponencial de um grande numero,
#mas o modulo lida normalmente com o calculo, logo podemos ignorar o aviso
warnings.filterwarnings('ignore')

#calculando a média das frequências de vibração para utilizar no modelo de Einstein
omega_si_einstein = sum(omega_si)/len(omega_si)

#definindo uma faixa de temperaturas
temperaturas = np.linspace(0.01,2000,10000)

#calculando as capacidades térmicas para os diferentes modelos, sabendo que a 
#velocidade do som no Silício é 2200 m/s (fonte: ) e que sua densidade atômica é
#4.99e28 átomos/m³

cv_si_einstein = cv_einstein(omega_si_einstein, 6.02e23, temperaturas)
cv_si_debye = cv_debye(omega_si, temperaturas, 2200, 6.02e23, 4.99e29)
cv_si_experimental = cv_densidade_experimental(omega_si, densidade_estados_si, temperaturas, 4.99e28)

#plotando as densidades de estados experimentais e os resultados das capacidades térmicas
fig, ax = plt.subplots(1,2, figsize=(15,5))
ax[0].plot(omega_si,densidade_estados_si)
ax[0].set_xlabel('Frequências de vibração')
ax[0].set_ylabel('Densidades de estados')

ax[1].plot(temperaturas, cv_si_einstein, label='Einstein')
ax[1].plot(temperaturas, cv_si_debye, label='Debye')
ax[1].plot(temperaturas, cv_si_experimental, label='Experimental')
ax[1].set_xlabel('Temperatura (K)')
ax[1].set_ylabel('Capacidade térmica (J/K)')
ax[1].legend()
plt.show()


