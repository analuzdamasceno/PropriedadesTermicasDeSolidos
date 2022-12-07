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
omega_gan_einstein = sum(omega_gan)/len(omega_gan)

#definindo uma faixa de temperaturas
temperaturas = np.linspace(0.01,2000,10000)

#calculando as capacidades térmicas para os diferentes modelos, sabendo que a 
#velocidade do som no GaN é 6510 m/s (fonte: https://www2.phys.uniroma1.it/doc/caprara/SCaprara/SC-scritto-21012020-CMP.pdf) e que sua densidade atômica é
#4.28e28 átomos/m³

cv_gan_einstein = cv_einstein(omega_gan_einstein, 2*6.02e23, temperaturas)
cv_gan_debye = cv_debye(omega_gan, temperaturas, 7000, 2*6.02e23, 4.28e28)
cv_gan_experimental = cv_densidade_experimental(omega_gan, densidade_estados_gan, temperaturas, 4.28e28)


#plotando as densidades de estados experimentais e os resultados das capacidades térmicas
fig, ax = plt.subplots(1,2, figsize=(15,5))
ax[0].plot(omega_gan,densidade_estados_gan)
ax[0].set_xlabel('Frequências de vibração')
ax[0].set_ylabel('Densidades de estados')

ax[1].plot(temperaturas, cv_gan_einstein, label='Einstein')
ax[1].plot(temperaturas, cv_gan_debye, label='Debye')
ax[1].plot(temperaturas, cv_gan_experimental, label='Experimental')
ax[1].set_xlabel('Temperatura (K)')
ax[1].set_ylabel('Capacidade térmica (J/K)')
ax[1].legend()
plt.show()
