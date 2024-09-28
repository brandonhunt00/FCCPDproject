import pika

EXCHANGE_NAME = 'agendamento_consultas'

def main():
    # Conectar ao RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar a exchange como 'durable=True' para que seja compatível com a configuração no produtor
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic', durable=True)

    # Declarar a fila de auditoria
    queue_name = 'auditoria_fila'
    channel.queue_declare(queue=queue_name, durable=True)

    # Bind da fila à exchange para escutar todas as mensagens
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name, routing_key='#')

    print(" [*] Aguardando mensagens de todos os tipos. Para sair, pressione CTRL+C")

    # Callback que exibe a mensagem recebida
    def callback(ch, method, properties, body):
        print(f" [x] Recebeu: {body.decode()}")

    # Consumir mensagens da fila de auditoria
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    main()
