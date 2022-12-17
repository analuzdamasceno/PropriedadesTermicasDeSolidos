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
