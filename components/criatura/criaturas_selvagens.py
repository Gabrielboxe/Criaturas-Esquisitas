from components.criatura.criatura import Criatura
from criatura.criatura import Criatura


def gerar_diabo_espinhoso():
    return Criatura(nome="Diabo-Espinhoso", hp=30, ataque=15, defesa=35, velocidade=10, energia=10, classe="Abundante", biomas={"Deserto": 95})

def gerar_rato_toupeira():
    return Criatura(nome="Rato-Toupeira", hp=40, ataque=10, defesa=25, velocidade=15, energia=10, classe="Abundante", biomas={"Deserto": 60, "Caverna": 30})

def gerar_peixe_bruxa():
    return Criatura(nome="Peixe-Bruxa", hp=30, ataque=10, defesa=30, velocidade=10, energia=20, classe="Abundante", biomas={"Oceano": 90})

def gerar_toupeira_nariz_de_estrela():
    return Criatura(nome="Toupeira-Nariz-de-Estrela", hp=20, ataque=15, defesa=15, velocidade=35, energia=15, classe="Abundante", biomas={"Pântano": 80, "Floresta": 25})

def gerar_sapo_flecha():
    return Criatura(nome="Sapo-Flecha", hp=10, ataque=35, defesa=5, velocidade=30, energia=20, classe="Comum", biomas={"Floresta": 75, "Pântano": 40})

def gerar_monstro_de_gila():
    return Criatura(nome="Monstro-de-Gila", hp=25, ataque=25, defesa=25, velocidade=10, energia=15, classe="Incomum", biomas={"Deserto": 85})

def gerar_peixe_morcego():
    return Criatura(nome="Peixe-Morcego", hp=25, ataque=10, defesa=25, velocidade=10, energia=30, classe="Incomum", biomas={"Oceano": 85})

def gerar_peixe_diabo():
    return Criatura(nome="Peixe-Diabo", hp=20, ataque=30, defesa=10, velocidade=15, energia=25, classe="Incomum", biomas={"Oceano": 80})

def gerar_tartaruga_aligator():
    return Criatura(nome="Tartaruga-Aligator", hp=35, ataque=30, defesa=25, velocidade=5, energia=5, classe="Incomum", biomas={"Rio": 65, "Pântano": 45})

def gerar_olm():
    return Criatura(nome="Olm", hp=30, ataque=10, defesa=15, velocidade=10, energia=35, classe="Rara", biomas={"Caverna": 95})

def gerar_aye_aye():
    return Criatura(nome="Aye-Aye", hp=15, ataque=25, defesa=10, velocidade=25, energia=25, classe="Rara", biomas={"Floresta": 90})

def gerar_ra_titicaca():
    return Criatura(nome="Rã-Titicaca", hp=35, ataque=10, defesa=30, velocidade=10, energia=15, classe="Criticamente Rara", biomas={"Rio": 60, "Pântano": 30})

lista_criaturas_selvagens = [
    gerar_toupeira_nariz_de_estrela, gerar_aye_aye, gerar_olm,
    gerar_sapo_flecha, gerar_peixe_morcego, gerar_ra_titicaca,
    gerar_diabo_espinhoso, gerar_rato_toupeira, gerar_peixe_bruxa,
    gerar_tartaruga_aligator, gerar_peixe_diabo, gerar_monstro_de_gila
]

import random

BIOMAS_DISPONIVEIS = ["Floresta", "Pântano", "Rio", "Caverna", "Deserto", "Oceano"]

def sortear_criatura_selvagem(bioma: str):
    candidatas = []
    pesos = []

    for gerar_func in lista_criaturas_selvagens:
        criatura = gerar_func()
        peso = criatura.obter_peso_spawn(bioma)
        if peso > 0:
            candidatas.append(gerar_func)
            pesos.append(peso)
    if not candidatas:
        return None

    funcao_sorteada = random.choices(candidatas, weights=pesos, k=1)[0]
    return funcao_sorteada()


