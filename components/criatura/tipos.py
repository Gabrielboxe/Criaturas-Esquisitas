# Sistema de tipos: cada tipo tem vantagem sobre exatamente um outro, formando um ciclo.
#
#   Aquático > Desértico > Florestal > Anfíbio > Subterrâneo > Aquático
#
# Aquático vence Desértico   (a água apaga o calor seco)
# Desértico vence Florestal  (a seca sufoca a mata)
# Florestal vence Anfíbio    (os predadores da mata caçam na margem)
# Anfíbio vence Subterrâneo  (o charco alaga as tocas)
# Subterrâneo vence Aquático (a terra e a lama barram a água)

TIPOS = ["Aquático", "Desértico", "Florestal", "Anfíbio", "Subterrâneo"]

VANTAGENS = {
    "Aquático": "Desértico",
    "Desértico": "Florestal",
    "Florestal": "Anfíbio",
    "Anfíbio": "Subterrâneo",
    "Subterrâneo": "Aquático",
}

MULTIPLICADOR_VANTAGEM = 1.5
MULTIPLICADOR_DESVANTAGEM = 0.5


def multiplicador_tipo(tipo_atacante: str, tipo_defensor: str) -> float:
    if VANTAGENS.get(tipo_atacante) == tipo_defensor:
        return MULTIPLICADOR_VANTAGEM
    if VANTAGENS.get(tipo_defensor) == tipo_atacante:
        return MULTIPLICADOR_DESVANTAGEM
    return 1.0


def descrever_efetividade(multiplicador: float) -> str:
    if multiplicador > 1.0:
        return "É super efetivo!"
    if multiplicador < 1.0:
        return "Não é muito efetivo..."
    return ""


def fraqueza_de(tipo: str) -> str:
    """Retorna o tipo que tem vantagem sobre o tipo informado."""
    for atacante, alvo in VANTAGENS.items():
        if alvo == tipo:
            return atacante
    return "?"
