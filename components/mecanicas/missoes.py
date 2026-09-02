import random
import components.criatura.criaturas_selvagens
from components.criatura.criatura import FATOR_XP_POR_CLASSE
from criatura.criaturas_selvagens import BIOMAS_DISPONIVEIS, sortear_criatura_selvagem

MULTIPLICADOR_DINHEIRO = 4

class Missao:
    def __init__(self, bioma: str, criatura_alvo):
        self.bioma = bioma
        self.criatura_alvo = criatura_alvo
        self.recompensa = calcular_recompensa_missao(criatura_alvo)
        self.concluida = False

    def descricao(self) -> str:
        return f"Derrote {self.criatura_alvo.nome} em {self.bioma} - recompensa: ${self.recompensa}"


def calcular_recompensa_missao(criatura) -> int:
    base = (criatura.hp_maximo + criatura.ataque + criatura.defesa + criatura.velocidade + criatura.energia_max) // 5
    fator = FATOR_XP_POR_CLASSE.get(criatura.classe, 1.0)
    variacao = random.uniform(0.9, 1.1)
    return max(1, round(base * fator * MULTIPLICADOR_DINHEIRO * variacao))

def gerar_missao():
    bioma = random.choice(BIOMAS_DISPONIVEIS)
    criatura_alvo = sortear_criatura_selvagem(bioma)

    if criatura_alvo is None:
        return None

    return Missao(bioma, criatura_alvo)