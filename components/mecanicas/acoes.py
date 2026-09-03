from components.criatura.criaturas_selvagens import sortear_criatura_selvagem, BIOMAS_DISPONIVEIS
from components.mecanicas.batalha import iniciar_batalha
from components.mecanicas.missoes import gerar_missao
from components.mecanicas.loja import menu_loja, NOMES_ARMADILHAS
from components.mecanicas.armadilhas import tentar_capturar
from components.player.treinador import TAMANHO_MAXIMO_TIME

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
            menu_loja(jogador)
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

    armadilha_ativa = jogador.armadilhas_ativas.get(bioma_escolhido)

    if armadilha_ativa:
        print(f"\n--- {bioma_escolhido.upper()} ---")
        print(f"Há uma {armadilha_ativa['tipo']} armada aqui, esperando a criatura...")
        print("Melhor deixar o bioma silencioso se quiser que a armadilha funcione...")

        if armadilha_ativa["pronta"]:
            print("1 - Checar armadilha")
            print("2 - Voltar")
            acao_armadilha = input("O que deseja fazer? ")
            if acao_armadilha == "1":
                checar_armadilha(jogador, bioma_escolhido)
            return
        else:
            print("A armadilha ainda não está pronta. Volte depois de uma batalha.")
            return

    while True:
        print(f"\n--- {bioma_escolhido.upper()} ---")
        print("1 - Encontrar criatura")
        print("2 - Colocar armadilha")
        print("3 - Voltar")

        acao_bioma = input("O que deseja fazer? ")

        if acao_bioma == "1":
            encontrar_criatura(jogador, bioma_escolhido)
            return
        elif acao_bioma == "2":
            colocar_armadilha(jogador, bioma_escolhido)
            return
        elif acao_bioma == "3":
            return
        else:
            print("\nComando inválido!")

def encontrar_criatura(jogador, bioma):
    aliado = escolher_aliado(jogador)
    if aliado is None:
        return

    inimigo = sortear_criatura_selvagem(bioma)
    if inimigo is None:
        print(f"\nNenhuma criatura foi encontrada em {bioma} dessa vez...")
        return

    iniciar_batalha(aliado, inimigo, jogador)

    for armadilha in jogador.armadilhas_ativas.values():
        armadilha["pronta"] = True

    if aliado.hp <= 0:
        print("\nSua criatura desmaiou, você correu para o Veterinário...")
        aliado.hp = aliado.hp_maximo

    for missao in jogador.missoes:
        if not missao.concluida and missao.criatura_alvo.nome == inimigo.nome and aliado.hp > 0:
            missao.concluida = True
            jogador.dinheiro += missao.recompensa
            print(f"\nMissão concluída! Você recebeu ${missao.recompensa}")

    jogador.missoes = [m for m in jogador.missoes if not m.concluida]

def colocar_armadilha(jogador, bioma):
    tipos_disponiveis = [nome for nome in NOMES_ARMADILHAS if jogador.tem_item(nome)]

    if not tipos_disponiveis:
        print("\nVocê não tem nenhuma armadilha no inventário. Compre uma na loja!")
        return

    print("\nQual armadilha deseja usar?")
    for i, nome in enumerate(tipos_disponiveis, start=1):
        print(f"{i} - {nome} ({jogador.inventario.get(nome, 0)} disponíveis)")

    escolha = input("Escolha: ")
    try:
        nome_armadilha = tipos_disponiveis[int(escolha) - 1]
    except (ValueError, IndexError):
        print("\nComando inválido!")
        return

    criatura_alvo = sortear_criatura_selvagem(bioma)
    if criatura_alvo is None:
        print(f"\nVocê armou a {nome_armadilha}, mas nenhuma criatura parece estar por perto...")
        return

    jogador.usar_item(nome_armadilha)
    jogador.armadilhas_ativas[bioma] = {
        "tipo": nome_armadilha,
        "criatura": criatura_alvo,
        "pronta": False,
    }
    print(f"\nVocê armou a {nome_armadilha} em {bioma}. Volte depois de uma batalha para checar!")


def checar_armadilha(jogador, bioma):
    armadilha = jogador.armadilhas_ativas.pop(bioma, None)
    if armadilha is None:
        return

    criatura = armadilha["criatura"]
    sucesso = tentar_capturar(armadilha["tipo"], criatura)

    if sucesso:
        print(f"\nSucesso! Você capturou {criatura.nome}!")
        jogador.adicionar_criatura_treinador(criatura)
    else:
        print(f"\nA armadilha não funcionou dessa vez... {criatura.nome} escapou.")

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

def escolher_aliado(jogador):
    disponiveis = [c for c in jogador.time if c.hp > 0]

    if not disponiveis:
        print("\nTodas as suas criaturas estão sem HP! Tente curá-las antes de batalhar.")
        return None

    if len(disponiveis) == 1:
        return disponiveis[0]

    print("\nQual criatura vai para a batalha?")
    for i, criatura in enumerate(disponiveis, start=1):
        print(f"{i} - {criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}/{criatura.hp_maximo}")

    escolha = input("Escolha: ")
    try:
        return disponiveis[int(escolha) - 1]
    except (ValueError, IndexError):
        print("\nComando inválido! Escolha automática ativada.")
        return disponiveis[0]

def menu_equipe(jogador):
    while True:
        print("\n--- MENU EQUIPE ---")
        print(" 1 - Ver time ")
        print(" 2 - Ver criaturas disponiveis")
        print(" 3 - mover criatura do Santuário para o time")
        print(" 4 - Mover criatura do time para o Santuário")
        print(" 5 - voltar")
        sub_opcao = input("Escolha uma opção: ")

        if sub_opcao == "1":
            print("\n--- SEU TIME ---")
            if not jogador.time:
                print("Seu time está vazio.")
            for criatura in jogador.time:
                print(f"- - - {criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}/{criatura.hp_maximo}")

        elif sub_opcao == "2":
            print("\n--- CRIATURAS DISPONIVEIS ---")
            if not jogador.criaturas_capturadas:
                print("\nVocê ainda não capturou criaturas esquisitas.")
                return
            for criatura in jogador.criaturas_capturadas:
                print(f"{criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}")

        elif sub_opcao == "3":
            mover_para_time(jogador)

        elif sub_opcao == "4":
            mover_para_santuario(jogador)

        elif sub_opcao == "5":
            break

        else:
            print("Opção invalida!")

def mover_para_time(jogador):
    if not jogador.criaturas_capturadas:
        print("\nVocê não tem nenhuma criatura no Santuário.")
        return

    if len(jogador.time) >= TAMANHO_MAXIMO_TIME:
        print(f"\nSeu time já está cheio (máx. {TAMANHO_MAXIMO_TIME}). Mova alguém para o Santuário primeiro.")
        return

    print("\n--- CRIATURAS DISPONÍVEIS ---")
    for i, criatura in enumerate(jogador.criaturas_capturadas, start=1):
        print(f"{i} - {criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}")

    escolha = input("Qual criatura deseja trazer para o time? ")
    try:
        criatura = jogador.criaturas_capturadas.pop(int(escolha) - 1)
    except (ValueError, IndexError):
        print("\nComando inválido!")
        return

    jogador.time.append(criatura)
    print(f"\n{criatura.nome} entrou para o time!")


def mover_para_santuario(jogador):
    if not jogador.time:
        print("\nSeu time está vazio.")
        return

    print("\n--- SEU TIME ---")
    for i, criatura in enumerate(jogador.time, start=1):
        print(f"{i} - {criatura.nome} | Nv. {criatura.nivel} | HP {criatura.hp}")

    escolha = input("Qual criatura deseja enviar para o Santuário? ")
    try:
        criatura = jogador.time.pop(int(escolha) - 1)
    except (ValueError, IndexError):
        print("\nComando inválido!")
        return

    jogador.criaturas_capturadas.append(criatura)
    print(f"\n{criatura.nome} foi enviada para o Santuário!")


