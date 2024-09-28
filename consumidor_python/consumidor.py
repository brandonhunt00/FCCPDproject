import pika

especialidades = [
    'cardiologista', 'dermatologista', 'pediatra', 'psiquiatra',
    'ginecologista', 'oncologista', 'geriatra', 'endocrinologista',
    'urologista', 'oftalmologista'
]

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    while True:
        # Menu de especialidades
        print("\nEscolha uma especialidade para filtrar as mensagens:")
        for i, especialidade in enumerate(especialidades, start=1):
            print(f"{i}. {especialidade}")
        print("0. Sair")

        choice = input("Digite o número da especialidade desejada: ")

        if choice == '0':
            print("Saindo do programa...")
            break

        try:
            choice_idx = int(choice) - 1
            if choice_idx < 0 or choice_idx >= len(especialidades):
                print("Escolha inválida. Tente novamente.")
                continue

            especialidade = especialidades[choice_idx]
            queue_name = f'consulta_fila_{especialidade.lower()}'

            # Declarar a fila como durável e iniciar a escuta
            channel.queue_declare(queue=queue_name, durable=True)

            print(f"\nAguardando mensagens para a especialidade: {especialidade}.")
            print("Digite 'v' para voltar ao menu de especialidades.")

            # Consumindo mensagens da fila
            while True:
                method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

                if method_frame:
                    print(f"[x] Consulta agendada com sucesso: {body.decode('utf-8')}")

                user_input = input()
                if user_input.lower() == 'v':
                    print("\nVoltando ao menu de especialidades...")
                    break

        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()
