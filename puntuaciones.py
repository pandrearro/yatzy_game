class PuntuacionesYatzy:
    def puntuaciones_uno(self, mano):
        return sum(mano.unos)

    def puntuaciones_doss(self, mano):
        return sum(mano.doss)

    def puntuaciones_tress(self, mano):
        return sum(mano.tress)

    def puntuaciones_cuatros(self, mano):
        return sum(mano.cuatros)

    def puntuaciones_cincos(self, mano):
        return sum(mano.cincos)

    def puntuaciones_seises(self, mano):
        return sum(mano.seises)

    def _puntar_set(self, mano, tamano_set):
        puntos = [0]
        for valor, cuenta in mano.sets.items():
            if cuenta == tamano_set:
                puntos.append(valor*tamano_set)
        return max(puntos)
