# tem 50 questoes sobre Arduino, todas diferentes

banco_questoes = [

    # 1
    {
        "pergunta": "O que é o Arduino?",
        "alternativas": {
            "A": "Um tipo de sensor analógico.",
            "B": "Uma placa controladora programável.",
            "C": "Um software de edição de imagens.",
            "D": "Um tipo de motor elétrico.",
            "E": "Um protocolo de comunicação de rede."
        },
        "correta": "B"
    },

    # 2
    {
        "pergunta": "Qual a linguagem usada para programar o Arduino?",
        "alternativas": {
            "A": "Python",
            "B": "Java",
            "C": "C/C++",
            "D": "Ruby",
            "E": "HTML"
        },
        "correta": "C"
    },

    # 3
    {
        "pergunta": "Qual é a placa Arduino mais utilizada para iniciantes?",
        "alternativas": {
            "A": "Arduino Due",
            "B": "Arduino Nano",
            "C": "Arduino Mega",
            "D": "Arduino Uno",
            "E": "Arduino Micro"
        },
        "correta": "D"
    },

    # 4
    {
        "pergunta": "O Arduino Uno utiliza qual microcontrolador?",
        "alternativas": {
            "A": "ESP8266",
            "B": "ATmega328P",
            "C": "PIC16F84",
            "D": "RYT2040",
            "E": "ARM Cortex"
        },
        "correta": "B"
    },

    # 5
    {
        "pergunta": "Qual porta do Arduino permite ler valores ANALÓGICOS?",
        "alternativas": {
            "A": "Portas digitais D0–D13",
            "B": "Portas USB",
            "C": "Portas A0–A5",
            "D": "Pinos VIN",
            "E": "Portas PWM"
        },
        "correta": "C"
    },

    # 6
    {
        "pergunta": "O que significa PWM?",
        "alternativas": {
            "A": "Power Motor Wave",
            "B": "Pulse Width Modulation",
            "C": "Programmable Wave Mode",
            "D": "Phase Wireless Mode",
            "E": "Pulse Wireless Motor"
        },
        "correta": "B"
    },

    # 7
    {
        "pergunta": "Qual função é executada repetidamente no código do Arduino?",
        "alternativas": {
            "A": "setup()",
            "B": "loop()",
            "C": "main()",
            "D": "repeat()",
            "E": "program()"
        },
        "correta": "B"
    },

    # 8
    {
        "pergunta": "A IDE Arduino serve para:",
        "alternativas": {
            "A": "Desenhar circuitos eletrônicos",
            "B": "Programar e enviar código para a placa",
            "C": "Criar bancos de dados",
            "D": "Compilar arquivos Java",
            "E": "Produzir áudio e vídeo"
        },
        "correta": "B"
    },

    # 9
    {
        "pergunta": "Qual tensão lógica a maioria dos Arduinos utiliza?",
        "alternativas": {
            "A": "1,8V",
            "B": "3,3V",
            "C": "5V",
            "D": "9V",
            "E": "12V"
        },
        "correta": "C"
    },

    # 10
    {
        "pergunta": "Qual porta do Arduino é usada para comunicação serial?",
        "alternativas": {
            "A": "Pinos 0 e 1",
            "B": "Pinos A4 e A5",
            "C": "Portas digitais 10 e 11",
            "D": "USB secundária",
            "E": "Porta VIN"
        },
        "correta": "A"
    },

    # 11
    {
        "pergunta": "Qual sensor mede distância usando ondas ultrassônicas?",
        "alternativas": {
            "A": "DHT11",
            "B": "LDR",
            "C": "HC-SR04",
            "D": "BMP180",
            "E": "MQ-2"
        },
        "correta": "C"
    },

    # 12
    {
        "pergunta": "Qual componente acende quando acionado pelo Arduino?",
        "alternativas": {
            "A": "LDR",
            "B": "LED",
            "C": "Push button",
            "D": "Resistor variável",
            "E": "Sensor PIR"
        },
        "correta": "B"
    },

    # 13
    {
        "pergunta": "Qual destes é um sensor de luminosidade?",
        "alternativas": {
            "A": "PIR",
            "B": "LDR",
            "C": "Ultrassom",
            "D": "Acelerômetro",
            "E": "GPS"
        },
        "correta": "B"
    },

    # 14
    {
        "pergunta": "Qual comando envia mensagens para o monitor serial?",
        "alternativas": {
            "A": "Serial.print()",
            "B": "Serial.begin()",
            "C": "Println.serial()",
            "D": "monitor.send()",
            "E": "digitalWrite()"
        },
        "correta": "A"
    },

    # 15
    {
        "pergunta": "O que o comando pinMode() faz?",
        "alternativas": {
            "A": "Cria variáveis",
            "B": "Define se um pino é entrada ou saída",
            "C": "Liga LEDs automaticamente",
            "D": "Reinicia a placa",
            "E": "Altera a voltagem"
        },
        "correta": "B"
    },

    # 16
    {
        "pergunta": "O Arduino Uno possui quantas entradas analógicas?",
        "alternativas": {
            "A": "3",
            "B": "5",
            "C": "6",
            "D": "10",
            "E": "15"
        },
        "correta": "C"
    },

    # 17
    {
        "pergunta": "O que significa IDE?",
        "alternativas": {
            "A": "Integrated Development Environment",
            "B": "Internal Device Edition",
            "C": "Integrated Digital Editor",
            "D": "Input Device Encoder",
            "E": "Internet Development Engine"
        },
        "correta": "A"
    },

    # 18
    {
        "pergunta": "O resistor serve para:",
        "alternativas": {
            "A": "Aumentar a corrente",
            "B": "Inverter polaridade",
            "C": "Limitar a corrente elétrica",
            "D": "Armazenar energia",
            "E": "Criar campos magnéticos"
        },
        "correta": "C"
    },

    # 19
    {
        "pergunta": "O que um servo motor faz?",
        "alternativas": {
            "A": "Gira apenas em 360° contínuos",
            "B": "Não possui controle de posição",
            "C": "Gira até ângulos controlados",
            "D": "Só funciona com 220V",
            "E": "É um motor de carro"
        },
        "correta": "C"
    },

    # 20
    {
        "pergunta": "Um LED precisa sempre de:",
        "alternativas": {
            "A": "Bateria de carro",
            "B": "Resistor em série",
            "C": "Dois sensores",
            "D": "Cabo HDMI",
            "E": "Bluetooth"
        },
        "correta": "B"
    },

    # 21
    {
        "pergunta": "O que caracteriza uma porta digital?",
        "alternativas": {
            "A": "Valores contínuos",
            "B": "Valores discretos (0 ou 1)",
            "C": "Somente valores negativos",
            "D": "Somente valores positivos",
            "E": "Somente sinais analógicos"
        },
        "correta": "B"
    },

    # 22
    {
        "pergunta": "Como é chamada a placa de expansão que adiciona funções ao Arduino?",
        "alternativas": {
            "A": "Cap",
            "B": "Shield",
            "C": "Core",
            "D": "Base",
            "E": "Block"
        },
        "correta": "B"
    },

    # 23
    {
        "pergunta": "O que significa a sigla USB?",
        "alternativas": {
            "A": "Universal Serial Bus",
            "B": "Ultra Sensor Board",
            "C": "United System Base",
            "D": "User Software Bridge",
            "E": "Universal Shield Board"
        },
        "correta": "A"
    },

    # 24
    {
        "pergunta": "O sensor DHT11 mede:",
        "alternativas": {
            "A": "Gás inflamável",
            "B": "Luz",
            "C": "Temperatura e umidade",
            "D": "Distância",
            "E": "Som"
        },
        "correta": "C"
    },

    # 25
    {
        "pergunta": "O que o comando digitalWrite() faz?",
        "alternativas": {
            "A": "Escreve texto no monitor serial",
            "B": "Controla motores",
            "C": "Define HIGH ou LOW em um pino",
            "D": "Lê um valor analógico",
            "E": "Cria bibliotecas"
        },
        "correta": "C"
    },

    # 26
    {
        "pergunta": "Qual desses NÃO é um tipo de Arduino?",
        "alternativas": {
            "A": "Uno",
            "B": "Nano",
            "C": "Mega",
            "D": "X-Pro 9000",
            "E": "Due"
        },
        "correta": "D"
    },

    # 27
    {
        "pergunta": "O que significa HIGH em uma porta digital?",
        "alternativas": {
            "A": "0V",
            "B": "Tensão baixa",
            "C": "Tensão alta (5V ou 3,3V)",
            "D": "Erro no sistema",
            "E": "Modo analógico"
        },
        "correta": "C"
    },

    # 28
    {
        "pergunta": "Qual destes NÃO é um sensor?",
        "alternativas": {
            "A": "LDR",
            "B": "PIR",
            "C": "HC-SR04",
            "D": "Servo motor",
            "E": "DHT22"
        },
        "correta": "D"
    },

    # 29
    {
        "pergunta": "Qual biblioteca é usada para comunicação serial?",
        "alternativas": {
            "A": "Keyboard.h",
            "B": "Servo.h",
            "C": "Wire.h",
            "D": "Serial (já integrada)",
            "E": "IRremote.h"
        },
        "correta": "D"
    },

    # 30
    {
        "pergunta": "O Arduino é muito utilizado em:",
        "alternativas": {
            "A": "Produção de filmes",
            "B": "Robótica e automação",
            "C": "Culinária",
            "D": "Esportes",
            "E": "Canto"
        },
        "correta": "B"
    },

    # 31
    {
        "pergunta": "Qual destes é um tipo de motor controlado pelo Arduino?",
        "alternativas": {
            "A": "Motor a diesel",
            "B": "Servo motor",
            "C": "Turbina industrial",
            "D": "Motor de carro V6",
            "E": "Motor nuclear"
        },
        "correta": "B"
    },

    # 32
    {
        "pergunta": "Qual componente detecta movimento?",
        "alternativas": {
            "A": "PIR",
            "B": "LDR",
            "C": "Potenciômetro",
            "D": "Resistor",
            "E": "LED"
        },
        "correta": "A"
    },

    # 33
    {
        "pergunta": "O que um potenciômetro faz?",
        "alternativas": {
            "A": "Produz luz",
            "B": "Gira motores",
            "C": "Varia resistência manualmente",
            "D": "Armazena energia",
            "E": "Remove ruídos de áudio"
        },
        "correta": "C"
    },

    # 34
    {
        "pergunta": "Para que serve a função delay()?",
        "alternativas": {
            "A": "Aumentar velocidade",
            "B": "Criar pausas em milissegundos",
            "C": "Salvar arquivos",
            "D": "Ler sensores",
            "E": "Gerar PWM"
        },
        "correta": "B"
    },

    # 35
    {
        "pergunta": "Qual destes é um protocolo de comunicação?",
        "alternativas": {
            "A": "SPI",
            "B": "LDR",
            "C": "PIR",
            "D": "LED",
            "E": "Resistor"
        },
        "correta": "A"
    },

    # 36
    {
        "pergunta": "O que significa Vin no Arduino?",
        "alternativas": {
            "A": "Porta de áudio",
            "B": "Entrada de tensão externa",
            "C": "Saída de áudio",
            "D": "Nome de biblioteca",
            "E": "Pino de PWM"
        },
        "correta": "B"
    },

    # 37
    {
        "pergunta": "O Arduino pode ser alimentado por:",
        "alternativas": {
            "A": "Cabo USB",
            "B": "VIN",
            "C": "Fonte de 7–12V",
            "D": "Todas as alternativas acima",
            "E": "Nenhuma das alternativas"
        },
        "correta": "D"
    },

    # 38
    {
        "pergunta": "A porta GND serve para:",
        "alternativas": {
            "A": "Fornecer energia",
            "B": "Aumentar tensão",
            "C": "Servir como terra do circuito",
            "D": "Transmitir dados",
            "E": "Criar frequências de PWM"
        },
        "correta": "C"
    },

    # 39
    {
        "pergunta": "O que é necessário para usar um servo motor no Arduino?",
        "alternativas": {
            "A": "Biblioteca Servo.h",
            "B": "Biblioteca Math.h",
            "C": "Biblioteca Led.h",
            "D": "Biblioteca Serial.h",
            "E": "Nenhuma biblioteca"
        },
        "correta": "A"
    },

    # 40
    {
        "pergunta": "O pino 13 do Arduino Uno possui:",
        "alternativas": {
            "A": "Um LED integrado",
            "B": "Sensor embutido",
            "C": "Motor interno",
            "D": "Bateria reserva",
            "E": "Módulo Bluetooth"
        },
        "correta": "A"
    },

    # 41
    {
        "pergunta": "O que é necessário para usar I2C?",
        "alternativas": {
            "A": "Pinos SDA e SCL",
            "B": "Pinos de PWM",
            "C": "Pinos VIN e GND",
            "D": "Biblioteca Servo",
            "E": "Nenhum fio"
        },
        "correta": "A"
    },

    # 42
    {
        "pergunta": "Qual desses sensores detecta gases?",
        "alternativas": {
            "A": "MQ-2",
            "B": "HC-SR04",
            "C": "DHT11",
            "D": "PIR",
            "E": "BMP280"
        },
        "correta": "A"
    },

    # 43
    {
        "pergunta": "Qual módulo adiciona controle remoto ao Arduino?",
        "alternativas": {
            "A": "Bluetooth HC-05",
            "B": "IR Receiver",
            "C": "Wi-Fi ESP01",
            "D": "GPS NEO-6M",
            "E": "MPU6050"
        },
        "correta": "B"
    },

    # 44
    {
        "pergunta": "Para conectar o Arduino ao computador é usado:",
        "alternativas": {
            "A": "Cabo HDMI",
            "B": "Cabo USB",
            "C": "Cabo RJ45",
            "D": "Cabo DisplayPort",
            "E": "Cabo VGA"
        },
        "correta": "B"
    },

    # 45
    {
        "pergunta": "O LDR varia sua resistência de acordo com:",
        "alternativas": {
            "A": "Som",
            "B": "Calor",
            "C": "Luz",
            "D": "Movimento",
            "E": "Pressão"
        },
        "correta": "C"
    },

    # 46
    {
        "pergunta": "O que significa LED?",
        "alternativas": {
            "A": "Light Emitting Diode",
            "B": "Low Energy Device",
            "C": "Long Electric Device",
            "D": "Laser Electronic Display",
            "E": "Linear Energy Driver"
        },
        "correta": "A"
    },

    # 47
    {
        "pergunta": "Qual protocolo usa dois fios para comunicação?",
        "alternativas": {
            "A": "UART",
            "B": "SPI",
            "C": "I2C",
            "D": "Wi-Fi",
            "E": "Bluetooth"
        },
        "correta": "C"
    },

    # 48
    {
        "pergunta": "O módulo HC-05 é usado para:",
        "alternativas": {
            "A": "Bluetooth",
            "B": "Ultrassom",
            "C": "Luminosidade",
            "D": "Temperatura",
            "E": "Gás"
        },
        "correta": "A"
    },

    # 49
    {
        "pergunta": "Qual a função do botão RESET no Arduino?",
        "alternativas": {
            "A": "Apagar o código",
            "B": "Reiniciar a execução do programa",
            "C": "Remover bibliotecas",
            "D": "Formatar a placa",
            "E": "Ajustar voltagem"
        },
        "correta": "B"
    },

    # 50
    {
        "pergunta": "O que é uma breadboard?",
        "alternativas": {
            "A": "Uma placa para fritar pão",
            "B": "Uma placa de ensaio sem solda",
            "C": "Um sensor de calor",
            "D": "Um módulo Wi-Fi",
            "E": "Um motor de precisão"
        },
        "correta": "B"
    }

]
