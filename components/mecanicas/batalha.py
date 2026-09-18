import time
import random

from components.criatura.tipos import multiplicador_tipo, descrever_efetividade

CUSTO_ESPECIAL = 30
GANHO_ENERGIA_BASICO = 10


def limite_energia(criatura) -> int:
    # A barra sempre comporta ao menos um especial; energia_max acima disso permite acumular mais.
    return max(criatura.energia_max, CUSTO_ESPECIAL)



def calcular_dano(ataque, defesa, multiplicador=1.0):
    dano_bruto = (ataque * multiplicador) * (100 / (defesa + 100))
    return max(1, int(dano_bruto))


def iniciar_batalha(aliado, inimigo, jogador):
    print("\n=====================================")
    print(f"\nUm {inimigo.nome} selvagem ({inimigo.tipo}) apareceu!")
    print("\n=====================================")

    aliado.energia = 0
    inimigo.energia = 0

    while aliado.hp > 0 and inimigo.hp > 0:
        print(f"\n--- ALIADO {aliado.nome} ({aliado.tipo}): HP {aliado.hp} | Energ. {aliado.energia}")
        print(f"--- INIMIGO {inimigo.nome} ({inimigo.tipo}): HP {inimigo.hp} | Energ. {inimigo.energia}")
        print("---------------------------------------------------")
        print(f"\n1 - Ataque basico (+{GANHO_ENERGIA_BASICO} energia)")

        if aliado.energia >= CUSTO_ESPECIAL:
            print(f"2 - Ataque especial (-{CUSTO_ESPECIAL} energia)")
        else:
            print("2 - Ataque especial (não disponível)")

        print("3 - Esquivar")
        print("4 - Usar Injeção")
        print("5 - Fugir do combate")

        escolha = input("Escolha sua ação (1 a 5): ")

        if escolha == "5":
            print("\n----------------------")
            print("Você fugiu do combate.")
            return
        if escolha == "3":
            acao_aliado = "esquivar"
        elif escolha == "4" and jogador.tem_item("Injeção"):
            jogador.usar_item("Injeção")
            cura = 20
            aliado.hp = min(aliado.hp + cura, aliado.hp_maximo)
            print(f"\n{aliado.nome} recuperou {cura} de HP!")
            acao_aliado = "curar"
        elif escolha == "2" and aliado.energia >= CUSTO_ESPECIAL:
            acao_aliado = "especial"
        else:
            if escolha == "4":
                print("\nVocê não tem Injeção! Usando ataque básico.")
            elif escolha == "2":
                print("\nEnergia insuficiente para o especial! Usando ataque básico.")
            acao_aliado = "basico"

        acao_inimigo = "especial" if inimigo.energia >= CUSTO_ESPECIAL else "basico"

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

            if acao_atk == "curar":
                continue

            print(f"\n{atacante.nome} usou Ataque {acao_atk.capitalize()}!")
            mult_tipo = multiplicador_tipo(atacante.tipo, defensor.tipo)

            if acao_atk == "basico":
                dano = calcular_dano(atacante.ataque, defensor.defesa, multiplicador=mult_tipo)
                atacante.energia = min(atacante.energia + GANHO_ENERGIA_BASICO, limite_energia(atacante))

            elif acao_atk == "especial":
                dano = calcular_dano(atacante.ataque, defensor.defesa, multiplicador=1.5 * mult_tipo)
                atacante.energia -= CUSTO_ESPECIAL

            efetividade = descrever_efetividade(mult_tipo)
            if efetividade:
                print(f"-> {efetividade}")

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
        xp_ganho = inimigo.calcular_xp_recompensa()
        aliado.ganhar_xp(xp_ganho)
    else:
        print(f"\nDerrota! Seu {aliado.nome} desmaiou.")
