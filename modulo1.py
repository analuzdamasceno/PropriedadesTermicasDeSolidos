import numpy as np

#Definição das constantes: 
kb = 1.380649e-23 
'''Constante de Boltzmann'''
hbar = 1.05457182e-34
'''Constante de Planck sobre 2 pi (h barra)'''

def cv_einstein(omega,N,intervaloTemp):
    ''' Função que retorna uma lista com as capacidades térmicas calculadas por meio do modelo de Einstein
    para cada temperatura dada, recebendo como parâmetros um valor de frequência de vibração (é recomendável
    que seja a média entre todas as frequências do sólido), um número N de átomos  e uma lista com o intervalo
    de temperatura para o qual serão calculadas as capacidades térmicas.'''
    def u_einstein(N,omega,T):
        '''Função que calcula a energia dos fônons em um cristal para o modelo de Einstein a partir do número
        N de átomos, da frequência e da temperatura'''
        return ((3*N*hbar*omega))/(np.exp(hbar*omega/(kb*T))-1)
    c_einstein = []
    h = 0.0001
    for temp in intervaloTemp:
        cv = (u_einstein(N, omega, (temp)+h) - u_einstein(N, omega, (temp)-h))/(2*h)
        c_einstein.append(cv)
        '''Cáculo da capacidade térmica por derivação numérica usando o método da diferença central'''
    return c_einstein
