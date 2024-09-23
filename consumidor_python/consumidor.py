import pika

# Conectando ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarando a exchange (deve ser a mesma utilizada pelo produtor)
exchange_name = 'agendamento_consultas'
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

# Declarando a fila (o RabbitMQ criará uma fila se ela não existir)
queue_name = 'consulta_fila'
channel.queue_declare(queue=queue_name, durable=True)

# Ligando a fila à exchange com a chave de roteamento usada pelo produtor
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='#')

print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')

# Função chamada sempre que uma mensagem chega
def callback(ch, method, properties, body):
    print(f" [x] Recebido: {body.decode()}")

# Consumindo as mensagens
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Iniciando o loop de espera por mensagens
channel.start_consuming()
