Instalações:
https://developer.hashicorp.com/consul/install
https://www.erlang.org/downloads
https://www.rabbitmq.com/docs/install-windows

Pacotes
pip install flask requests python-consul
pip install pybreaker
pip install pika


Em um prompt:
consul agent -dev
acessar: http://localhost:8500/ui/dc1/services

Para registrar os serviços e instancia-los, ( um prompt para cada serviço ) ex:
consul services register consul_config/service_a.json
services/service_a.py

Para verificar o funcionamento do Service Discovery:
clientSD.py

Para verificar o funcionamento do  Circuit Breaker:
clientCB.py

Para verificar o funcionamento do  Event-Driven Architecture:
Instanciar  service_EDA.py
Abrir o worker em um prompt separado ( vai ficar ouvindo )
rodar o clientSD.py para verificar as chamadas de EDA e acompanhar no worker o ping 


 
