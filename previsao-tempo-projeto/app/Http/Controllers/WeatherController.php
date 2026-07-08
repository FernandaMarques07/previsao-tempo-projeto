<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class WeatherController extends Controller
{
    public function index(Request $request)
    {
        $city = $request->input('city', 'São Paulo');

        $response = Http::get(
            'http://127.0.0.1:5000/weather',
            [
                'city' => $city
            ]
        );

        return view('weather', [
            'weather' => $response->json()
        ]);
    }
}
