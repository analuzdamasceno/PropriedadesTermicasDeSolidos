import numpy as np

#Definição das constantes
kb = 1.380649e-23
hbar = 1.05457182e-34

''' função que retorna uma lista com as capacidades térmicas calculadas por meio do modelo de Einstein
para cada temperatura dada, calculada a partir de um valor de omega, um número N de átomos 
e uma lista com o intervalo de temperatura '''
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
