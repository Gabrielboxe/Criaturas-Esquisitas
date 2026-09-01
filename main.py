import random
from components.criatura.criatura import Criatura
from components.player.treinador import Treinador, Sexo
from components.criatura.iniciais import escolher_inicial
from mecanicas.batalha import iniciar_batalha
from criatura.criaturas_selvagens import lista_criaturas_selvagens


def main():
    print("\n==== BEM VINDO AO JOGO ===")
    print("\n== CRIATURAS ESQUISITAS ==")

    # 1. Criação do Personagem
    while True:
        print("\nPor favor escolha seu gênero digitando H ou F")
        escolha_genero = input("Escolha seu gênero: ").upper()

        if escolha_genero == "H":
            jogador = Treinador(nome="Aventureiro", sexo=Sexo.MASCULINO, idade=15)
            break
        elif escolha_genero == "F":
            # CORREÇÃO: Mantido como 'jogador' para não quebrar a função 'escolher_inicial'
            jogador = Treinador(nome="Aventureira", sexo=Sexo.FEMININO, idade=15)
            break
        else:
            print("\nPor favor escolha entre H ou F!")
            continue

    # 2. Escolha do Inicial
    escolher_inicial(jogador)

    # Se a lista estiver vazia (jogador cancelou a escolha), encerra o programa
    if len(jogador.criaturas) == 0:
        print("\nO jogador encerrou o jogo sem escolher um inicial.")
        return

    # 3. Menu Principal (Game Loop de Exploração)
    while True:
        print("\n" + "=" * 30)
        print("--- MENU PRINCIPAL ---")
        print("1 - Explorar o mapa (Batalhar!)")
        print("2 - Ver minha equipe")
        print("3 - Sair do Jogo")
        print("=" * 30)

        acao = input("O que deseja fazer? ")

        if acao == "1":
            funcao_inimigo = random.choice(lista_criaturas_selvagens)
            inimigo = funcao_inimigo()

            aliado = jogador.criaturas[0]

            iniciar_batalha(aliado, inimigo)

            if aliado.hp <= 0:
                print("\nSeu monstro desmaiou! Você correu para o Centro de Cura...")
                aliado.hp = aliado.hp_maximo

        elif acao == "2":
            print(f"\nResumo da equipe de {jogador.nome}:")
            for criatura in jogador.criaturas:
                criatura.exibir_status_criatura()

        elif acao == "3":
            print("\nSalvando aventura... Até a próxima!")
            break

        else:
            print("\nComando inválido!")


if __name__ == "__main__":
    main()