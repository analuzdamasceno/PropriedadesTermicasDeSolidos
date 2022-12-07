from extracaoDados import*
import matplotlib.pyplot as plt
import numpy as np

#Definição das constantes
kb = 1.380649e-23
hbar = 1.05457182e-34

def cv_densidade_experimental(omega, densidade_estados, tempLista, d_atomica):
    def f(w, temp,d_omega):
        return (d_omega/(d_atomica/6.02e23)*np.exp((hbar*w)/(kb*temp))*((hbar*w/temp)**2))/(kb*(np.exp((hbar*w)/(kb*temp))-1)**2)
    def cv(omega, densidade_estados, temp):
        h = (omega[-1]-omega[0])/len(omega)
        inte = f(omega[0], temp, densidade_estados[0]) + f(omega[-1], temp, densidade_estados[-1])
        for i in range(1,len(omega)):
            inte += 2*f(omega[i], temp, densidade_estados[i])
        inte = inte*(h/2)
        return inte
    c_dados = []
    for temp in tempLista:
        c_dados.append(cv(omega, densidade_estados, temp))
    return c_dados


temperaturas = np.linspace(0.01, 1000, 5000)
cv_dados_si = cv_densidade_experimental(omega_si, densidade_estados_si, temperaturas, 4.99e28)
cv_dados_gan = cv_densidade_experimental(omega_gan, densidade_estados_gan, temperaturas, 4.28e28)
#plt.plot(temperaturas, cv_dados_si)
#plt.plot(temperaturas, cv_si_einstein, label = 'Silício Einstein')
#plt.grid()
#plt.show()
