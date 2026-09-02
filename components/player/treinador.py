from enum import Enum
from statistics import quantiles

TAMANHO_MAXIMO_TIME = 3

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Treinador:
    def __init__(self, nome: str, sexo: Sexo, idade: int, dinheiro: float = 0.0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.dinheiro = dinheiro
        self.inventario = {}
        self.missoes = []
        self.time = []
        self.criaturas_capturadas = []
        self.armadilhas_ativas = {}


    def adicionar_criatura_treinador(self, criatura):
        if len(self.time) < TAMANHO_MAXIMO_TIME:
            self.time.append(criatura)
            print(f"{criatura.nome} foi adicionado ao seu time!")
        else:
            self.criaturas_capturadas.append(criatura)
            print(f"Seu time está cheio! {criatura.nome} foi enviada para seu santuário!")

    def adicionar_item(self, nome_item: str, quantidade: int=1):
        self.inventario[nome_item] = self.inventario.get(nome_item, 0) + quantidade
        print(f"Você recebeu {quantidade}x {nome_item}")

    def tem_item(self, nome_item: str) -> bool:
        return self.inventario.get(nome_item, 0) > 0

    def usar_item(self, nome_item: str) -> bool:
        if not self.tem_item(nome_item):
            print(f"Você não tem mais {nome_item}!")
            return False
        self.inventario[nome_item] -= 1
        return True

    def pode_receber_missao(self) -> bool:
        return len(self.missoes) < 3
    