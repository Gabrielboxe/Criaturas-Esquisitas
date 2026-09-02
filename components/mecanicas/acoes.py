from components.criatura.criaturas_selvagens import sortear_criatura_selvagem
from components.mecanicas.batalha import iniciar_batalha
from components.mecanicas.missoes import gerar_missao
from criatura.criaturas_selvagens import BIOMAS_DISPONIVEIS
from mecanicas.missoes import Missao


def menu_explorar(jogador):
    while True:
        print("\n" + "=" * 30)
        print("--- EXPLORAR ----")
        print("1 - Explorar um bioma")
        print("2 - Selecionar uma missão")
        print("3 - Entrar na loja")
        print("4 - Curar minhas criaturas")
        print("5 - Voltar ao menu principal")
        print("=" * 30)

        escolha = input("O que deseja fazer agora?")

        if escolha == "1":
            menu_bioma(jogador)
        elif escolha == "2":
            menu_missoes(jogador)
        elif escolha == "3":
            print("\nHm... parece que a loja não abriu ainda.")
        elif escolha == "4":
            curar_equipe(jogador)
        elif escolha =="5":
            return
        else:
            print("\nComando inválido!")

def menu_bioma(jogador):
    print("\nEscolha o bioma para explorar:")
    for i, bioma in enumerate(BIOMAS_DISPONIVEIS, start=1):
        print(f"{i} - {bioma}")

    escolha_bioma = input("bioma: ")
    try:
        bioma_escolhido = BIOMAS_DISPONIVEIS[int(escolha_bioma) - 1]
    except (ValueError, IndexError):
        print("\nBioma Inválido!")
        return

    while True:
        print(f"\n--- {bioma_escolhido.upper()} ---")
        print("1 - Encontrar criatura")
        print("2 - Colocar armadilha ")
        print("3 - Voltar")

        acao_bioma = input("O que deseja fazer? ")

        if acao_bioma == "1":
            encontrar_criatura(jogador, bioma_escolhido)
            return
        elif acao_bioma == "2":
            print("\nAinda não temos permissões para montar armadilhas.")
        elif acao_bioma == "3":
            return
        else:
            print("\nComando inválido!")

def encontrar_criatura(jogador, bioma):
    inimigo = sortear_criatura_selvagem(bioma)
    if inimigo is None:
        print(f"\nNenhuma criatura foi encontrada em {bioma} dessa vez...")
        return

    aliado = jogador.time[0]
    iniciar_batalha(aliado, inimigo, jogador)

    if aliado.hp <= 0:
        print("\nSua criatura desmaiou, você correu para o Veterinário...")
        aliado.hp = aliado.hp_maximo

    for missao in jogador.missoes:
        if not missao.concluida and missao.criatura_alvo.nome == inimigo.nome and aliado.hp > 0:
            missao.concluida = True
            jogador.dinheiro += missao.recompensa
            print(f"\nMissão concluída! Você recebeu ${missao.recompensa}")

    jogador.missoes = [m for m in jogador.missoes if not m.concluida]

def menu_missoes(jogador):
    print(f"\nMissões de {jogador.nome}:")
    if not jogador.missoes:
        print("Nenhuma missão ativa.")
    else:
        for i, missao in enumerate(jogador.missoes, start=1):
            print(f"{i} - {missao.descricao()}")

    if jogador.pode_receber_missao():
        gerar = input("\nGerar uma nova missão?(s/n) ")
        if gerar.lower() == "s":
            nova_missao = gerar_missao()
            if nova_missao:
                jogador.missoes.append(nova_missao)
                print(f"\nNova missão: {nova_missao.descricao()}")
    else:
        print("\nVocê já tem missões demais! Conclua ou descarte uma antes de gerar outra.")

def curar_equipe(jogador):
    CUSTO_CURA = 2
    criaturas_para_curar = [c for c in jogador.time if c.hp < c.hp_maximo]

    if not criaturas_para_curar:
        print("\nA equipe já está com a vida cheia.")
        return

    custo_total = CUSTO_CURA * len(criaturas_para_curar)
    print(f"\nCurar {len(criaturas_para_curar)} criatura(s) vai custar ${custo_total}.")
    confirmar = input("\nDeseja continuar? (s/n): ")

    if confirmar.lower() != "s":
        print("\nCura cancelada.")
        return

    if jogador.dinheiro < custo_total:
        print(f"\nVocê não tem dinheiro suficiente! (${jogador.dinheiro})")
        return

    jogador.dinheiro -= custo_total
    for criatura in criaturas_para_curar:
        criatura.hp = criatura.hp_maximo
        print(f"{criatura.nome} foi curado!")

    print(f"\nVocê pagou ${custo_total}. Saldo atual: ${jogador.dinheiro}")

def menu_equipe(jogador):
    while True:
        print("\n--- MENU EQUIPE ---")
        print("1 - Ver time ")
        print("2 - Ver criaturas disponíveis")
        print("3 - Voltar")
        sub_opcao = input("Escolha uma opção: ")

        if sub_opcao == "1":
            print("\n--- SEU TIME ---")
            if not jogador.time:
                print("Seu time está vazio.")
            for criatura in jogador.time:
                print(f"{criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}")
        elif sub_opcao == "2":
            print("\n--- CRIATURAS DISPONIVEIS ---")
            if not jogador.criaturas_capturadas:
                print("Você ainda não capturou criaturas esquisitas.")
            for criatura in jogador.criaturas_capturadas:
                print(f"{criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}")
        elif sub_opcao == "3":
            break
        else:
            print("Opção inválida!")


