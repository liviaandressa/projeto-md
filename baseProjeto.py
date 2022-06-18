## Dupla: Lívia Andressa da Silva Santos e Maria Aparecida da Silva Nascimento

from GerarChavePublica import gerarChavePublica
from Encriptar import encriptar
from Desencriptar import desencriptar


## Menu de apresentção de escolha ao usuário
print('''1 - Gerar Chave Pública
2 - Encriptar
3 - Desencriptar''')

escolhaInicial = int(input('escolha a opção desejada de acordo com o menu acima:'))


## chamda da função de cada opção:
if escolhaInicial == 1:
    gerarChavePublica(escolhaInicial)

if escolhaInicial == 2:
    encriptar(escolhaInicial)

if escolhaInicial == 3:
    desencriptar(escolhaInicial)
