import random
from components.criatura.criatura import Criatura
from components.player.treinador import Treinador, Sexo
from components.criatura.iniciais import escolher_inicial
from components.mecanicas.batalha import iniciar_batalha
from components.criatura.criaturas_selvagens import lista_criaturas_selvagens
from criatura.criaturas_selvagens import BIOMAS_DISPONIVEIS, sortear_criatura_selvagem


def main():
    print("\n==== BEM VINDO AO JOGO ===")
    print("\n== CRIATURAS ESQUISITAS ==")

    while True:
        print("\nPor favor escolha seu gênero digitando H ou F")
        escolha_genero = input("Escolha seu gênero: ").upper()

        if escolha_genero == "H":
            jogador = Treinador(nome="Aventureiro", sexo=Sexo.MASCULINO, idade=15)
            break
        elif escolha_genero == "F":
            jogador = Treinador(nome="Aventureira", sexo=Sexo.FEMININO, idade=15)
            break
        else:
            print("\nPor favor escolha entre H ou F!")
            continue

    escolher_inicial(jogador)
    jogador.adicionar_item("Poção de Cura", 3)
    jogador.adicionar_item("Isca", 0)

    if len(jogador.criaturas) == 0:
        print("\nO jogador encerrou o jogo sem escolher um inicial.")
        return

    while True:
        print("\n" + "=" * 30)
        print("--- MENU PRINCIPAL ---")
        print("1 - Explorar o mapa (Batalhar!)")
        print("2 - Ver minha Equipe")
        print("3 - Ver Inventario")
        print("4 - Sair do Jogo")
        print("=" * 30)

        acao = input("O que deseja fazer? ")

        if acao == "1":
            print("\nEscolha o bioma para explorar:")
            for i, bioma in enumerate(BIOMAS_DISPONIVEIS, start=1):
                print(f"{i} - {bioma}")

            escolha_bioma = input("Bioma: ")
            try:
                bioma_escolhido = BIOMAS_DISPONIVEIS[int(escolha_bioma) - 1]
            except (ValueError, IndexError):
                print("\nBioma inválido!")
                continue
            inimigo = sortear_criatura_selvagem(bioma_escolhido)
            if inimigo is None:
                print(f"\nNenhuma criatura encontrada em {bioma_escolhido} dessa vez...")
                continue

            aliado = jogador.criaturas[0]
            iniciar_batalha(aliado, inimigo, jogador)

            if aliado.hp <= 0:
                print("\nSeu monstro desmaiou! Você correu para o Centro de Cura...")
                aliado.hp = aliado.hp_maximo

        elif acao == "2":
            print(f"\nResumo da equipe de {jogador.nome}:")
            for criatura in jogador.criaturas:
                criatura.exibir_status_criatura()

        elif acao == "3":
            print(f"\nInventário de {jogador.nome}:")
            if not jogador.inventario:
                print("vazio")
            else:
                for item, qtd in jogador.inventario.items():
                    print(f"{item}: {qtd}")

        elif acao == "4":
            print(f"\nSalvando aventura... Até a próxima!")
            break

        else:
            print("\nComando inválido!")


if __name__ == "__main__":
    main()