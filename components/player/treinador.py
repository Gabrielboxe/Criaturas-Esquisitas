from enum import Enum

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
        self.diario = {}


    def adicionar_criatura_treinador(self, criatura):
        if self.possui_especie(criatura.nome):
            print(f"Você já possui um(a) {criatura.nome}! Soltando ela na natureza...")
            return

        self.registrar_captura_diario(criatura.nome)

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

    def nivel_pesquisa(self, nome_especie: str) -> int:
        registro = self.diario.get(nome_especie, {"capturada": False, "derrotada": False})
        return int(registro["capturada"]) + int(registro["derrotada"])

    def registrar_derrota_diario(self, nome_especie: str):
        registro = self.diario.setdefault(nome_especie, {"capturada": False, "derrotada": False})
        if not registro["derrotada"]:
            registro["derrotada"] = True
            print(f"\n[Diário] {nome_especie} derrotado! Nível de pesquisa progrediu: {self.nivel_pesquisa(nome_especie)}")

    def registrar_captura_diario(self, nome_especie: str):
        registro = self.diario.setdefault(nome_especie, {"capturada": False, "derrotada": False})
        if not registro["capturada"]:
            registro["capturada"] = True
            print(
                f"\n[Diário] {nome_especie} capturada! Nível de pesquisa progrediu: {self.nivel_pesquisa(nome_especie)}")

    def possui_especie(self, nome_especie: str) -> bool:
        no_time = any(c.nome == nome_especie for c in self.time)
        no_santuario = any(c.nome == nome_especie for c in self.criaturas_capturadas)
        return no_time or no_santuario