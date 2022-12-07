import numpy as np
import matplotlib.pyplot as plt 
from extracaoDados import*

#Definição das constantes
kb = 1.380649e-23
hbar = 1.05457182e-34

def cv_einstein(omega,N,intervaloTemp):
    #energia dos fônons em um cristal para o modelo de Einstein
    def u_einstein(N,omega,T):
        return ((3*N*hbar*omega))/(np.exp(hbar*omega/(kb*T))-1)
    #Cáculo da capacidade térmica por derivação numérica usando o método da diferença central
    c_einstein = []
    h = 0.0001
    for temp in intervaloTemp:
        cv = (u_einstein(N, omega, (temp)+h) - u_einstein(N, omega, (temp)-h))/(2*h)
        c_einstein.append(cv)
    return c_einstein
    


#calculando a média para usar nesse modelo

omega_si_einstein = sum(omega_si)/len(omega_si)

#calculando a media
omega_gan_einstein = sum(omega_gan)/(len(omega_gan))

omega_zno_rs_einstein = sum(omega_zno_rs)/len(omega_zno_rs)

temperaturas = np.linspace(0.01, 1000, 5000)
cv_si_einstein = cv_einstein(omega_si_einstein, 6.02e23, temperaturas)
cv_gan_einstein = cv_einstein(omega_gan_einstein, 2*6.02e23, temperaturas)
#plt.plot(temperaturas, cv_si_einstein, label = 'Silício Einstein')
#plt.grid()
#plt.show()
