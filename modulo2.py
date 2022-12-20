import numpy as np

#Definição das constantes:
kb = 1.380649e-23
'''Constante de Boltzmann'''
hbar = 1.05457182e-34
'''Constante de Planck sobre 2 pi (h barra)'''

def densidade_debye(omega, v, densidade_atomica):
    '''Função para cálculo da densidade de estados segundo o modelo de Debye, que recebe como
    parâmetros uma lista de frequências de vibração omega, a velocidade do som no sólido e a
    densidade atômica, e retorna uma lista com as densidades de estados para cada valor de 
    frequência dado.'''
    d_debye = []
    omega_d = (6*(np.pi**2)*densidade_atomica*(v**3))**(1/3)
    #frquência de Debye
    for w in omega:
        if w<omega_d:
            d_debye.append((3*(w**2)/(2*(np.pi**2)*(v**3))))
        else:
            d_debye.append(0)
    return d_debye


def cv_debye(omega, TempLista, v, N, densidade_atomica):
    '''Função para cálculo da capacidade térmica segundo o modelo Debye que recebe como parâmetros 
    uma lista de temperaturas, uma lista com as frequências de vibração omega, a velocidade do som
    no sólido, o número N de átomos da amostra e a densidade atômica do sólido, e retorna uma lista
    com as capacidades térmicas para cada temperatura dada.'''
    def f(x):
        #Função a ser integrada numericamente sobre omega
        return ((x**4)*np.exp(x)/(np.exp(x)-1)**2)
    c_debye = []
    temp_debye = hbar*v*((6*(np.pi**2)*densidade_atomica)**(1/3))/kb
    #temperatura de debye
    def cv(omega, temp):
        #cálculo da capacidade térmica integrando a função sobre a lista omega para uma dada temperatura
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
        #cálculo da capacidade térmica para cada temperatura
        c_debye.append(cv(omega,temp))
    return c_debye
