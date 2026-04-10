import time
import random

N = 100000  # número de fincas


# ----------------------------
# 1. LISTA TRADICIONAL
# ----------------------------
inicio = time.time()

lista_tradicional = []
for _ in range(N):
    lista_tradicional.append(random.randint(50, 500))

total_tradicional = sum(lista_tradicional) * 1.10

fin = time.time()
tiempo_tradicional = fin - inicio

print("=== LISTA TRADICIONAL ===")
print("Total:", total_tradicional)
print("Tiempo:", tiempo_tradicional)
print()


# ----------------------------
# 2. LISTA CON COMPRENSIÓN
# ----------------------------
inicio = time.time()

lista_comprension = [random.randint(50, 500) for _ in range(N)]

total_comprension = sum(lista_comprension) * 1.10

fin = time.time()
tiempo_comprension = fin - inicio

print("=== LIST COMPREHENSION ===")
print("Total:", total_comprension)
print("Tiempo:", tiempo_comprension)
print()


# ----------------------------
# 3. GENERADOR
# ----------------------------
def generador_abono(n):
    for _ in range(n):
        yield random.randint(50, 500)


inicio = time.time()

total_generador = sum(generador_abono(N)) * 1.10

fin = time.time()
tiempo_generador = fin - inicio

print("=== GENERADOR ===")
print("Total:", total_generador)
print("Tiempo:", tiempo_generador)
print()