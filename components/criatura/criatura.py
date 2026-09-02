import random

FATOR_XP_POR_CLASSE = {
        "Abundante": 1.0,
        "Comum": 1.15,
        "Incomum": 1.4,
        "Rara": 1.75,
        "Criticamente Rara": 2.2,
}

FATOR_SPAWN_POR_CLASSE = {
        "Abundante": 1.0,
        "Comum": 0.85,
        "Incomum": 0.6,
        "Rara": 0.4,
        "Criticamente Rara": 0.25,
}


class Criatura:
    def __init__(self, nome: str, hp: int, ataque: int, defesa: int, velocidade: int, energia: int, classe: str = "Comum", biomas = None):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.energia = energia
        self.classe = classe
        self.biomas = biomas or {}

        self.hp_maximo = hp
        self.energia_max = energia

        self.nivel = 1
        self.xp = 0
        self.level_up = 50

    def exibir_status_criatura(self):
        print(f"--==[ {self.nome} ]==--")
        print(f"-- Vida: {self.hp} / {self.hp_maximo}")
        print(f"-- Ataque {self.ataque} | Defesa: {self.defesa}")
        print(f"-- Velocidade: {self.velocidade} | Energia: {self.energia}")
        print(f"-----------------------")

    def obter_peso_spawn(self, bioma: str) -> float:
        afinidade = self.biomas.get(bioma, 0)
        if afinidade == 0:
            return 0.0
        fator = FATOR_SPAWN_POR_CLASSE.get(self.classe, 1.0)
        return afinidade * fator

    def ganhar_xp(self, quantidade: int):
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} de XP!")

        while self.xp >= self.level_up:
            self.xp -= self.level_up
            self._subir_nivel()

    def _subir_nivel(self):
        self.nivel += 1
        self.hp_maximo += 5
        self.ataque += 2
        self.defesa += 2
        self.velocidade += 2
        self.energia_max += 2
        self.hp = self.hp_maximo
        self.level_up = int(self.level_up * 1.2)
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def calcular_xp_recompensa(self) -> int:
        xp_base = (self.hp_maximo + self.ataque + self.defesa + self.velocidade + self.energia_max) // 5
        fator = FATOR_XP_POR_CLASSE.get(self.classe, 1.0)
        variacao = random.uniform(0.9, 1.1)
        return  max(1, round(xp_base * fator *variacao))

