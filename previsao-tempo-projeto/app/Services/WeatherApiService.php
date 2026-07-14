<?php

namespace App\Services;

use Illuminate\Support\Facades\Http;

class WeatherApiService
{
    public function getWeather(string $city): array
    {
        return Http::get(
            'http://127.0.0.1:8001/weather',
            [
                'city' => $city
            ]
        )->json();
    }
}