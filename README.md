# Propriedades térmicas de sólidos

  O projeto desenvolvido é o trabalho final da disciplina Introdução à Computação em Física, ofertada no segundo semestre de 2022 pelo Departamento de Física da UFMG. O projeto foi proposto pelo professor doutor Walber Hugo de Brito, realizado de modo a aplicar os conhecimentos desenvolvidos na disciplina.

  Teve-se como objetivo desenvolver módulos para calcular a capacidade e a condutividade térmica de sólidos e aplicar as funções desenvolivdas no cálculo dessas propriedades para alguns semicondutores.

  O trabalho encontra-se dividido em quatro módulos de contas:
  
**modulo1.py**
  Neste módulo há uma função que calcula a capacidade térmica de um sólido a partir do modelo de Einstein, recebendo como parâmetros uma lista com as frequências de oscilação dos fônons do sólido, o número de átomos da amostra e uma lista com as temperaturas para as quais deve-se realizar o cálculo. O método numérico utilizado é a derivação numérica por diferença central.
  A equação para a capacidade térmica neste modelo é:
  
  <h1 align="center"> $U = \dfrac{3N\hbar\omega_{0}}{e^{\hbar\omega_{0}/k_{B}T}-1}$ </h1>
  <h1 align="center"> $C = \dfrac{\del U}{\del T}$ </h1>
  
**modulo2.py**
  Aqui, há uma função que calcula a capacidade térmica de um sólido com base no modelo de Debye. Ela recebe como parâmetros uma lista com as frequências de vibração dos fônons, a velocidade do som no sólido, o número de átomos da amostra, a densidade atômica do sólido e a lista de temperaturas para as quais a capacidade térmica será calculada. Os cálculos são realizados utilizando o método de integração numérica dos trapézios repetidos.
    As equações deste modelo são:
<h1 align="center"> $$ </h1>
