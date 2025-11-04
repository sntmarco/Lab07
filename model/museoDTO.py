from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Museo
'''

@dataclass()
class Museo:
    id: int
    nome: str
    tipologia: str

    def __eq__(self, other):
        return isinstance(other, Museo) and self.nome == other.nome

    def __str__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia}"
