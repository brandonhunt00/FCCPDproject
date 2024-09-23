
# FCCPDproject - Sistema de Mensagens com RabbitMQ

## Descrição

Este projeto implementa um sistema de envio e recebimento de mensagens utilizando o RabbitMQ, composto por três componentes:

- **Produtor de Mensagens** (Java): responsável por enviar mensagens para a fila.
- **Consumidor de Mensagens** (Python): responsável por consumir as mensagens da fila.
- **Backend de Auditoria** (Python): recebe e exibe todas as mensagens enviadas para auditoria.

O sistema é configurado para utilizar uma exchange do tipo **topic** e permite a execução de múltiplas instâncias de produtores e consumidores, bem como a auditoria de todas as mensagens.

## Pré-requisitos

- **RabbitMQ**: Instalar e configurar o RabbitMQ. O servidor RabbitMQ deve estar rodando.
- **Java** (versão 8 ou superior)
- **Python** (versão 3.6 ou superior)
- **Pika** (biblioteca Python para RabbitMQ)
- **Maven** (para o build do projeto Java)

## Estrutura do Projeto

```bash
FCCPDproject/
├── backend_auditoria/          # Backend de auditoria em Python
│   └── backend_auditoria.py
├── consumidor_python/          # Consumidor de mensagens em Python
│   └── consumidor.py
├── produtor_java/              # Produtor de mensagens em Java
│   └── src/
│       └── main/
│           └── java/
│               └── com/
│                   └── consultamedica/
│                       └── Produtor.java
├── pom.xml                     # Configuração do Maven para o projeto Java
├── README.md                   # Este arquivo de documentação
```

## Passo a Passo para Executar

### 1. Clone o Repositório

Clone o repositório em sua máquina local:

```bash
git clone https://github.com/brandonhunt00/FCCPDproject.git
cd FCCPDproject
```

### 2. Configurar o RabbitMQ

Certifique-se de que o RabbitMQ está instalado e rodando em `localhost` (ou aponte o `host` para onde o RabbitMQ estiver rodando). Para monitorar as filas e exchanges, utilize a interface de gerenciamento do RabbitMQ acessando `http://localhost:15672/` (login padrão: **guest/guest**).

### 3. Executar o Produtor (Java)

1. **Navegue até o diretório do produtor:**
   ```bash
   cd produtor_java
   ```

2. **Build do projeto Java:**
   - Execute o Maven para construir o projeto:
     ```bash
     mvn clean package
     ```

3. **Executar o Produtor:**
   - Utilize o Maven para executar o produtor:
     ```bash
     mvn exec:java
     ```

4. **Função do Produtor:**
   - O produtor enviará mensagens para a exchange `agendamento_consultas`, e você será solicitado a inserir informações como ID do paciente, tipo de solicitação, data e hora da consulta, especialidade médica e detalhes adicionais.

### 4. Executar o Consumidor (Python)

1. **Navegue até o diretório do consumidor:**
   ```bash
   cd consumidor_python
   ```

2. **Instalar as dependências:**
   - Se necessário, ative um ambiente virtual e instale as dependências:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install pika
     ```

3. **Executar o Consumidor:**
   ```bash
   python3 consumidor.py
   ```

4. **Função do Consumidor:**
   - O consumidor escuta as mensagens enviadas para a fila `consulta_fila` e exibe o conteúdo no terminal.

### 5. Executar o Backend de Auditoria (Python)

1. **Navegue até o diretório do backend de auditoria:**
   ```bash
   cd backend_auditoria
   ```

2. **Instalar as dependências:**
   - Se necessário, ative o ambiente virtual e instale as dependências:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install pika
     ```

3. **Executar o Backend de Auditoria:**
   ```bash
   python3 backend_auditoria.py
   ```

4. **Função do Backend:**
   - O backend de auditoria recebe todas as mensagens da exchange `agendamento_consultas` e exibe o conteúdo para auditoria.

### 6. Menu de Opções (Produtor, Consumidor ou Auditoria)

Foi implementado um menu de opções simples para que o usuário possa escolher se deseja iniciar o **Produtor**, o **Consumidor**, ou o **Backend de Auditoria**:

1. **No terminal, execute:**
   ```bash
   python menu_opcoes.py
   ```

2. **Escolha a opção desejada no menu interativo.**

## Testes e Execução Simultânea

Para testar a execução simultânea de várias instâncias de produtores e consumidores:

- Abra múltiplos terminais e execute os consumidores, auditorias e produtores em cada um.
- Certifique-se de que os consumidores recebem as mesmas mensagens enviadas, conforme esperado no modo de broadcast.

## Contribuidores

- **Lucas Rosati** - Desenvolvedor
- **Brandon Hunt** - Desenvolvedor
- **Sivert Muren** - Desenvolvedor
- **Anders Burok** - Desenvolvedor
