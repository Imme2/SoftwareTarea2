from decimal import *
from datetime import *
from Tarifa import *

def calcularPrecio(tarifa, tiempoDeTrabajo):
    
    precioSemana = tarifa.getPrecio()
    precioFindeSemana = tarifa.getPrecio()
        
        
    #Chequeamos que los valores sean validos.
    if (precioSemana < 0):
        raise ValueError('La tarifa de la semana no debe ser negativa',precioSemana)
    
    if (precioFindeSemana < 0):
        raise ValueError('La tarifa del fin de semana no debe ser negativa',precioFindeSemana)
    
    if (tiempoDeTrabajo[0] < tiempoDeTrabajo[1]):
        raise ValueError('Tiempo de trabajo negativo!',tiempoDeTrabajo[0],tiempoDeTrabajo[1])
    
    aux = (tiempoDeTrabajo[1] - tiempoDeTrabajo[0])
    
    if (aux.day == 0 and aux.year == 0 and aux.month == 0 and aux.hour == 0 and aux.minute < 15):
        raise ValueError('Tiempo de trabajo menor a 15 minutos!',tiempoDeTrabajo[0],tiempoDeTrabajo[1])
    
    if (aux.day > 7 or (aux.day == 7 and aux.hour > 0)):
        raise ValueError('El Tiempo de trabajo debe ser menor a 7 dias',tiempoDeTrabajo[0],tiempoDeTrabajo[1])
    
    #Inicializamos valores para el ciclo
    aux = tiempoDeTrabajo[0]
    aux2 = timedelta(hours=1)
    prevDay = 0
    tarifa = Decimal(0)
    
    
    while (aux < tiempoDeTrabajo[1]):
        
        #Se suman las tarifas en caso de ser cualquier dia (0 siendo lunes, 6 siendo domingo)
        if (aux.weekday < 5):
            tarifa += precioSemana
        else:
            tarifa += precioFindeSemana


        # Estos proximos ifs implementan el cambio de precio cuando se va de un dia de semana
        # a uno que es fin de semana y viceversa           
        if (prevDay == 6 and aux.weekday == 0):
            tarifa += precioSemana
        elif (prevDay == 4 and aux.weekday == 5):
            tarifa += precioFindeSemana
        
        prevDay = aux.weekday
        aux += aux2
    
    return tarifa