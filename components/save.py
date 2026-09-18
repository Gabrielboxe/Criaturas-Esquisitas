import json
import os

from components.criatura.criatura import Criatura
from components.criatura.criaturas_selvagens import TIPO_POR_ESPECIE
from components.mecanicas.missoes import Missao
from components.player.treinador import Treinador, Sexo


def criatura_para_dict(c):
    return {
        "nome": c.nome,
        "hp": c.hp,
        "hp_maximo": c.hp_maximo,
        "ataque": c.ataque,
        "defesa": c.defesa,
        "velocidade": c.velocidade,
        "energia": c.energia,
        "energia_max": c.energia_max,
        "classe": c.classe,
        "tipo": c.tipo,
        "biomas": c.biomas,
        "nivel": c.nivel,
        "xp": c.xp,
        "level_up": c.level_up,
    }


def criatura_de_dict(d):
    criatura = Criatura(
        nome=d["nome"],
        hp=d["hp_maximo"],
        ataque=d["ataque"],
        defesa=d["defesa"],
        velocidade=d["velocidade"],
        energia=d["energia_max"],
        classe=d["classe"],
        biomas=d["biomas"],
        tipo=d.get("tipo") or TIPO_POR_ESPECIE.get(d["nome"], "Desconhecido"),
    )
    criatura.hp = d["hp"]
    criatura.energia = d["energia"]
    criatura.nivel = d["nivel"]
    criatura.xp = d["xp"]
    criatura.level_up = d["level_up"]
    return criatura


def salvar_jogo(jogador, caminho: str = "save.json"):
    dados = {
        "nome": jogador.nome,
        "sexo": jogador.sexo.value,
        "idade": jogador.idade,
        "dinheiro": jogador.dinheiro,
        "inventario": jogador.inventario,
        "diario": jogador.diario,
        "time": [criatura_para_dict(c) for c in jogador.time],
        "criaturas_capturadas": [criatura_para_dict(c) for c in jogador.criaturas_capturadas],
        "armadilhas_ativas": {
            bioma: {
                "tipo": armadilha["tipo"],
                "criatura": criatura_para_dict(armadilha["criatura"]),
                "pronta": armadilha["pronta"],
            }
            for bioma, armadilha in jogador.armadilhas_ativas.items()
        },
        "missoes": [
            {
                "bioma": m.bioma,
                "criatura_alvo": criatura_para_dict(m.criatura_alvo),
                "recompensa": m.recompensa,
                "concluida": m.concluida,
            }
            for m in jogador.missoes
        ],
    }

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)

    print(f"\nProgresso salvo em '{caminho}'!")


def carregar_jogo(caminho: str = "save.json"):
    if not os.path.exists(caminho):
        return None

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    sexo = Sexo(dados["sexo"])
    jogador = Treinador(nome=dados["nome"], sexo=sexo, idade=dados["idade"], dinheiro=dados["dinheiro"])
    jogador.inventario = dados["inventario"]
    jogador.diario = dados["diario"]

    jogador.time = [criatura_de_dict(d) for d in dados["time"]]
    jogador.criaturas_capturadas = [criatura_de_dict(d) for d in dados["criaturas_capturadas"]]

    jogador.armadilhas_ativas = {
        bioma: {
            "tipo": armadilha["tipo"],
            "criatura": criatura_de_dict(armadilha["criatura"]),
            "pronta": armadilha["pronta"],
        }
        for bioma, armadilha in dados["armadilhas_ativas"].items()
    }

    jogador.missoes = []
    for m in dados["missoes"]:
        missao = Missao(bioma=m["bioma"], criatura_alvo=criatura_de_dict(m["criatura_alvo"]))
        missao.recompensa = m["recompensa"]
        missao.concluida = m["concluida"]
        jogador.missoes.append(missao)

    print(f"\nProgresso carregado de '{caminho}'!")
    return jogador