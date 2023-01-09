from hora import obtener_hora_actual
from ventana import variable_hora_actual


def refrescar_reloj():
    print("Refrescando!")
    variable_hora_actual.set(obtener_hora_actual())
    raiz.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)