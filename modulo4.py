from extracaoDados import*
import numpy as np
import matplotlib.pyplot as plt

#Definição das constantes: constante de Boltazmann e h barra (constante de Plack sobre 2 pi)
kb = 1.380649e-23
hbar = 1.05457182e-34


def tau(w, temp, v, densidade_atomica):
    theta = hbar*v*((6*densidade_atomica/(np.pi))**(1/3))/(2*kb)
    tau_pe = 2.2e7 * (w**2)
    tau_v = 9.16e4 * (w**2) * temp * np.exp(-theta/(3*temp))
    t = ( tau_pe + tau_v)**(-1)
    return t 

def condutiv(omega, tempLista, v, densidade_atomica):
    def f(x, w, temp):
        return (tau(w, temp, v, densidade_atomica)*(x**4)*np.exp(x)/(np.exp(x)-1)**2)
    def k(omega, temp):
        lista_x = []
        for w in omega:
            lista_x.append(hbar*w/(kb*temp))
        imax = 1
        for i in range(len(lista_x)):
            if (lista_x[i]>((hbar*v*((6*(np.pi**2)*densidade_atomica)**(1/3))/kb)/temp)):
                imax = i
                break
        h = (lista_x[imax]-lista_x[0])/(imax+1)
        inte = f(lista_x[0], omega[0], temp) + f(lista_x[imax], omega[imax], temp)
        for i in range(1,imax):
            inte += 2*f(lista_x[i], omega[i], temp)
        inte = inte * (h/2)
        return (inte * ((kb**4) * (temp**3))/(2*(np.pi**2)*v*(hbar**3)))
    lista_k = [] 
    for temp in tempLista:
        lista_k.append(k(omega, temp)) 
    return lista_k 








