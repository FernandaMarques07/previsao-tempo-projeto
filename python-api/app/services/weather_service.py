import requests # permite acessar sites e APIs (fazer requests)

from app.cache.memory_cache import MemoryCache
from app.config import CACHE_TTL

class WeatherService:
    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search" # coordenadas
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast" # buscar o clima 
    # link sobre a api: https://open-meteo.com/en/docs

    cache = MemoryCache()

    def get_weather(self, city): # permite usar as funções internas da classe/ espera receber

        key = city.lower().strip()

        cached = self.cache.get(key)

        if cached:
            print("Resposta veio do CACHE")
            return cached
        
        print("Resposta veio da API")

        # 1. Busca as coordenadas da cidade
        geo = requests.get(
            self.GEO_URL, # permite com que o programa encontre var globais
            params={
                "name": city,
                "count": 1 # devolve apenas 1 resultado (a cidade digitada)
            },
            timeout=5 # evita travamento
        )

        geo.raise_for_status() # verificar status

        data = geo.json() # resposta 

        if "results" not in data:
            raise Exception("Cidade não encontrada.") # o raise para o código quando não encontra o resultado em data
        
        place = data["results"][0] # guarda o resultado 1, isso é uma array

        latitude = place["latitude"]
        longitude = place["longitude"]

        # 2. Busca o clima usando as coordenadas 
        weather = requests.get(
            self.WEATHER_URL, # var global
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m" # dados atuais
            },
            timeout=5 # evita travamentos
        )

        weather.raise_for_status()

        current = weather.json()["current"]

        result = {
            "city": place["name"],
            "country": place["country"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"]
        }
    
        self.cache.set(
            key,
            result,
            CACHE_TTL
        )

        return result