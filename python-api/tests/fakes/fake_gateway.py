# fornecedor para testes unitários
from app.gateways.contracts.weather_gateway import WeatherGateway
from app.models.weather_response import WeatherResponse
from app.exceptions.city_not_found import CityNotFoundException

class FakeGateway(WeatherGateway):

    def __init__(self):
        self.calls = 0

    def get_weather(self, city: str) -> WeatherResponse:
        self.calls += 1 # Toda vez que é chamado, soma +1 no contador

        if not city or city == "Inexistente":
            raise CityNotFoundException(city)
        # Se a cidade for vazia ou "Inexistente", ele simula um erro imediatamente

        # Para qualquer outra cidade devolve a resposta pronta:
        return WeatherResponse(
            city=city,
            country="Brazil",
            temperature=25.0,
            humidity=60,
            wind=5.0
        )