import numpy as np

#Definição das constantes
kb = 1.380649e-23
hbar = 1.05457182e-34

#função para cáculo da capacidade térmica utilizando as densidades de estados experimentais
def cv_densidade_experimental(omega, densidade_estados, tempLista, d_atomica):
    #para obter em termos de 1 mol, que será o utilizado, dividimos a densidade de estados pela densidade atomica dividida por 1 mol,
    #uma vez que os dados utilizados no projeto medem a densidade de estados para um metro cúbico de moléculas
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
