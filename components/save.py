import json
import os
from components.player.treinador import Treinador, Sexo
from components.criatura.criatura import Criatura
from criatura import criatura

def carregar_jogo(caminho="save.json"):
    if not os.path.exists(caminho):
        return None

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    sexo = Sexo(dados["sexo"])
    jogador = Treinador(nome=dados["nome"], sexo=sexo, idade=dados["idade"], dinheiro=dados["dinheiro"])
    jogador.inventario = dados["inventario"]

    for dados_criatura in dados["criaturas"]:
        criatura = Criatura(
            nome=dados_criatura["nome"],
            hp=dados_criatura["hp_maximo"],
            ataque=dados_criatura["ataque"],
            defesa=dados_criatura["defesa"],
            velocidade=dados_criatura["velocidade"],
            energia=dados_criatura["energia_max"],
            classe=dados_criatura["classe"],
            biomas=dados_criatura["biomas"],
        )
        criatura.hp = dados_criatura["hp"]
        criatura.energia = dados_criatura["energia"]
        criatura.nivel = dados_criatura["nivel"]
        criatura.xp = dados_criatura["xp"]
        criatura.level_up = dados_criatura["level_up"]
        jogador.adicionar_criatura_treinador(criatura)

    print(f"\nProgresso carregado de '{caminho}'!")
    return jogador


def salvar_jogo(jogador, caminho="save.json"):
    dados = {
        "nome": jogador.nome,
        "sexo": jogador.sexo.value,
        "idade": jogador.idade,
        "dinheiro": jogador.dinheiro,
        "inventario": jogador.inventario,
        "criaturas": [
            {
                "nome": c.nome,
                "hp": c.hp,
                "hp_maximo": c.hp_maximo,
                "ataque": c.ataque,
                "defesa": c.defesa,
                "velocidade": c.velocidade,
                "energia": c.energia,
                "energia_max": c.energia_max,
                "classe": c.classe,
                "biomas": c.biomas,
                "nivel": c.nivel,
                "xp": c.xp,
                "level_up": c.level_up,
            }
            for c in jogador.time
        ],
    }

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

    print(f"\nProgresso salvo em {caminho}!")