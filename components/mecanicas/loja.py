ITENS_LOJA = {
    "Injeção": {"preco": 50, "limite": 10},
    "Armadilha Velha": {"preco": 300, "limite": 3},
    "Armadilha Boa": {"preco": 500, "limite": 3},
    "Armadilha Especial": {"preco": 800, "limite": 3},
}

NOMES_ARMADILHAS = ["Armadilha velha", "Armadilha Boa", "Armadilha Especial"]

def menu_loja(jogador):
    while True:
        print("\n--- LOJA ---")
        print(f"Dinheiro: ${jogador.dinheiro}")
        itens = list(ITENS_LOJA.items())
        for i, (nome, info) in enumerate(itens, start=1):
            quantidade_atual = jogador.inventario.get(nome, 0)
            print(f"{i} - {nome} - (${info['preco']}) | Você tem: {quantidade_atual}/{info['limite']}")
        print(f"{len(itens) + 1} - Sair da loja")

        escolha = input("O que deseja comprar? ")
        try:
            escolha = int(escolha)
        except ValueError:
            print("\nComando inválido!")
            continue

        if escolha == len(itens) + 1:
            return
        if not (1 <= escolha <= len(itens)):
            print("\nComando inválido!")
            continue

        nome_item, info = itens[escolha - 1]
        quantidade_atual = jogador.inventario.get(nome_item, 0)

        if quantidade_atual >= info["limite"]:
            print(f"\nVocê já possui o máximo de {nome.item} (Qtde: {info['limite']})")
            continue
        if jogador.dinheiro < info["preco"]:
            print(f"Você não tem dinheiro suficiente! (Saldo: ${jogador.dinheiro})")
            continue

        jogador.dinheiro -= info["preco"]
        jogador.adicionar_item(nome_item, 1)
        print(f"\nVocê comprou 1x {nome_item}!")




