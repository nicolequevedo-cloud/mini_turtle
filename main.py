from mini_tracker import iniciar_tarea, detener_tarea, consultar_total

iniciar_tarea("Estudiar Python")
detener_tarea(2.5)

iniciar_tarea("Hacer tarea")
detener_tarea(1.5)

print(f"Tiempo total trabajado: {consultar_total()} horas")
