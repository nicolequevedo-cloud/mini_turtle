# Estado global
tiempo_total_acumulado = 0.0


def iniciar_tarea(tarea):
    print(f"Iniciando tarea: {tarea}")


def detener_tarea(tiempo_trabajado):
    global tiempo_total_acumulado
    tiempo_total_acumulado += tiempo_trabajado
    print(f"Tarea detenida. Tiempo trabajado: {tiempo_trabajado} horas")


def consultar_total():
    return tiempo_total_acumulado
