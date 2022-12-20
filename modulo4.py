from extracaoDados import*
import numpy as np
import matplotlib.pyplot as plt

#Definição das constantes:
kb = 1.380649e-23
'''Constante de Boltzmann'''
hbar = 1.05457182e-34
'''Constante de Planck sobre 2 pi (h barra)'''

def tau(w, temp, v, densidade_atomica):
    '''Função para calcular o tempo entre as colisões entre fônons, que recebe como
    parâmetros uma frequência de vibração omega (w), uma temperatura, a velocidade do som
    no sólido e a densidade atômica.'''
    theta = hbar*v*((6*densidade_atomica/(np.pi))**(1/3))/(2*kb)
    #temperatura de Debye
    tau_pe = 2.2e7 * (w**2)
    #fator do tempo relacionado ao espalhamento por causa das colisões com elétrons
    tau_v = 9.16e4 * (w**2) * temp * np.exp(-theta/(3*temp))
    #fator do tempo relacionado às colisões entre fônons, os chamados processos Umklapp
    t = ( tau_pe + tau_v)**(-1)
    #tempo calculado a partir dos dois fatores mencionados
    return t 

def condutiv(omega, tempLista, v, densidade_atomica):
    '''Função para calcular a condutividade térmica, que recebe como parâmetros uma lista com os valores
    das frequências de vibração (omega), uma lista de temperaturas para as quais serão calculadas as
    condutividades, a velocidade do som no sólido e a densidade atômica.  A função utiliza a outra função 
    tau definida no módulo e retorna uma lista com as condutividades para cada valor de temperatura dado.'''
    def f(x, w, temp):
        #função que será integrada sobre x (que é calculado a partir de omega) para cálculo da condutividade
        return (tau(w, temp, v, densidade_atomica)*(x**4)*np.exp(x)/(np.exp(x)-1)**2)
    def k(omega, temp):
        '''Cálculo da condutividade por meio da criação de uma lista para x, a partir da lista de 
        frequências dada e, depois, integrando a função anterior sobre x para dada temperatura 
        passada como parâmetro utilizando o método dos trapézios repetidos.'''
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
        #cálculo da condutividade para toda a lista de temperaturas dada, gerando também uma lista de condutividades
        lista_k.append(k(omega, temp)) 
    return lista_k
