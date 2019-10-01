from dados import D6


class Mano(list):
    def __init__(self, tamano=0, clase_dado=None, *args, **kwargs):
        if not clase_dado:
            raise ValueError("¿Que dados quieres?")
        super().__init__()

        for _ in range(tamano):
            self.append(clase_dado())
        self.sort()

    def _por_valor(self, valor):
        dados = []
        for dado in self:
            if dado == valor:
                dados.append(dado)
        return dados


class ManoYatzy(Mano):
    def __init__(self, *args, **kwargs):
        super().__init__(tamano=5, clase_dado=D6, *args, **kwargs)

    @property
    def unos(self):
        return self._por_valor(1)

    @property
    def doss(self):
        return self._por_valor(2)

    @property
    def tress(self):
        return self._por_valor(3)

    @property
    def cuatros(self):
        return self._por_valor(4)

    @property
    def cincos(self):
        return self._por_valor(5)

    @property
    def seises(self):
        return self._por_valor(6)

    @property
    def _sets(self):
        return{
            1: len(self.unos),
            2: len(self.doss),
            3: len(self.tress),
            4: len(self.cuatros),
            5: len(self.cincos),
            6: len(self.seises)
        }
