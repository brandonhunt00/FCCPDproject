# FCCPD Project - Message Queue System with RabbitMQ

## Project Overview

This project is a messaging system utilizing RabbitMQ, composed of three main components:

1. *Producer (Java)*: Responsible for generating medical consultation requests.
2. *Consumer (Python)*: Filters and receives messages based on chosen medical specialties.
3. *Audit Backend (Python)*: Receives and logs all messages for auditing purposes.

The system uses a *Topic Exchange* to distribute messages between consumers and backend audit. This allows consumers to filter messages based on specific routing keys, making the system flexible and efficient.

## Requirements

- *Java* for the producer (Produtor.java)
- *Python 3* with pika library for the consumers (consumer.py and backend_audit.py)
- *RabbitMQ* running locally

### Setting Up

1. *Install RabbitMQ* on your system. Make sure it is running:
   - For Windows: Start RabbitMQ from the command line using rabbitmq-server.bat.
   - For macOS: Use brew services start rabbitmq.

2. *Install Dependencies*:
   - Python library: Install pika using:
     sh
     pip install pika
     
   - Java dependencies for the producer: The producer requires RabbitMQ's Java Client. This is managed via Maven.

3. *Configure RabbitMQ*:
   - Make sure the exchange agendamento_consultas is created in RabbitMQ as *durable* and of type *topic*.
   - Bind queues to the exchange with appropriate routing keys:
     - For each medical specialty (e.g., consulta_fila_cardiologista), bind with nova_consulta.<specialty>.
     - Bind the audit queue (auditoria_fila) with the routing key # to receive all messages.

### Running the System

1. *Start the Producer*:
   - Navigate to the produtor_java directory.
   - Run the producer using Maven:
     sh
     mvn exec:java -Dexec.mainClass="com.consultamedica.Produtor"
     

2. *Start Consumers*:
   - For the consumer that filters messages based on a specialty, run:
     sh
     python3 consumidor.py
     
   - Choose the desired specialty from the menu to start listening for messages of that type.
   - To return to the menu, use ctrl+c.

3. *Start the Audit Backend*:
   - To monitor all messages, run the backend audit consumer:
     sh
     python3 backend_auditoria.py
     

### Usage Flow

- *Producer* sends messages with a specific routing key (e.g., nova_consulta.cardiologista). The messages are routed to queues bound with matching keys.
- *Consumer* subscribes to a specific queue and receives messages as they are published.
- *Audit Backend* receives all messages for logging purposes.

### Important Notes

- Ensure RabbitMQ server is always running when executing the producer or consumers.
- Messages are persistent, meaning they will be saved in queues even if consumers are not connected at the time of message delivery.

### Project Structure

- produtor_java/ - Contains Produtor.java (Java code for producing messages).
- consumidor_python/ - Contains consumer.py (Python consumer for receiving messages).
- backend_auditoria/ - Contains backend_auditoria.py (Python backend audit for receiving all messages).

### License

This project is licensed under the MIT License - see the LICENSE file for details.
