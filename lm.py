# Archivo: espapy.py

import math
import time

# Funciones básicas de E/S
def imprimir(texto):
    print(texto)

def entrada(texto):
    return input(texto)

# Control de flujo
def si(condicion):
    return condicion

def sino():
    pass

# Ciclos
def para(rango):
    for i in range(rango):
        yield i

def mientras(condicion):
    while condicion:
        yield

# Funciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    return math.sqrt(a)

# Funciones de cadenas
def longitud(texto):
    return len(texto)

def mayusculas(texto):
    return texto.upper()

def minusculas(texto):
    return texto.lower()

def reemplazar(texto, viejo, nuevo):
    return texto.replace(viejo, nuevo)

# Listas
def agregar(lista, elemento):
    lista.append(elemento)

def remover(lista, elemento):
    lista.remove(elemento)

def ordenar(lista):
    lista.sort()

# Manejo de archivos
def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return archivo.read()

# Fechas y tiempo
def hoy():
    return time.strftime("%d/%m/%Y")

def ahora():
    return time.strftime("%H:%M:%S")

def esperar(segundos):
    time.sleep(segundos)

# Manejo de excepciones
def intentar(codigo, manejar_error):
    try:
        codigo()
    except Exception as e:
        manejar_error(e)

# Decoradores
def tiempo_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        imprimir(f"Tiempo de ejecución: {fin - inicio} segundos")
        return resultado
    return wrapper
