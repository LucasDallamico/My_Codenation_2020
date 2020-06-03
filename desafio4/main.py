import jwt

senha_da_criptografica = "acelera"

def create_token(data, secret):
    '''
    Cria um token criptogrado
    Parametros:
        data (json): arquivo com o conteúdo que será criptografado
        secret (str): a senha que será usado para quebrar a criptografia
    Return:
        token: sequência criptografada contendo dados de entrada

    '''
    # Função que ira pegar o json,str,codificação e transforma em jwt
    token_criado = jwt.encode(data, secret, algorithm='HS256')
    return token_criado

def verify_signature(token):
    try:
        #Quebrar o token em um json
        json_token = jwt.decode(token,senha_da_criptografica)
        return json_token
    except:
        return {"error": 2}

"""
# -------------------------------
def meu_test():
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'
    token_output = create_token({"language": "Python"}, "acelera")
    assert create_token({"language": "Python"}, "acelera") == token

if __name__ == "__main__":
    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'
    #meu_test()
    verify_signature(token)
"""