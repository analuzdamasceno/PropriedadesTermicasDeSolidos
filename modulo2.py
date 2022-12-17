import numpy as np

#Definição das constantes: constante de Boltazmann e h barra (constante de Plack sobre 2 pi)
kb = 1.380649e-23
hbar = 1.05457182e-34

#criando a funcao densidade de estados de Debye
def densidade_debye(omega, v, densidade_atomica):
    d_debye = []
    #frquência de Debye
    omega_d = (6*(np.pi**2)*densidade_atomica*(v**3))**(1/3)
    for w in omega:
        if w<omega_d:
            d_debye.append((3*(w**2)/(2*(np.pi**2)*(v**3))))
        else:
            d_debye.append(0)
    return d_debye

#função da capacidade térmica Debye: retorna uma lista com as capacidades térmicas calculadas
# com base no modelo de Debye para uma dada lista de temperaturas, uma lista com as frequências
# omega, a velocidade do som no sólido, o número N de átomos e a densidade atômica do sólido.
def cv_debye(omega, TempLista, v, N, densidade_atomica):
    #funçao a ser integrada numericamente para cada omega
    def f(x):
        return ((x**4)*np.exp(x)/(np.exp(x)-1)**2)
    c_debye = []
    #temperatura de debye
    temp_debye = hbar*v*((6*(np.pi**2)*densidade_atomica)**(1/3))/kb
    #cálculo da capacidade térmica integrando a função sobre a lista omega para uma dada temperatura
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
    #cálculo da capacidade térmica para cada temperatura
    for temp in TempLista:
        c_debye.append(cv(omega,temp))
    return c_debye
