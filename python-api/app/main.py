from fastapi import FastAPI, HTTPException
from services.weather_service import WeatherService

app = FastAPI()

service = WeatherService()

@app.get("/weather") # @ -> decorador
def weather(city: str): # define a função 
    try:
        return service.get_weather(city)
    
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
