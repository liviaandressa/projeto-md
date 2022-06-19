## Dupla: Lívia Andressa da Silva Santos e Maria Aparecida da Silva Nascimento

from GerarChavePublica import gerarChavePublica
from Encriptar import encriptar
from Desencriptar import desencriptar

## Menu de apresentção de escolha ao usuário
print('''
******* Menu *******

1 - Gerar Chave Pública
2 - Encriptar 
3 - Desencriptar
4 - sair

*********************
''')

escolhaInicial = int(input('escolha a opção desejada de acordo com o menu acima: '))

#Repete a chamada das funções após ter sido feito o que se pede na opção
while escolhaInicial != 4:
    
    ## chamada da função de cada opção
    if escolhaInicial == 1:
        gerarChavePublica(escolhaInicial)

    if escolhaInicial == 2:
        encriptar(escolhaInicial)

    if escolhaInicial == 3:
        desencriptar(escolhaInicial)

    print('''
******* Menu *******

1 - Gerar Chave Pública
2 - Encriptar 
3 - Desencriptar
4 - sair

*********************
''')
    
    escolhaInicial = int(input('escolha a opção desejada de acordo com o menu acima: '))
