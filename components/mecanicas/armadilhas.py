import random

from components.criatura.criatura import FATOR_SPAWN_POR_CLASSE

CHANCE_BASE_ARMADILHA = {
    "Armadilha Velha": 0.30,
    "Armadilha Boa": 0.55,
    "Armadilha Especial": 0.75,
}

BONUS_RARO_ARMADILHA = {
    "Armadilha Velha": 0.0,
    "Armadilha Boa": 0.10,
    "Armadilha Especial": 0.20,
}

CLASSES_RARAS = {"Rara", "Criticamente Rara"}

def calcular_chance_captura(nome_armadilha, criatura):
    fator_spawn = FATOR_SPAWN_POR_CLASSE.get(criatura.classe, 1.0)
    chance = CHANCE_BASE_ARMADILHA.get(nome_armadilha, 0.0) * fator_spawn

    if criatura.classe in CLASSES_RARAS:
        chance += BONUS_RARO_ARMADILHA.get(nome_armadilha, 0.0)

    return min(chance, 0.95)

def tentar_capturar(nome_armadilha, criatura):
    chance = calcular_chance_captura(nome_armadilha, criatura)
    return random.random() <= chance