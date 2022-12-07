#função para leitura e extração dos dados desejados (as frequências de vibração e as densidades de estado)
def ler_dados(lista_omega, lista_densidade, arquivo):
    for linha in arquivo:
        omega = linha.split()[0]
        densidade_estados = linha.split()[1]
        omega = omega.replace(",",".")
        densidade_estados = densidade_estados.replace(",",".")
        omega = float(omega)
        densidade_estados = float(densidade_estados)
        lista_omega.append(omega)
        lista_densidade.append(densidade_estados)

#para o Silício
arquivo_si = open('dadosSilicio.txt', 'r')
omega_si = []
densidade_estados_si = []
ler_dados(omega_si, densidade_estados_si, arquivo_si)

#Para o GaN
arquivo_gan = open('dadosGaN.txt')
omega_gan = []
densidade_estados_gan = []
ler_dados(omega_gan, densidade_estados_gan, arquivo_gan)

#Para o ZnO (rocksalt)
arquivo_zno_rocksalt = open("dadosZnO_rocksalt.txt")
omega_zno_rs = []
densidade_estados_zno_rs = []
ler_dados(omega_zno_rs, densidade_estados_zno_rs, arquivo_zno_rocksalt)

