import pika
import sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    especialidades = ['cardiologista', 'dermatologista', 'pediatra', 'psiquiatra', 'ginecologista',
                      'oncologista', 'geriatra', 'endocrinologista', 'urologista', 'pneumologista']

    while True:
        print("\nEscolha uma especialidade para filtrar as mensagens:")
        for i, especialidade in enumerate(especialidades, start=1):
            print(f"{i}. {especialidade}")
        print("0. Sair")
        
        escolha = input("Digite o número da especialidade desejada: ")

        if escolha == '0':
            print("Saindo...")
            break

        if escolha.lower() == 'v':
            continue

        try:
            indice_escolhido = int(escolha) - 1
            if 0 <= indice_escolhido < len(especialidades):
                especialidade = especialidades[indice_escolhido]
                queue_name = f"consulta_fila_{especialidade}"
                
                print(f"\nAguardando mensagens para a especialidade: {especialidade}.")
                print("Pressione 'ctrl+c' para voltar ao menu")
                
                channel.queue_declare(queue=queue_name, durable=True)

                def callback(ch, method, properties, body):
                    print(f"Consulta agendada com sucesso! Detalhes: {body.decode()}")

                channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

                try:
                    channel.start_consuming()
                except KeyboardInterrupt:
                    print("\nParando o consumo de mensagens...")
                    continue
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Digite um número.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
