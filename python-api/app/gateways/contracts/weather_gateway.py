# Define apenas a "regra" do que um gateway deve ter
from abc import ABC, abstractmethod
from app.models.weather_response import WeatherResponse

class WeatherGateway(ABC):

    @abstractmethod
    def get_weather(self, city: str) -> WeatherResponse:
        pass