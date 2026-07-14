<?php

namespace App\Http\Controllers; # Onde fica essa classe -> dentro da pasta app/http/controllers

use App\Services\WeatherApiService; # import do serviço da API 

use Illuminate\Http\Request; # classe Request nativa do Laravel
# lida com os dados enviados pelo usuário (como parâmetros de URL, formulários, etc.).

class WeatherController extends Controller # nova classe WeatherController usa/herda as funcionalidades do Controller base do Laravel.
{
    public function index( # função pública indez
        Request $request,
        WeatherApiService $service # dependencias request e service
        )
    {
        $city = $request->input( # parâmetro city (input) guardado em $city
            'city'
        );

        return view('weather', [ # envia a cidade e retorna as informações do serviço WeatherApiService
            'weather' => $service->getWeather($city)
            ]
        );
    }
}
