import random

from components.criatura.criatura import Criatura, NIVEL_MAXIMO_CRIATURA

ESPECIES_SELVAGENS = [
    {"nome": "Diabo-Espinhoso", "tipo": "Desértico", "hp": 30, "ataque": 15, "defesa": 35, "velocidade": 10, "energia": 10, "classe": "Abundante", "biomas": {"Deserto": 95}},
    {"nome": "Rato-Toupeira", "tipo": "Subterrâneo", "hp": 40, "ataque": 10, "defesa": 25, "velocidade": 15, "energia": 10, "classe": "Abundante", "biomas": {"Deserto": 60, "Caverna": 30}},
    {"nome": "Peixe-Bruxa", "tipo": "Aquático", "hp": 30, "ataque": 10, "defesa": 30, "velocidade": 10, "energia": 20, "classe": "Abundante", "biomas": {"Oceano": 90}},
    {"nome": "Toupeira-Nariz-de-Estrela", "tipo": "Subterrâneo", "hp": 20, "ataque": 15, "defesa": 15, "velocidade": 35, "energia": 15, "classe": "Abundante", "biomas": {"Pântano": 80, "Floresta": 25}},
    {"nome": "Sapo-Flecha", "tipo": "Anfíbio", "hp": 10, "ataque": 35, "defesa": 5, "velocidade": 30, "energia": 20, "classe": "Comum", "biomas": {"Floresta": 75, "Pântano": 40}},
    {"nome": "Monstro-de-Gila", "tipo": "Desértico", "hp": 25, "ataque": 25, "defesa": 25, "velocidade": 10, "energia": 15, "classe": "Incomum", "biomas": {"Deserto": 85}},
    {"nome": "Peixe-Morcego", "tipo": "Aquático", "hp": 25, "ataque": 10, "defesa": 25, "velocidade": 10, "energia": 30, "classe": "Incomum", "biomas": {"Oceano": 85}},
    {"nome": "Peixe-Diabo", "tipo": "Aquático", "hp": 20, "ataque": 30, "defesa": 10, "velocidade": 15, "energia": 25, "classe": "Incomum", "biomas": {"Oceano": 80}},
    {"nome": "Tartaruga-Aligator", "tipo": "Anfíbio", "hp": 35, "ataque": 30, "defesa": 25, "velocidade": 5, "energia": 5, "classe": "Incomum", "biomas": {"Rio": 65, "Pântano": 45}},
    {"nome": "Olm", "tipo": "Anfíbio", "hp": 30, "ataque": 10, "defesa": 15, "velocidade": 10, "energia": 35, "classe": "Rara", "biomas": {"Caverna": 95}},
    {"nome": "Aye-Aye", "tipo": "Florestal", "hp": 15, "ataque": 25, "defesa": 10, "velocidade": 25, "energia": 25, "classe": "Rara", "biomas": {"Floresta": 90}},
    {"nome": "Rã-Titicaca", "tipo": "Anfíbio", "hp": 35, "ataque": 10, "defesa": 30, "velocidade": 10, "energia": 15, "classe": "Criticamente Rara", "biomas": {"Rio": 60, "Pântano": 30}},
]

BIOMAS_DISPONIVEIS = ["Floresta", "Pântano", "Rio", "Caverna", "Deserto", "Oceano"]

# Tipo de cada espécie conhecida (selvagens + iniciais), usado pelo Diário e por saves antigos.
TIPO_POR_ESPECIE = {especie["nome"]: especie["tipo"] for especie in ESPECIES_SELVAGENS}
TIPO_POR_ESPECIE.update({"Solenodonte": "Florestal", "Ornitorrinco": "Anfíbio", "Poraquê": "Aquático"})


def criar_criatura_selvagem(especie: dict) -> Criatura:
    return Criatura(
        nome=especie["nome"],
        hp=especie["hp"],
        ataque=especie["ataque"],
        defesa=especie["defesa"],
        velocidade=especie["velocidade"],
        energia=especie["energia"],
        classe=especie["classe"],
        biomas=especie["biomas"],
        tipo=especie["tipo"],
    )


def sortear_criatura_selvagem(bioma: str, nivel_maximo: int = NIVEL_MAXIMO_CRIATURA):
    candidatas = []
    pesos = []

    for especie in ESPECIES_SELVAGENS:
        criatura = criar_criatura_selvagem(especie)
        peso = criatura.obter_peso_spawn(bioma)
        if peso > 0:
            candidatas.append(criatura)
            pesos.append(peso)

    if not candidatas:
        return None

    criatura_sorteada = random.choices(candidatas, weights=pesos, k=1)[0]

    teto = max(1, min(nivel_maximo, NIVEL_MAXIMO_CRIATURA))
    nivel_sorteado = random.randint(1, teto)
    criatura_sorteada.aplicar_niveis(nivel_sorteado - 1)

    return criatura_sorteada