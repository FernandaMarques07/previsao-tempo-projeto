# Busca os dados na internet usando a API Open-Meteo
import requests

from app.gateways.contracts.weather_gateway import WeatherGateway

from app.models.weather_response import WeatherResponse

from app.exceptions.city_not_found import CityNotFoundException

from app.exceptions.external_api import ExternalApiException

class OpenMeteoGateway(WeatherGateway):
    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, city: str) -> WeatherResponse:
        try:
            geo = requests.get(
                self.GEO_URL,
                params={"name": city, "count": 1}
            )
            geo.raise_for_status()
        except requests.RequestException:
            raise ExternalApiException()

        data = geo.json()

        if "results" not in data:
            raise CityNotFoundException(city)

        place = data["results"][0]

        try:
            weather = requests.get(
                self.WEATHER_URL,
                params={
                    "latitude": place["latitude"],
                    "longitude": place["longitude"],
                    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
                }
            )
            weather.raise_for_status()
        except requests.RequestException:
            raise ExternalApiException()

        current = weather.json()["current"]

        return WeatherResponse(
            city=place["name"],
            country=place["country"],
            temperature=current["temperature_2m"],
            humidity=current["relative_humidity_2m"],
            wind=current["wind_speed_10m"]
        )