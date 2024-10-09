import lm as ep

# Entrada y salida
nombre = ep.entrada("¿Cómo te llamas? ")
ep.imprimir(f"Hola, {nombre}")

# Control de flujo
if ep.si(nombre == "Luis"):
    ep.imprimir("¡Bienvenido, Luis!")
else:
    ep.imprimir("Hola, visitante")

# Operaciones matemáticas
resultado = ep.sumar(5, 3)
ep.imprimir(f"La suma es: {resultado}")

# Bucles
for i in ep.para(5):
    ep.imprimir(f"Contando: {i}")

# Manejo de archivos
ep.escribir_archivo("saludo.txt", "Hola, mundo")
contenido = ep.leer_archivo("saludo.txt")
ep.imprimir(contenido)

# Fechas y tiempos
ep.imprimir(f"Hoy es {ep.hoy()} y la hora actual es {ep.ahora()}")

# Medir tiempo de ejecución
@ep.tiempo_ejecucion
def tarea_pesada():
    ep.esperar(2)

tarea_pesada()
