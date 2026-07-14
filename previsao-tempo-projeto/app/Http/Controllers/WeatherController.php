<?php

namespace App\Http\Controllers;

use App\Services\WeatherApiService;

use Illuminate\Http\Request;

class WeatherController extends Controller
{
    public function index(
        Request $request,
        WeatherApiService $service
        )
    {
        $city = $request->input(
            'city'
        );

        return view('weather', [
            'weather' => $service->getWeather($city)
            ]
        );
    }
}
