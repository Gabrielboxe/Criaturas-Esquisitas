class Criatura:
    def __init__(self, nome: str, hp: int, ataque: int, defesa: int, velocidade: int, energia: int):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.energia = energia

        self.hp_maximo = hp
        self.energia_max = energia

    def exibir_status_criatura(self):
        print(f"--==[ {self.nome} ]==--")
        print(f"-- Vida: {self.hp} / {self.hp_maximo}")
        print(f"-- Ataque {self.ataque} | Defesa: {self.defesa}")
        print(f"-- Velocidade: {self.velocidade} | Energia: {self.energia}")
        print(f"-----------------------")