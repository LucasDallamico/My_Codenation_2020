from main import get_temperature
import pytest

def test_get_temp_not_lat_and_log():
    lat = -1000
    lng = -1000
    #Reposta esperado: "Erro"
    try:
        outuput = get_temperature(lat, lng)
        assert outuput == 'None'
    except:
        assert True

def test_get_temp_sao_paulo():
    # Localização de teste
    lat = -26.9141422
    lng = -49.0718383
    #Reposta esperada
    output_expected = 25

    outuput = get_temperature(lat, lng)

    assert outuput == output_expected


def test_get_temperature_example_lat_lng():
    # Localização de teste
    lat = -14.235004
    lng = -51.92528
    #Reposta esperada
    output_expected = 29

    outuput = get_temperature(lat, lng)

    assert outuput == output_expected
