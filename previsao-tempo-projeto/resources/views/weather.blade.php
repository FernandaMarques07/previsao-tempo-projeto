<h1> Previsão do Tempo </h1> <!-- Exibição !-->

<form>
    <input name="city"
    placeholder="Digite uma cidade">

    <button>
        Buscar
    </button>

</form>

<hr>

<h2>{{ $weather['city'] }}</h2>

<p>País: {{$weather['country'] }}</p>
<p>Temperatura: {{$weather['temperature'] }} ºC</p>
<p>Umidade: {{$weather['humidity'] }} %</p>
<p>Vento: {{$weather['wind'] }} km/h</p>