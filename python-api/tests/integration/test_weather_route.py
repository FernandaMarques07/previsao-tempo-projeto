from fastapi.testclient import TestClient # importa um simulador de requisições HTTP do FastAPI para testar rotas direto pelo código
from app.main import app # importa toda a API

# Cria o cliente de testes que simula requisições para a API
client = TestClient(app)

def test_get_weather_route_success():
    # Faz uma requisição GET simulada para a rota
    response = client.get("/weather?city=London")

    # Valida que o código HTTP retornado foi 200 OK
    assert response.status_code == 200
    # o assert (afirma/garante) lê a condição e se True (ignora e continua) se False (trava e dispara o erro de teste AssertionError) 

    # Valida se a chave "city" está no JSON retornado

    data = response.json() # data é a resposta da API convertida em dicionário
    assert "city" in data # garanta que exista a chave city em data

def test_get_weather_route_not_found():
    # Busca uma cidade inexistente
    response = client.get("/weather?city=CidadeQueNaoExiste12345")

    # Verifica se API respondeu com 404
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "CITY_NOT_FOUND"