<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;  # Importa o HTTP Client do Laravel

class WeatherApiService # essa classe é chamada pelo WeatherController
{
    public function getWeather(string $city): array # método público getWeather;  # exige receber um parâmetro chamado $city (string)
    { # : array -> indica que será retornado um array
        return Http::get(
            'http://127.0.0.1:8001/weather', # primeiro parâmetro -> API rodando
            [
                'city' => $city # segundo parâmetro -> string city
            ]
        )->json(); # resposta da API transformada em array associativo do PHP.
    }
}