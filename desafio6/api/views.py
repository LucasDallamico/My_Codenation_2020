from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

@api_view(['POST'])
def lambda_function(request):
    '''
    Função acessada através de 
        curl -X POST http://127.0.0.1:8000/lambda/ -H "Content-Type: application/json" -d 
        '{"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}'
        response {"solution":[3,3,3,3,2,2,2,5,5,12,12,4]}
    Retorno
        Um JSON com a solução
    '''
    """
    if request.method == 'GET':
        return Response({'error': 'nao eh possivel obter informacaoes'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    """
    if request.method == 'POST':
        dados_brutos = request.data.get('question')
        dados_brutos_tratados = ordena_por_mais_aparicao(dados_brutos)
        # Json para responder a requisição
        json_resposta = {
            'solution': dados_brutos_tratados,
        }
        return Response(json_resposta, status=status.HTTP_200_OK)