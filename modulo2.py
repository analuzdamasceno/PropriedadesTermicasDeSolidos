import numpy as np
import matplotlib.pyplot as plt 
import warnings

warnings.filterwarnings('ignore')

#Definição das constantes
kb = 1.380649e-23
hbar = 1.05457182e-34

#criando a funcao densidade de estados de Debye
def densidade_debye(omega, v):
    return (3*(omega**2)/(2*(np.pi**2)*(v**3)))

#calculando os valores de omega para o silicio
arquivo_si = open('dadosSilicio.txt', 'r')
omega_si = []

for linha in arquivo_si: 
    omega = linha.split()[0]
    omega = omega.replace(",",'.')
    omega = float(omega)
    omega_si.append(omega)

#omega_si.remove(0)

v_si = 2200 


temperaturas = np.linspace(0.01,1000,5000)


#funcao da capacidade termica de debye
def cv_debye(omega, TempLista, v, N, densidade_atomica):
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

def cv_debye2(omega, TempLista, v, N, densidade_atomica):
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



#para o silicio


#para o GaN
#omega

arquivo_gan = open('dadosGaN.txt', 'r')
omega_gan = []

for linha in arquivo_gan: 
    omega = linha.split()[0]
    omega = omega.replace(",",'.')
    omega = float(omega)
    omega_gan.append(omega)

#omega_gan.remove(0)

v_gan = 6900


#plt.plot(temperaturas, cv_debye_si)
#plt.plot(temperaturas, cv_debye_gan)
#plt.grid()
#plt.show()



#cv_debye_ta = cv_debye(omega_ta, temperaturas, v_ta, 6.02e23, 5.6e28)
#plt.plot(temperaturas, cv_debye_ta)