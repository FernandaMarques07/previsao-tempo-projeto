import pytest # importa a biblioteca para testes de exceções e configurar o mesmo teste com dados diferentes
from app.services.weather_service import WeatherService
from tests.fakes.fake_gateway import FakeGateway
from app.exceptions.city_not_found import CityNotFoundException

def test_should_return_weather_data():
    gateway = FakeGateway()
    service = WeatherService(gateway=gateway)

    response = service.get_weather("São Paulo")

    assert response.city == "São Paulo"
    assert response.country == "Brazil"

def test_should_use_cache_on_second_call():
    gateway = FakeGateway()
    service = WeatherService(gateway=gateway)

    # 1ª busca no FakeGateway 
    service.get_weather("São Paulo") # calls -> 1
    # 2ª busca, que pega do MemoryCache
    service.get_weather("São Paulo") # deve manter calls -> 1, pois não retorna da 'api'/gateway

    assert gateway.calls == 1 # assert (garanta) que calls == 1

def test_should_raise_city_not_found_exception():
    gateway = FakeGateway()
    service = WeatherService(gateway=gateway)

    # Monitore o bloco abaixo (with) e garanta (pytest) que ele lance esta exceção (raises)
    with pytest.raises(CityNotFoundException):
        service.get_weather("Inexistente")