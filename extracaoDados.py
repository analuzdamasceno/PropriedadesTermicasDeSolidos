def ler_dados(lista_omega, lista_densidade, arquivo):
    '''Função para extração e tretamento dos dados desejados, que recebe uma lista em
    que serão inseridas as frequências de vibração dos fônons, uma lista para inserir as 
    densidades de estados e um arquivo do qual serão lidos os dados. É considerado que o
    arquivo seja da seguinte forma: na primeira coluna as frequências de vibração e na
    segunda as densidades de estado correspondentes.'''
    for linha in arquivo:
        omega = linha.split()[0]
        densidade_estados = linha.split()[1]
        omega = omega.replace(",",".")
        densidade_estados = densidade_estados.replace(",",".")
        omega = float(omega)
        densidade_estados = float(densidade_estados)
        lista_omega.append(omega)
        lista_densidade.append(densidade_estados)