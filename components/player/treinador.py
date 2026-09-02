from enum import Enum
from statistics import quantiles


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
        self.criaturas = []

    def adicionar_criatura_treinador(self, criatura: str):
        self.criaturas.append(criatura)
        print(f"{criatura.nome} foi adicionada a sua equipe!")

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


















