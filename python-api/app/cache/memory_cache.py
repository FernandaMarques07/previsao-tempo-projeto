from time import time # biblioteca nativa - horário exato

class MemoryCache:
    def __init__(self): # construtor da classe. 
        # Dunder (Double Underline) indica que será executado automaticamente
        # inicializa/cria o objeto
        self.storage = {}
    def get(self, key): # recebe a chave de busca (key)

        item = self.storage.get(key) # Busca a chave no dicionário - storage

        if not item:
            return None # Se não tiver, interrompa e retorne nenhum
        
        if item["expires"] < time():

            del self.storage[key]
            return None
        return item["value"]
    def set(self, key, value, ttl=600): # time to live => 600 segundos 
        self.storage[key] = {
            "value": value,
            "expires": time() + ttl
        }