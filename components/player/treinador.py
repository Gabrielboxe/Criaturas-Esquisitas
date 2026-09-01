from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Treinador:
    def __init__(self, nome: str, sexo: Sexo, idade: int, dinheiro: float = 0.0):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.dinheiro = dinheiro
        self.criaturas = []

    def adicionar_criatura_treinador(self, criatura: str):
        self.criaturas.append(criatura)
        print(f"{criatura.nome} foi adicionada a sua equipe!")