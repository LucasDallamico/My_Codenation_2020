from datetime import datetime
import time

# -----------------------------------
# Custos de uma ligacao
custo_fixo = 0.36
taxa_diurna = 0.09
# Limite de faixa de horario ( em seg )
diuno_to_noturno = 22 * 60 * 60
noturno_to_diuno = 6 * 60 * 60
# -----------------------------------
# entrada ( lista de dicionarios )
records = [
    {
        "source": "48-996355555",
        "destination": "48-666666666",
        "end": 1564610974,
        "start": 1564610674,
    },
    {
        "source": "41-885633788",
        "destination": "41-886383097",
        "end": 1564506121,
        "start": 1564504821,
    },
    {
        "source": "48-996383697",
        "destination": "41-886383097",
        "end": 1564630198,
        "start": 1564629838,
    },
    {
        "source": "48-999999999",
        "destination": "41-885633788",
        "end": 1564697158,
        "start": 1564696258,
    },
    {
        "source": "41-833333333",
        "destination": "41-885633788",
        "end": 1564707276,
        "start": 1564704317,
    },
    {
        "source": "41-886383097",
        "destination": "48-996384099",
        "end": 1564505621,
        "start": 1564504821,
    },
    {
        "source": "48-999999999",
        "destination": "48-996383697",
        "end": 1564505721,
        "start": 1564504821,
    },
    {
        "source": "41-885633788",
        "destination": "48-996384099",
        "end": 1564505721,
        "start": 1564504821,
    },
    {
        "source": "48-996355555",
        "destination": "48-996383697",
        "end": 1564505821,
        "start": 1564504821,
    },
    {
        "source": "48-999999999",
        "destination": "41-886383097",
        "end": 1564610750,
        "start": 1564610150,
    },
    {
        "source": "48-996383697",
        "destination": "41-885633788",
        "end": 1564505021,
        "start": 1564504821,
    },
    {
        "source": "48-996383697",
        "destination": "41-885633788",
        "end": 1564627800,
        "start": 1564626000,
    },
]
# -----------------------------------
def converte_timestamp_to_sec(timestamp):
    data_ = datetime.fromtimestamp(timestamp)
    """
    Retorna tempo em segundos das horas desse timestamp
    """
    return data_.hour * 60 * 60 + data_.minute * 60 + data_.second


# -----------------------------------
def tempo_da_chamada_sec(tempStar, tempEnd):
    """
    Retorna o tempo da chamada inicial e final em sec
    """
    temp_I = converte_timestamp_to_sec(tempStar)
    temp_F = converte_timestamp_to_sec(tempEnd)
    return temp_I, temp_F


# -----------------------------------
def preco_da_chamada(inicio_chamada, fim_chamada):
    """
    Retorna o custo da ligação
    """
    # Regra de negocio
    if (inicio_chamada >= noturno_to_diuno) and (inicio_chamada < diuno_to_noturno):
        tempo_chamada = min(
            abs(fim_chamada - inicio_chamada), abs(noturno_to_diuno - inicio_chamada)
        )
        valorChamada = custo_fixo + (tempo_chamada // 60) * taxa_diurna

    elif (inicio_chamada > diuno_to_noturno) or (inicio_chamada < noturno_to_diuno):
        tempo_chamada = min(
            abs(fim_chamada - inicio_chamada), abs(noturno_to_diuno - inicio_chamada)
        )
        valorChamada = (
            custo_fixo
            + ((abs(inicio_chamada - fim_chamada) - tempo_chamada) // 60) * taxa_diurna
        )

    valorChamada = round(valorChamada, ndigits=2)
    return valorChamada


# -----------------------------------
def junta_a_conta_dos_numeros(analise_de_dados):
    """
    Prepara a estrutura para enviar como resposta
    -> Agrupa numeros semelhantes
    -> Ordena por ordem descrecente
    """
    estrutura_limpa = []
    for aux in analise_de_dados:
        if len(estrutura_limpa) == 0:
            estrutura_limpa.append({"source": aux["source"], "total": aux["total"]})
        else:
            cont = 0
            for item in estrutura_limpa:
                if aux["source"] is item["source"]:
                    var = item["total"] + aux["total"]
                    item["total"] = round(var, ndigits=2)
                    cont = 1
                    break
            if cont == 0:
                estrutura_limpa.append({"source": aux["source"], "total": aux["total"]})

    estrutura_limpa = sorted(estrutura_limpa, key=lambda k: k["total"], reverse=True)
    return estrutura_limpa


# -----------------------------------
def classify_by_phone_number(records):
    # estrutura para armazenar as analises de dado
    analise_de_dados = []
    for i in range(0, len(records)):
        analise_evento = {}
        # armazena o numero que efetuou a ligacao
        analise_evento["source"] = records[i]["source"]
        # obter tempo de duracao da chamada
        temp_lig_start, temp_lig_end = tempo_da_chamada_sec(
            records[i]["start"], records[i]["end"]
        )
        # custo da chamada
        analise_evento["total"] = preco_da_chamada(temp_lig_start, temp_lig_end)
        # Adicionar o dicionario na lista
        analise_de_dados.append(analise_evento)

    # Agrupando o valor dos numeros de telefone repetidos
    dados_prontos = junta_a_conta_dos_numeros(analise_de_dados)
    return dados_prontos


# -----------------------------------
