def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        nivel = "Alto"
    elif duracion < 60 or clics < 3:
        nivel = "Bajo"
    else:
        nivel = "Medio"
    return nivel


def leer_numero_entero(mensaje):
    texto = input(mensaje)
    while not texto.isdecimal():
        print("  Valor no válido. Ingrese un número entero sin decimales ni letras.")
        texto = input(mensaje)
    return int(texto)


nueva_prueba = "s"

while nueva_prueba == "s":
    print()
    print("1. Usar datos de prueba")
    print("2. Ingresar sesiones manualmente")
    opcion = input("Elija una opción: ")

    while opcion != "1" and opcion != "2":
        opcion = input("Opción no válida. Elija 1 o 2: ")

    if opcion == "1":
        sesiones = [
            ["1", 240, 12],
            ["2", 45, 10],
            ["3", 120, 5],
            ["4", 300, 2],
            ["5", 180, 12]
        ]
    else:
        sesiones = []
        cantidad_sesiones = leer_numero_entero("¿Cuántas sesiones desea ingresar? (mínimo 5): ")
        while cantidad_sesiones < 5:
            cantidad_sesiones = leer_numero_entero("Debe ingresar al menos 5 sesiones: ")
        for i in range(cantidad_sesiones):
            print()
            print("--- Sesión", i + 1, "de", cantidad_sesiones, "---")
            id_cliente = input("  ID del cliente: ")
            duracion = leer_numero_entero("  Duración en segundos: ")
            clics = leer_numero_entero("  Número de clics: ")
            sesiones.append([id_cliente, duracion, clics])

    print()
    print("MATRIZ DE SESIONES")
    print("ID\t\tDuración (s)\tClics")
    i = 0
    while i < len(sesiones):
        print(sesiones[i][0], sesiones[i][1], sesiones[i][2], sep="\t\t")
        i = i + 1

    print()
    print("INFORME DE COMPROMISO")
    i = 0
    while i < len(sesiones):
        id_cliente = sesiones[i][0]
        duracion = sesiones[i][1]
        clics = sesiones[i][2]
        nivel = clasificar_compromiso(duracion, clics)
        print("ID:", id_cliente, "| Clasificación:", nivel)
        i = i + 1

    print()
    nueva_prueba = input("¿Desea hacer una nueva prueba? (s/n): ")
    while nueva_prueba != "s" and nueva_prueba != "n":
        nueva_prueba = input("Respuesta no válida. Escriba s o n: ")

print("Programa finalizado")
