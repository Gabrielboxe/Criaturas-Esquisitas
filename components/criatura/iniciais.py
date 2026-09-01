import random

from components.criatura.criatura import Criatura
from components.player.treinador import Treinador


def gerar_solenodonte():
    return Criatura(
        nome="Solenodonte",
        hp=15,
        ataque=30,
        defesa=10,
        velocidade=30,
        energia=15,
    )

def gerar_ornitorrinco():
    return Criatura(
        nome="Ornitorrinco",
        hp=20,
        ataque=20,
        defesa=20,
        velocidade=20,
        energia=20,
    )

def gerar_poraque():
    return Criatura(
        nome="Poraquê",
        hp=20,
        ataque=20,
        defesa=10,
        velocidade=30,
        energia=35,
    )

inicial = None

def escolher_inicial(treinador: Treinador):
    print(f"Olá {treinador.nome}! Está na hora de começar sua jornada!")
    print(f"Escolha sua criatura esquisita inicial: ")
    print(f"1 - Solenodonte. ")
    print(f"2 - Ornitorrinco. ")
    print(f"3 - Poraque. ")
    print(f"4 - Surpreenda-me! (Aleatório)\n")
    print(f"4 - Sair da escolha. ")

    def encerrar_escolha():
        print("Encerrando escolhas! Obrigado!")

    opcoes_aleatorias = [gerar_solenodonte, gerar_ornitorrinco, gerar_poraque]

    while True:
        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            inicial = gerar_solenodonte()
            break
        elif escolha == "2":
            inicial = gerar_ornitorrinco()
            break
        elif escolha == "3":
            inicial = gerar_poraque()
            break
        elif escolha == "4":
            funcao_sorteada = random.choice(opcoes_aleatorias)
            inicial = funcao_sorteada()
            break
        elif escolha == "5":
            sair = input("Deseja sair? (y/n)")
            if sair == "y":
                encerrar_escolha()
                return
            else:
                continue
        else:
            print("\n Comando inválido. Selecione uma das opções!")

    if inicial is not None:
        treinador.adicionar_criatura_treinador(inicial)