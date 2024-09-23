# FCCPDproject
**Sistema de Agendamento Médico com RabbitMQ**

**Descrição do Projeto**
Este projeto implementa um sistema de agendamento de consultas médicas utilizando RabbitMQ para o envio e recebimento de mensagens. O sistema é composto por três componentes principais:

**Produtor de Mensagens (Java):** Responsável por simular médicos agendando consultas.

**Consumidor de Mensagens (Python):** Representa pacientes que recebem as informações sobre suas consultas agendadas.

**Backend de Auditoria:** Um componente adicional que registra todas as mensagens enviadas para monitoramento e auditoria. O projeto segue uma arquitetura orientada a mensagens, com comunicação assíncrona entre os componentes, utilizando RabbitMQ como broker de mensagens.

**Estrutura do Projeto**
produtor/ - Contém o código em Java responsável pelo envio de mensagens.
consumidor/ - Contém o código em Python responsável pelo recebimento de mensagens.
auditoria/ - Backend de auditoria que coleta todas as mensagens enviadas.

**Requisitos**
Java (versão 11 ou superior)
Python (versão 3.8 ou superior)
RabbitMQ instalado e em execução localmente ou em um servidor acessível.
Bibliotecas utilizadas:
Java: amqp-client
Python: pika

**Instalação e Execução**
**Configurando RabbitMQ**
Certifique-se de que o RabbitMQ está em execução. Você pode iniciar o RabbitMQ com o seguinte comando:

rabbitmq-server
O sistema utiliza um exchange do tipo fanout para garantir que várias instâncias de consumidores recebam as mesmas mensagens.

Produtor (Java)
Navegue até o diretório produtor/.

Compile o código Java:
javac -cp .:amqp-client-5.13.0.jar Produtor.java

Execute o produtor:
java -cp .:amqp-client-5.13.0.jar Produtor
O produtor permite parametrizar os dados da consulta médica que será agendada, como nome do paciente e data/hora da consulta.

Consumidor (Python)
Navegue até o diretório consumidor/.

Instale as dependências:
pip install pika

Execute o consumidor:
python consumidor.py

O consumidor receberá as mensagens enviadas pelo produtor e exibirá as informações da consulta agendada.

Backend de Auditoria
Navegue até o diretório auditoria/.

Execute o backend de auditoria:
python auditoria.py

O backend exibirá todas as mensagens enviadas pelo produtor, registrando as consultas agendadas para fins de auditoria.

Exemplos de Execução
**Cenário 1:** Um produtor e mais de um consumidor
Execute o produtor e duas instâncias do consumidor. Ambos os consumidores receberão as mesmas mensagens enviadas pelo produtor.

**Cenário 2:** Mais de um produtor e mais de um consumidor
Execute múltiplos produtores e consumidores. Todos os consumidores continuarão a receber as mensagens de todos os produtores, garantindo que o sistema seja escalável e distribua as mensagens corretamente.

**Composição das Mensagens**

As mensagens enviadas pelos produtores têm o seguinte formato:
[dd/MM/yyyy - HH:mm] Médico: Nome_Médico -> Paciente: Nome_Paciente | Data: dd/MM/yyyy HH:mm

**Referências:**
RabbitMQ Documentation
Biblioteca pika para Python: Pika Documentation
Biblioteca amqp-client para Java: Java Client for RabbitMQ
