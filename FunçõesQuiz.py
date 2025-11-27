import random
from Banco import banco_questoes


def sortear_questoes(qtd=20):
    """escolhe 20 pergunta aleatória, de 50""" 
    return random.sample(banco_questoes, qtd)


def exibir_questao(questao, numero):
    print(f"\n==============================")
    print(f"❓ Questão {numero}")
    print(f"==============================")
    print(questao["pergunta"])
    print()

    # embaralha as alternativa
    alternativas = list(questao["alternativas"].items())
    random.shuffle(alternativas)

    letra_map = ["A", "B", "C", "D", "E"]
    nova_ordem = {}

    for i, (letra_original, texto) in enumerate(alternativas):
        nova_ordem[letra_map[i]] = texto
        print(f"{letra_map[i]}) {texto}")

    return nova_ordem


def verificar_resposta(resposta_jogador, questao, alternativas_embaralhadas):
    """verifica se a resposta do usuario é a certa"""

    correta_original = questao["correta"]
    texto_correto = questao["alternativas"][correta_original]

    # descobre onde a certa foi parar
    letra_correta_embaralhada = None
    for letra, texto in alternativas_embaralhadas.items():
        if texto == texto_correto:
            letra_correta_embaralhada = letra
            break

    # retorna
    # 1. se o usuario acerto (True/False)
    # 2. a alternativa correta (A-E após embaralhar)
    # 3. o texto da alternativa correta
    return (
        resposta_jogador.upper() == letra_correta_embaralhada,
        letra_correta_embaralhada,
        texto_correto
    )



def exibir_resultado(acertos):
    """ve a nota final"""
    nota = acertos * 0.5
    print("\n====================================")
    print(f"✔️  Total de acertos: {acertos}/20")
    print(f"📘 Nota final: {nota:.1f} / 10.0")
    print("====================================\n")
