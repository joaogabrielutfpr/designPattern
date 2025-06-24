import requests
import random
import consul

def discover_service():
    c = consul.Consul()
    index, services = c.catalog.service('microservice')
    if not services:
        print("Nenhum serviço encontrado.")
        return None
    return random.choice(services)

def call_service(service):
    address = service['ServiceAddress']
    port = service['ServicePort']
    try:
        response = requests.get(f"http://{address}:{port}/")
        print(f"Resposta de {service['ServiceID']}: {response.text}")
    except Exception as e:
        print(f"Erro ao chamar serviço: {e}")

if __name__ == "__main__":
    for _ in range(10):
        service = discover_service()
        if service:
            call_service(service)
