
entrada = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]
saida_esperada = [3 ,3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]

import statistics

def ordena_por_mais_aparicao(lista_desorganizada):
    lista_retorno = []
    while lista_desorganizada:
        # Verifica o elementos mais repetido
        mais_repetido = statistics.mode(lista_desorganizada)
        # Obtem a quantidade de vezes que ele repete
        qnt_mais_repetido = lista_desorganizada.count(mais_repetido)
        # Adiciona em outra lista as repetições de elemento
        for i in range(0,qnt_mais_repetido,1):
            lista_retorno.append(mais_repetido)
            # Remove da antiga lista os elementos
            lista_desorganizada.remove(mais_repetido)

    return lista_retorno


saida_recebida = ordena_por_mais_aparicao(entrada)
print(saida_recebida)
print(saida_esperada)
assert saida_esperada == saida_recebida







