# -------------------------------------
def descriptador(num_casa,str_crip):
    # transformei em lista para facilitar o trabalho com caracteres separados
    texto = list(str_crip)
    c = 1
    for i in range(0,len(texto)):
        c = ord(texto[i])
        if ( c >= 65 and c <= 90 ) or ( c >=97 and c <= 122):
            c = c - num_casa
            if (c < 65 and (c+num_casa) <= 90 ) or (c < 97 and  (c + num_casa) <= 122 ):
                c = c + 26
        texto[i] = chr(c)
    
    #converter lista para string
    texto = ''.join(texto)
    #print(texto)
    return texto
    
# -------------------------------------
def resumo_descriptador(entrada, encoding='utf-8'):
    return sha1(entrada.encode(encoding)).hexdigest()

# -------------------------------------
import json
import requests
import pickle
from hashlib import sha1

# -------------------------------------
# Urls de interação
url_request = ("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?"
                "token=b684822732ff0a2ae7cf214e4c1babe4a00386a8")
url_send = ("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?"
            "token=b684822732ff0a2ae7cf214e4c1babe4a00386a8")

#obter a estrutura json do servidor
bruto_json = requests.get(url_request)

# verificação se a requisição funcionou
if bruto_json.status_code == 200:
    #salva em modo dicionário
    dic_dados = json.loads(bruto_json.content)

#Obtendo informações do dicionário
num_c = dic_dados["numero_casas"] # obter o numero de casas para somar na letra
mns_codificada = dic_dados["cifrado"] # obter a mensagem criptografada do dicionário

# Alterando os dados do dicionário
msn_decodifica = descriptador(num_c,mns_codificada)
msn_resumo_dec = resumo_descriptador(msn_decodifica)
dic_dados["decifrado"] = msn_decodifica
dic_dados["resumo_criptografico"] = msn_resumo_dec

#transformar o dicionário em json e escrever no arquivo
with open("answer.json", "w") as arq:
    json.dump(dic_dados,arq,indent=4,sort_keys=False)

#Envia para o arquivo para o servidor
files = {
    'answer': open('answer.json', 'r')
}

retorno = requests.post(url_send, files = files)
print(retorno.status_code)
print(retorno.text)
