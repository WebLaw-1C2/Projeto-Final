# Projeto-Final
Proposto pelo professor Ronildo Aparecido, como último trabalho em python a ser realizado até o fim do ano.

// Grupo: WebLaw - Davi de Jesus, Gabriel Macedo, João Gabriel e Nicolas de Oliveira 

🧠 Atividade Avaliativa – 4º Bimestre
  Curso Técnico em Desenvolvimento de Sistemas — Nível Médio
  Tema: Arduino – História, Placas, Componentes, Código e Aplicações

🎯 Objetivo da Atividade
  Desenvolver um programa em Python que funcione como um quiz interativo (perguntas e respostas)
  sobre Arduino, avaliando o domínio dos conteúdos trabalhados durante o bimestre.
  A atividade tem como foco o raciocínio lógico, a organização modular do código, o uso de funções, o
  tratamento de dados, e a aplicação prática dos conceitos de programação estudados.

🧩 Descrição Geral
  O grupo deverá criar um programa completo em Python capaz de:
  •Apresentar um menu interativo com opções como:
  •Responder Quiz
  •Exibir Regras
  •Encerrar Programa
  •Sortear questões de múltipla escolha, 5 alternativas, sobre Arduino.
  •Calcular e exibir automaticamente a pontuação final do jogador.
  •Ser modularizado, com funções bem definidas e comentários explicativos.
  •Manter as perguntas e alternativas dentro do próprio código (sem arquivos externos).
  •Embaralhar tanto as perguntas quanto as alternativas em cada execução.

📚 Conteúdo das Questões
    As perguntas deverão abranger os seguintes tópicos do módulo Arduino:
    1.Histórico e origem do projeto
    2.Modelos e famílias de placas (Uno, Mega, Nano, etc.)
    3.Componentes e arquitetura básica
    4.Conexões, portas e sinais (digitais, analógicos, PWM)
    5.Estrutura de código (setup, loop, funções, bibliotecas)
    6.Principais comandos e funções da IDE Arduino
    7.Sensores, atuadores e shields
    8.Comunicações: Serial, I²C, SPI, Bluetooth, Wi-Fi
    9.Boas práticas e segurança elétrica
    10.Casos de uso e aplicações práticas

🧮 Regras e Critérios Técnicos
  Item Descrição
  Quantidade mínima de perguntas no banco 50
  Quantidade sorteada por execução 20
  Modelo das questões Múltipla escolha (A–E)
  Valor de cada questão 0,5 ponto
  Nota máxima 10,0 pontos
  Sorteio das perguntas e alternativas Sim, obrigatório
  Estrutura modular O código deve ser dividido em funções
  Comentários O código deve conter comentários explicativos
  Menu principal Opções: Responder, Regras e Encerrar
  Banco de perguntas Embutido no código (não externo)
  Pontuação Exibida ao final do jogo

💻 Requisitos de Programação
  O programa deve conter, no mínimo, as seguintes funções(EXEMPLO):
  1.mostrar_menu() — Exibe as opções principais.
  2.mostrar_regras() — Exibe as instruções do jogo.
  3.sortear_questoes() — Seleciona aleatoriamente as perguntas.
  4.exibir_questao() — Mostra enunciado e alternativas.
  5.verificar_resposta() — Avalia acertos e soma a pontuação.
  6.exibir_resultado() — Mostra o desempenho final.
  💡 Dica: cada função deve realizar apenas uma tarefa específica, para manter a clareza e a reutilização
  do código.

👥 Organização dos Grupos
  •A atividade é em grupo.
  •Cada grupo deve definir um nome de equipe e um responsável pela entrega (Manter o mesmo
  do 3 BIMESTRE).
  •Todos os membros devem constar no README.md do repositório, com suas funções (ex.:
  lógica, design, revisão, documentação).
  •Todos devem colaborar em uma parte do projeto. (Isto deve ficar claro no GitHub, através dos
  COMMIT’s)

📆 Entrega e Apresentação
  Etapa Descrição
  Data de entrega 22/11/2025
  Forma de entrega Envio via repositório GitHub (público ou privado com acesso ao
  professor)
  Apresentação Demonstração em sala de aula (execução + explicação técnica)
  Tempo de apresentação 5 a 8 minutos por grupo
  Itens obrigatórios no
  repositório quiz_arduino.py, README.md.

🧾 Critérios de Avaliação (Total: 10 pontos)
  Critério Descrição Valor
  Funcionalidade Cumprimento dos requisitos técnicos e regras 4,0
  Qualidade do código Organização, modularização, clareza e comentários 2,0
  Conteúdo Qualidade e abrangência das perguntas (mínimo 50) 2,0
  Apresentação Clareza na demonstração e explicação em aula 2,0
  Bônus opcional Ranking, cronômetro, ou outro item. +1,0

🧪 Checklist de Testes
  Antes de entregar, verifique se o programa:
  • Apresenta menu com opções de jogo e encerramento.
  • Mostra regras e instruções corretamente.
  • Sorteia 20 perguntas aleatórias a cada execução.
  • Embaralha as alternativas de cada pergunta.
  • Valida entradas incorretas sem quebrar o programa.
  • Exibe a nota final corretamente.
  • Contém funções bem separadas e comentários explicativos.
  • É executável em Python 3.10 ou superior.

🧭 Exemplo de Estrutura de Pastas
  AA4B_Quiz_Arduino/
  │
  ├── quiz_arduino.py # Código principal (com perguntas e funções)
  └── README.md # Identificação do grupo e orientações
  🧠 Orientações Finais
  •Utilize boas práticas de programação: nomes de variáveis claros, comentários úteis e código
  limpo.
  •Evite copiar códigos prontos da internet — o importante é entender o funcionamento.
  •O programa deve ser executável em qualquer computador com Python 3.10+ sem depender de
  bibliotecas externas.
  •Grupos que demonstrarem criatividade, interface aprimorada ou recursos extras poderão
  receber bônus de até 1,0 ponto.
  📍 Resumo Rápido
  •📘 Tema: Arduino – História, Placas, Componentes, Código...
  •🧩 Tipo: Quiz interativo (múltipla escolha)
  •👥 Trabalho em grupo (MESMO DO 3 BIMESTRE)
  •🔢 50 perguntas no banco / 20 por execução
  •📅 Entrega: 22/11/2025 via GitHub + apresentação em aula
  •💯 Valor: até 10 pontos (+1 bônus)
  •💻 Linguagem: Python (versão 3.10 ou superior)
