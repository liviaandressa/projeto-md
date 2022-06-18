import math

e = 0

def gerarChavePublica(escolhaInicial):

    print("Digite dois números primos:")
    primeiroPrimo = int(input("Primeiro número primo:"))
    segundoPrimo = int(input("Segundo número primo:"))

    ## Agora, vamos declarar duas funções para verificar se os números dados são primos ou não:
    def verificaPrimo1(primeiroPrimo):

        multiplos = 0
       
        ## Aqui vamos utilizar uma estrutura de repetição para verificar se os números dados são primos:
        ## Se não são primos, precisaremos pedi-los de novo!
    
        for contador in range(2, primeiroPrimo):
            if (primeiroPrimo % contador == 0):
                multiplos += 1

        if multiplos != 0:
            print("O primeiro número digitado não é primo, por favor informe outro número:")
            primeiroPrimo = int(input())

            return verificaPrimo1(primeiroPrimo)


    def verificaPrimo2(segundoPrimo):   
        multiplos2 = 0
    
        for cont in range(2,segundoPrimo):
                if (segundoPrimo % cont == 0):
                    multiplos2 += 1

        if multiplos2 != 0:
            print("O segundo número digitado não é primo, por favor escolha outro:")
            segundoPrimo = int(input())

            return verificaPrimo2(segundoPrimo)

    ## Aqui chamamos as funções para que elas possam funcionar:           
    verificaPrimo1(primeiroPrimo)
    verificaPrimo2(segundoPrimo)
    
    ## Agora temos que receber o número "e":       
    print("Agora escolha um número relativamente primo à (Primeiro Primo − 1) * (segundo Primo − 1):")

    global e
    e += int(input())

    N = (primeiroPrimo - 1) * (segundoPrimo - 1)

    aux_e = e
    aux_N = N
    if (e > N):
        aux_e = N
        aux_N = e 
    
    ## Agora vamos verificar se o número "e" e o valor da variável "N" são primos entre si:

    ## Aqui criamos uma função para descobrir o MDC de "e" e "N":
    def mdc(a, segundoPrimo, d, r):
        if (r == 0):
            return d
        else:
            a = d
            d = r
            segundoPrimo = math.floor(a/d)
            r = a % d 
            return mdc(a, segundoPrimo, d, r)


    mdc2 = mdc(aux_N, math.floor(aux_N/aux_e), aux_e, aux_N%aux_e)    

       ## Se não é 1, temos que pedir outro valor. 
       ## Caso o valor da função seja 1, significa que os números são coprimos!

    while (mdc2 != 1):

        print("O número escolhido não é coprimo à expressão (Primeiro Primo − 1) * (segundo Primo − 1). Por favor, tente novamente!")
        e = int(input("Digite outro valor: "))
        aux_e = e

        ## Aqui chamamos a função mdc para que o novo valor seja computado
        mdc2 = mdc(aux_N, math.floor(aux_N/aux_e), aux_e, aux_N%aux_e)


    ## Este comando cria um arquivo e permite que adicionemos algo nele:    
    arquivo = open("arquivo.txt", "w")

    ## Aqui transformamos as variaveis em string para que possam ser escritas juntas:
    v1 = str(e)
    v2 = str(N)
            
    ## Aqui eu criei a variável "Chave Pública" que vai ser composta pelos números "e" e "N":       
    chavePublica = v1 + v2
            
    ## Aqui nós escrevemos o valor da chavePublica no arquivo:       
    arquivo.writelines(chavePublica)

    ## Por fim, avisamos ao usuário qual é sua Chave Pública:
    print("A sua chave pública é: ", chavePublica)

      
