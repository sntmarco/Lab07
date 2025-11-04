from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Artefatto
'''

@dataclass()
class Artefatto:
    id: int
    nome: str
    tipologia: str
    epoca: str
    id_museo: str

    def __eq__(self, other):
        return isinstance(other, Artefatto) and self.nome == other.nome and self.epoca == other.epoca

    def __str__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia} | Epoca: {self.epoca} | Museo: {self.id_museo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia} | Epoca: {self.epoca} | Museo: {self.id_museo}"

    def __lt__(self, other):
        return self.nome < other.nome