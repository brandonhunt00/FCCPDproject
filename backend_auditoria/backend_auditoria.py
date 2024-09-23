import pika

# Nome da exchange que você está usando
EXCHANGE_NAME = 'agendamento_consultas'

def callback(ch, method, properties, body):
    print(f"[AUDITORIA] Mensagem recebida: {body.decode('utf-8')}")

def main():
    # Configurar conexão com o RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar a mesma exchange que o produtor
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')

    # Criar uma fila exclusiva para o backend de auditoria
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Binding com chave '#' para receber todas as mensagens
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name, routing_key='#')

    print(" [*] Aguardando mensagens para auditoria. Pressione CTRL+C para sair.")

    # Consumir mensagens
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == "__main__":
    main()
