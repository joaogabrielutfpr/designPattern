import requests
import random
import consul
import pybreaker
import time


# Circuit Breaker
breaker = pybreaker.CircuitBreaker(
    fail_max=2,
    reset_timeout=5
)




# Service Discovery
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
    url = f"http://{address}:{port}/"

    try:
        # Envolvendo só a chamada HTTP com o breaker
        @breaker
        def protected_request():
            return requests.get(url, timeout=3)

        response = protected_request()
        print(f"✅ Resposta de {service['ServiceID']}: {response.text}")

    except pybreaker.CircuitBreakerError:
        print(f"⚠️ Circuito ABERTO para {service['ServiceID']}. Ignorando tentativa.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao chamar serviço {service['ServiceID']}")


# Service Discovery

if __name__ == "__main__":
    for i in range(50):
        print(f"\n🔄 Tentativa {i+1}")
        service = discover_service()
        if service:
            call_service(service)
        time.sleep(1)

