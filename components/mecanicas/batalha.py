import time
import random

def calcular_dano(ataque, defesa, multiplicador= 1.0):
    dano_bruto = (ataque * multiplicador) * (100 / (defesa + 100))
    return max(1, int(dano_bruto))

def iniciar_batalha(aliado, inimigo):
    print("\n=====================================")
    print(f"\nUm {inimigo.nome} selvagem apareceu!")
    print("\n=====================================")

    aliado.energia = 0
    inimigo.energia = 0

    while aliado.hp > 0 and inimigo.hp > 0:
        print(f"\n--- ALIADO {aliado.nome}: HP {aliado.hp} | Energ. {aliado.energia}")
        print(f"--- INIMIGO {inimigo.nome}: HP {inimigo.hp} | Energ. {inimigo.energia}")
        print("---------------------------------------------------")
        print("\n1 - Ataque basico (+10 energia)")

        if aliado.energia >= 30:
            print("2 - Ataque especial (-30 energia)")
        else:
            print("2 - Ataque especial (não disponível)")

        print("3 - Esquivar")
        print("4 - Fugir do combate")

        escolha = input("Escolha sua ação (1 a 4): ")

        if escolha == "4":
            print("\n----------------------")
            print("Você fugiu do combate.")
            return
        if escolha == "3":
            acao_aliado = "esquivar"
        elif escolha == "2" and aliado.energia >= 30:
            acao_aliado = "especial"
        else:
            acao_aliado = "basico"

        acao_inimigo = "especial" if inimigo.energia >= 30 else "basico"

        if aliado.velocidade >= inimigo.velocidade:
            ordem = [(aliado, acao_aliado, inimigo, acao_inimigo), (inimigo, acao_inimigo, aliado, acao_aliado)]
        else:
            ordem = [(inimigo, acao_inimigo, aliado, acao_aliado), (aliado, acao_aliado, inimigo, acao_inimigo)]

        for atacante, acao_atk, defensor, acao_def in ordem:
            if atacante.hp <= 0:
                continue

            if acao_atk == "esquivar":
                print(f"\n{atacante.nome} focou na agilidade e está pronto para esquivar!")
                time.sleep(1.0)
                continue
            print(f"\n{atacante.nome} usou Ataque {acao_atk.capitalize()}!")

            if acao_atk == "basico":
                dano = calcular_dano(atacante.ataque, defensor.defesa)
                atacante.energia += 10
            elif acao_atk == "especial":
                dano = calcular_dano(atacante.ataque, defensor.defesa, multiplicador=1.5)
                atacante.energia -= 30

            if acao_def == "esquivar":
                sorte = random.randint(1, 100)
                if sorte <= 40:
                    dano = 0
                    print(f"-> {defensor.nome} ESQUIVOU PERFEITAMENTE e não tomou dano!")
                elif 41 <= sorte <= 90:
                    dano = max(1, dano // 2)
                    print(f"-> {defensor.nome} esquivou parcialmente e tomou metade do dano!")
                else:
                    dano = max(1, dano // 1)
                    print(f"-> {defensor.nome} não conseguiu esquivar e recebeu o ataque!")
            else:
                print(f"-> Causou {dano} de dano!")

            defensor.hp -= dano
            print(f"[{defensor.nome} ficou com {max(0, defensor.hp)} de HP.]")
            time.sleep(1.5)

            if defensor.hp <= 0:
                break

        if aliado.hp <= 0 or inimigo.hp <= 0:
            break

    if aliado.hp > 0:
        print(f"\nVitória! {inimigo.nome} foi derrotado!")
    else:
        print(f"\nDerrota! Seu {aliado.nome} desmaiou.")