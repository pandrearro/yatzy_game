import random


class Dado:

    def __init__(self, lados=2, valor=0):
        if not lados >= 2:
            raise ValueError("Debe tener al menos 2 lados")
        if not isinstance(lados, int):
            raise ValueError("Los lados deben ser un numero entero")
        self.valor = valor or random.randint(1, lados)

    def __int__(self):
        return self.valor

    def __eq__(self, otro):
        return int(self) == otro

    def __ne__(self, otro):
        return int(self) != otro

    def __gt__(self, otro):
        return int(self) > otro

    def __lt__(self, otro):
        return int(self) < otro

    def __ge__(self, otro):
        return int(self) > otro or int(self) == otro

    def __le__(self, otro):
        return int(self) < otro or int(self) == otro

    def __add__(self, otro):
        return int(self) + otro

    def __radd__(self, otro):
        return int(self) + otro

    def __repr__(self):
        return str(self.valor)


class D6(Dado):
    def __init__(self, valor=0):
        super().__init__(lados=6, valor=valor)
