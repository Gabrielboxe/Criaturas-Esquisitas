import os
import sys
import json
from components.criatura.iniciais import escolher_inicial
from components.player.treinador import Treinador, Sexo
from components.mecanicas.acoes import menu_explorar, menu_missoes, menu_equipe
from components.save import salvar_jogo, carregar_jogo

jogador = None

if os.path.exists("save.json"):
    resposta = input("Foi encontrado um save. Deseja carregar? (S/N): ").strip().upper()
    if resposta == "S":
        jogador = carregar_jogo()

if jogador is None:
    while True:
        nome_jogador = input("Digite o nome do seu personagem (máx. 12 caracteres): ").strip()
        if not nome_jogador:
            print("O nome não pode ser vazio.")
            continue
        if len(nome_jogador) > 12:
            print("O nome deve ter no máximo 12 caracteres.")
            continue
        break

    while True:
        escolha_sexo = input("Escolha o sexo do personagem (H/F): ").strip().upper()
        if escolha_sexo == "H":
            sexo_jogador = Sexo.MASCULINO
            break
        elif escolha_sexo == "F":
            sexo_jogador = Sexo.FEMININO
            break
        else:
            print("Opção inválida. Digite H ou F.")

    jogador = Treinador(nome=nome_jogador, sexo=sexo_jogador, idade=16)

    escolher_inicial(jogador)

    if not jogador.time:
        print("\nVocê saiu da escolha de criatura inicial.")
        sys.exit()

    jogador.dinheiro = 200
    jogador.adicionar_item("Injeção", 3)

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Explorar")
    print("2 - Ver equipe")
    print("3 - Ver inventário")
    print("4 - Salvar Jogo")
    print("5 - Sair")

    acao = input("Escolha uma opção: ")

    if acao == "1":
        menu_explorar(jogador)

    elif acao == "2":
        menu_equipe(jogador)

    elif acao == "3":
        print(f"\n--- INVENTÁRIO --- (Dinheiro: ${jogador.dinheiro})")
        for item, qtd in jogador.inventario.items():
            print(f"{item}: {qtd}")

    elif acao == "4":
        salvar_jogo(jogador)
        print("Jogo salvo com sucesso!")

    elif acao == "5":
        print("Até a próxima!")
        break

    else:
        print("Opção inválida.")