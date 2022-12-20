import numpy as np

#Definição das constantes:
kb = 1.380649e-23
'''Constante de Boltzmann'''
hbar = 1.05457182e-34
'''Constante de Planck sobre 2 pi (h barra)'''


def cv_densidade_experimental(omega, densidade_estados, tempLista, d_atomica):
    '''Função para cálculo da capacidade térmica a partir de valores experimentais para a 
    densidade de estados, recebendo como parâmetros uma lista de frequências de vibração omega, 
    uma lista com os valores de densidade de estados, uma lista de temperaturas para as quais a 
    grandeza será calculada e a densidade atômica do solo, retornando uma lista com as capacidades 
    térmicas para cada temperatura.'''
    def f(w, temp,d_omega):
        '''função que será integrada para cada valor de omega e de densidade de estados correspondente,
        considerando que os dados experimentais de densidade de estados são para um metro cúbico do sólido.'''
        return (d_omega/(d_atomica/6.02e23)*np.exp((hbar*w)/(kb*temp))*((hbar*w/temp)**2))/(kb*(np.exp((hbar*w)/(kb*temp))-1)**2)
    def cv(omega, densidade_estados, temp):
        '''Função de cálculo da capacidade térmica para as listas de frequência e de densidades de estado 
        para dada temperatura a partir da integração numérica da função anterior sobre omega utilizando o 
        método dos trapézios repetidos.'''
        h = (omega[-1]-omega[0])/len(omega)
        inte = f(omega[0], temp, densidade_estados[0]) + f(omega[-1], temp, densidade_estados[-1])
        for i in range(1,len(omega)):
            inte += 2*f(omega[i], temp, densidade_estados[i])
        inte = inte*(h/2)
        return inte
    c_dados = []
    for temp in tempLista:
        #cálculo da densidade de estados para todas as temperaturas da lista dada
        c_dados.append(cv(omega, densidade_estados, temp))
    return c_dados
