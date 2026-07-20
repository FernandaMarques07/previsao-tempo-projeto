from app.services.weather_service import WeatherService

from app.gateways.open_meteo_gateway import OpenMeteoGateway


def get_weather_service():

    gateway = OpenMeteoGateway()

    return WeatherService(gateway)