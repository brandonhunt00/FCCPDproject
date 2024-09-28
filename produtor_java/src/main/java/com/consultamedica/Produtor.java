package com.consultamedica;

import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Produtor {

    private final static String EXCHANGE_NAME = "agendamento_consultas";

    public static void main(String[] argv) {
        // Configurando a fábrica de conexões
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        try (Connection connection = factory.newConnection(); Channel channel = connection.createChannel()) {
            // Declarando o exchange do tipo 'topic'
            channel.exchangeDeclare(EXCHANGE_NAME, "topic", true);

            Scanner scanner = new Scanner(System.in);
            System.out.println("=== Sistema de Agendamento de Consultas Médicas ===");

            System.out.print("Informe o ID do paciente: ");
            String pacienteId = scanner.nextLine();

            System.out.print("Tipo de solicitação (Nova_Consulta/Cancelamento/Remarcacao): ");
            String tipoSolicitacao = scanner.nextLine();

            System.out.print("Data e hora da consulta (dd/MM/yyyy - HH:mm): ");
            String dataConsulta = scanner.nextLine();

            System.out.print("Especialidade médica: ");
            String especialidade = scanner.nextLine().toLowerCase();

            System.out.print("Detalhes adicionais: ");
            String detalhes = scanner.nextLine();

            // Composição da mensagem
            String mensagem = String.format("[%s] %s : %s : %s : %s : \"%s\"",
                    LocalDateTime.now().format(DateTimeFormatter.ofPattern("dd/MM/yyyy - HH:mm")),
                    pacienteId,
                    tipoSolicitacao,
                    dataConsulta,
                    especialidade,
                    detalhes);

            // Chave de roteamento
            String routingKey = "nova_consulta." + especialidade;

            // Propriedades da mensagem para torná-la persistente
            AMQP.BasicProperties props = new AMQP.BasicProperties.Builder()
                    .deliveryMode(2) // 2 significa que a mensagem é persistente
                    .build();

            // Publicando a mensagem no exchange
            channel.basicPublish(EXCHANGE_NAME, routingKey, props, mensagem.getBytes("UTF-8"));
            System.out.println("Mensagem enviada: " + mensagem);

        } catch (Exception e) {
            System.err.println("Erro ao enviar a mensagem: " + e.getMessage());
        }
    }
}
