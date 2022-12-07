import numpy as np

#Definição das constantes
kb = 1.380649e-23
hbar = 1.05457182e-34

#criando a funcao densidade de estados de Debye
def densidade_debye(omega, v):
    return (3*(omega**2)/(2*(np.pi**2)*(v**3)))


#funcao da capacidade termica de debye
def cv_debye0(omega, TempLista, v, N, densidade_atomica):
    def densidade_estados(w, densidade_atomica, v):
        return (N/densidade_atomica*(w**2)/(2*(np.pi**2)*(v**3)))
    def f(w, temp,densidade_atomica,v):
        return (densidade_estados(w,densidade_atomica,v)*np.exp((hbar*w)/(kb*temp))*((hbar*w/temp)**2))/(kb*(np.exp((hbar*w)/(kb*temp))-1)**2)
    c_debye = []
    def cv(omega, temp):
        h = (omega[-1]-omega[0])/len(omega)
        inte = f(omega[0], temp, densidade_atomica, v) + f(omega[-1], temp, densidade_atomica, v)
        for w in omega[1:-1]:
            inte += 2*f(w, temp, densidade_atomica, v)
        inte = inte * (h/2)
        return inte
    for temp in TempLista:
        c_debye.append(cv(omega,temp))
    return c_debye

#segunda versão da capacidade térmica de Debye, que será a utilizada pela eficiência
def cv_debye(omega, TempLista, v, N, densidade_atomica):
    def f(x):
        return ((x**4)*np.exp(x)/(np.exp(x)-1)**2)
    c_debye = []
    temp_debye = hbar*v*((6*(np.pi**2)*densidade_atomica)**(1/3))/kb
    def cv(omega, temp):
        lista_x = []
        for w in omega:
            lista_x.append(hbar*w/(kb*temp))

        h = (lista_x[-1]-lista_x[0])/len(lista_x)
        inte = f(lista_x[0]) + f(lista_x[-1])
        for x in lista_x[1:-1]:
            inte += 2*f(x)
        inte = inte * (h/2)
        return (inte*3*N*kb*((temp/temp_debye)**3))
    for temp in TempLista:
        c_debye.append(cv(omega,temp))
    return c_debye
