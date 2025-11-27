def mostrar_regras():
    regras = """
    #####################################################################
    #           📜 REGRAS DO QUIZ INTERATIVO ARDUINO 🧠                #
    #####################################################################

    Bem-vindo(a) ao Quiz Interativo Arduino! Este programa testará seus
    conhecimentos sobre o universo Arduino.

    🎯 OBJETIVO DO JOGO:
    O objetivo é responder corretamente o maior número possível de questões
    sorteadas, buscando a pontuação máxima de 10,0 pontos.

    ❓ COMO FUNCIONA:
    1.  **Seleção:** A cada execução, 20 perguntas serão sorteadas aleatoriamente
        do banco de dados (mínimo de 50 questões).
    2.  **Formato:** Todas as questões são de múltipla escolha, com 5 alternativas
        (A, B, C, D, E).
    3.  **Resposta:** Digite a letra correspondente à alternativa correta
        (A, B, C, D ou E) e pressione ENTER.
    4.  **Embaralhamento:** A ordem das perguntas e das alternativas será
        embaralhada em cada nova rodada.

    💯 PONTUAÇÃO:
    * **Valor por Questão:** Cada resposta correta vale 0,5 ponto.
    * **Total de Questões:** 20 questões por rodada.
    * **Pontuação Máxima:** 10,0 pontos.
    * O resultado final será exibido ao término do Quiz.

    📚 TÓPICOS ABRANGIDOS:
    O conteúdo inclui Histórico, Modelos de Placas, Componentes, Estrutura de2

    Código (setup, loop), Portas (Digital, Analógica, PWM), Comunicações,
    Sensores, Atuadores e Boas Práticas.

    ⚠️ DICA:
    O programa irá validar sua entrada. Digite apenas as letras das opções
    válidas (A, B, C, D, E) ou do menu.

    Bons estudos e boa sorte!
    #####################################################################
    """
    print(regras)


def mostrar_menu():
    while True:
        print("\n========= MENU PRINCIPAL =========")
        print("1 - Iniciar Quiz")
        print("2 - Mostrar Regras")
        print("3 - Sair")
        print("==================================")

        op = input("Escolha uma opção: ")

        if op == "1":
            iniciar_quiz()
        elif op == "2":
            mostrar_regras()
        elif op == "3":
            print("Encerrando... Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")
