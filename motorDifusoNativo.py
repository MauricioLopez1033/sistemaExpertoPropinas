import numpy as np

def funcionTriangular (x, a, b, c):
      return np.maximum(0, np.minimum((x-a)/(b-a + 1e-9), (c-x)/(c-b + 1e-9)))

def evaluarSistemaExpertoPropina(calidadComida, calidadServicio):
    xComida = np.linspace(0, 10, 101)
    xServicio = np.linspace(0, 10, 101)
    yPropina = np.linspace(0, 25, 251)

    comidaMala = funcionTriangular(calidadComida, 0, 0, 5)
    comidaAceptable = funcionTriangular(calidadComida, 2, 5, 8)
    comidaExcelente = funcionTriangular(calidadComida, 5, 10, 10)
    
    servicioPobre = funcionTriangular(calidadServicio, 0, 0, 5)
    servicioBueno = funcionTriangular(calidadServicio, 2, 5, 8)
    servicioExcelente = funcionTriangular(calidadServicio, 5, 10, 10)

    muPropinaBaja = funcionTriangular(yPropina, 0, 0, 10)
    muPropinaMedia = funcionTriangular(yPropina, 8, 15, 20)
    muPropinaAlta = funcionTriangular(yPropina, 15, 25, 25)

    r1 = min(comidaMala, servicioPobre)
    r2 = min(comidaMala, servicioBueno)
    r3 = min(comidaMala, servicioExcelente)
    r4 = min(comidaAceptable, servicioPobre)
    r5 = min(comidaAceptable, servicioBueno)
    r6 = min(comidaAceptable, servicioExcelente)
    r7 = min(comidaExcelente, servicioPobre)
    r8 = min(comidaExcelente, servicioBueno)
    r9 = min(comidaExcelente, servicioExcelente)

    cBaja = np.maximum.reduce([np.minimum(r1, muPropinaBaja), np.minimum(r2, muPropinaBaja), np.minimum(r4, muPropinaBaja)])
    cMedia = np.maximum.reduce([np.minimum(r3, muPropinaMedia), np.minimum(r5, muPropinaMedia), np.minimum(r7, muPropinaMedia)])
    cAlta = np.maximum.reduce([np.minimum(r6, muPropinaAlta), np.minimum(r8, muPropinaAlta), np.minimum(r9, muPropinaAlta)])

    curvaAgregada = np.maximum.reduce([cBaja, cMedia, cAlta])

    numerador = np.sum(yPropina * curvaAgregada)
    denominador = np.sum(curvaAgregada)

    if denominador == 0:
         propinaCrisp = 12.5
    else:
         propinaCrisp = numerador / denominador

    if propinaCrisp <= 10:
      nivelPropina = "Propina Baja"
    elif propinaCrisp <= 18:
      nivelPropina = "Propina Media"
    else:
      nivelPropina = "Propina Alta"

    return round(float(propinaCrisp), 2), nivelPropina 