# Propriedades térmicas de sólidos

  O projeto desenvolvido é o trabalho final da disciplina Introdução à Computação em Física, ofertada no segundo semestre de 2022 pelo Departamento de Física da UFMG. O projeto foi proposto pelo professor doutor Walber Hugo de Brito, realizado de modo a aplicar os conhecimentos desenvolvidos na disciplina.

  Teve-se como objetivo desenvolver módulos para calcular a capacidade e a condutividade térmica de sólidos e aplicar as funções desenvolivdas no cálculo dessas propriedades para alguns semicondutores.

  O trabalho encontra-se dividido em quatro módulos de contas e utiliza as bibliotecas Numpy e Matplotlib.pyplot do Python:
  
**modulo1.py**

  Neste módulo há uma função que calcula a capacidade térmica de um sólido a partir do modelo de Einstein, recebendo como parâmetros uma lista com as frequências de oscilação dos fônons do sólido, o número de átomos da amostra e uma lista com as temperaturas para as quais deve-se realizar o cálculo. O método numérico utilizado é a derivação numérica por diferença central.
  
  A equação para a capacidade térmica neste modelo é:
  
  <h3 align="center"> $U = \dfrac{3N\hbar\omega_{0}}{e^{\hbar\omega_{0}/k_{B}T}-1}$ </h3>
  <h3 align="center"> $C = \dfrac{\partial U}{\partial T}$ </h3>
  
**modulo2.py**

  Aqui, há uma função que calcula a capacidade térmica de um sólido com base no modelo de Debye. Ela recebe como parâmetros uma lista com as frequências de vibração dos fônons, a velocidade do som no sólido, o número de átomos da amostra, a densidade atômica do sólido e a lista de temperaturas para as quais a capacidade térmica será calculada. Os cálculos são realizados utilizando o método de integração numérica dos trapézios repetidos.
    As equações deste modelo são:
    
  <h3 align="center"> $C = 3Nk_{B}(\dfrac{T}{\theta})^{3}\int_{x_{0}}^{x_{máx}}\dfrac{x^{4}e^{x}}{(e^{x}-1)^{2}}dx$ </h3>

  Em que

  <h3 align="center"> $x = \dfrac{\hbar\omega}{k_{B}T}$ </h3>
  <h3 align="center"> $\theta = \dfrac{\hbar v_{som}}{k_{B}}(6\pi^{2}\rho_{atom})^{1/3}$ </h3>
  

**modulo3.py**

  Neste módulo são utilizados dados experimentais de densidades de estado do sólido, $D(\omega)$, para cálculo da capacidade térmica: a função recebe a lista de frequências de oscilação dos fônons, a lista das densidades de estados correspondentes a cada frequência, a densidade atômica e a lista de temperaturas. A função foi criada com base nos dados que serão utilizados: considerando que a densidade de estados é dada para um metro cúbico do sólido. A equação base foi:
    
  <h3 align="center"> $C = \int_{\omega_{0}}^{\omega_{máx}}D(\omega)\dfrac{e^{\hbar\omega/k_{B}T}}{(e^{\hbar\omega/k_{B}T}-1)^{2}}\dfrac{\hbar\omega}{T}d\omega$ </h3>

**modulo4.py**

  Aqui cria-se duas funções: uma para cálculo do $\tau$, tempo médio entre as colisões dos fônons, que recebe como parâmetros uma fequência de oscilação $\omega$, a temperatura, a velocidade do som no sólido e a densidade atômica; e uma segunda função de cálculo da condutividade térmica, que recebe como parâmetros uma lista das frequências de oscilação dos fônons, a velocidade do som no sólido, a densidade atômica e uma lista de temperaturas, e esta segunda função utiliza a primeira.
  As equações de referência são baseadas em um modelo simplicado da Teoria de Callaway:
  
  <h3 align="center"> $\tau = (\tau_{pe}^{-1} + \tau_{v}^{-1})^{-1}$ </h3>
  <h3 align="center"> $\tau_{pe}^{-1} = A\omega^{2}$ </h3>
  <h3 align="center"> $\tau_{v}^{-1} = D\omega^{2}Te^{-(\theta/3T)}$ </h3>
  <h3 align="center"> $k = \dfrac{k_{B}^{4}T^{3}}{2\pi^{2}v_{som}\hbar^{3}}\int_{0}^{\theta/T}\tau\dfrac{x^{4}e^{x}}{(e^{x}-1)^{2}}dx$ </h3>
  
  Em que $x$ é o mesmo citado anteriormente e $A$ e $D$ são constantes experimentais. No trabalho, como trata-se de um modelo simplificado, os valores utilizados para tais constantes foram: $A=2.2 * 10^{7}$ e $D=9.16 * 10^{4}$, extraídos do artigo "Thermal conductivity of the Kondo semiconductor
CeRu4Sn6", publicado no Journal of Physics.


Além destes quatro módulos, há também o módulo **extracaoDados.py**, em que define-se uma função para a leitura dos dados das frequências de oscilação e das densidades de estados, considerando arquivos de duas colunas, em que cada uma responde à respectiva grandeza.

Por meio dos módulos desenvolvidos, foi possível aplicá-los a diferentes sólidos, cujos arquivos contendo os dados estão no diretório e foram extraídos de [lampx.tugraz.at/~hadley/ss1/](http://lampx.tugraz.at/~hadley/ss1/). 

Os resultados foram dispostos em aqruivos de extensão .ipynb para que fosse possível a visualização dos gráficos gerados no próprio arquivo. Foram obtidos resultados para o silício, para o nitreto de gálio, e para duas disposições estruturais diferentes do óxido de zinco: da forma rocksalt e da forma zincblende. Há também um arquivo que compara os resultados das condutividades térmicas de tais sólidos em um mesmo gráfico.

No diretório estão também a pasta de nome "Documentação", na qual estão contidos os html com as documentações dos módulos descritos anteriormente, e a pasta "Metodologia e Análise", em que está um arquivo pdf com uma breve análise dos sólidos utilizados e dos resultados obtidos e o arquivo do "Software Design Document", que propõe a ideia original por trás do projeto e contém a metodologia teórica utilizada de maneira mais detalhada. 
