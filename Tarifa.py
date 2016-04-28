from decimal import *

class Tarifa:
    precioSemana
    precioFindeSemana
    
    def __init__(self,semanal,finesdeSemana):
        self.precioSemana = Decimal(semanal)
        self.precioFindeSemana = Decimal(finesdeSemana)
    
    def precioDiaSemana(self):
        return self.precioSemana
    
    def precioDiaFinSemana(self):
        return self.precioFindeSemana