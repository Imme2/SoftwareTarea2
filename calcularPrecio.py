from decimal import *
from datetime import *
from Tarifa import *

def calcularPrecio(tarifa, tiempoDeTrabajo):
    
    precioSemana = tarifa.getPrecio()
    precioFindeSemana = tarifa.getPrecio()
        
    if (tiempoDeTrabajo[0] < tiempoDeTrabajo[1]):
        raise ValueError('Tiempo de trabajo negativo!',tiempoDeTrabajo[0],tiempoDeTrabajo[1])
    
    
    aux = (tiempoDeTrabajo[0] - tiempoDeTrabajo[1])
    
    if (aux.day == 0 and aux.year == 0):
        pass
    
        
        
        
    
    