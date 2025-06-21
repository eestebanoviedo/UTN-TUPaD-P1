import random
import time

# Solicita al usuario la cantidad de números a generar.
# Retorna una lista de números únicos, desordenada.
def generar_lista():
    while True:
        try:
            cantidad = int(input("¿Cuántos números querés generar?: "))
            if cantidad > 0:
                break
            print("Ingresá un número mayor a 0.")
        except ValueError:
            print("Ingresá un número válido.")
    return random.sample(range(1, cantidad + 1), cantidad)

# Algoritmos de ordenamiento

# Ordenamiento Burbuja: compara elementos adyacentes e intercambia si están desordenados
def ordenamiento_burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ordenamiento por Selección: busca el mínimo y lo mueve a su lugar correcto
def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

# Ordenamiento por Inserción: inserta cada elemento en su posición correcta
def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor

# QuickSort: algoritmo recursivo eficiente basado en dividir y conquistar
def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return ordenamiento_rapido(menores) + [pivote] + ordenamiento_rapido(mayores)

# Algoritmos de búsqueda

# Búsqueda Lineal: recorre la lista secuencialmente hasta encontrar el valor
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Búsqueda Binaria: requiere lista ordenada; divide y busca en mitades
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Aplica el método de ordenamiento indicado, luego realiza búsquedas
# Mide los tiempos de ejecución de cada paso
def ordenar_y_buscar(metodo, lista, objetivo):
    copia = lista.copy()  # Evitar modificar la lista original

    inicio = time.perf_counter()  # Tiempo inicial

    if metodo == 'burbuja':
        ordenamiento_burbuja(copia)
    elif metodo == 'insercion':
        ordenamiento_insercion(copia)
    elif metodo == 'seleccion':
        ordenamiento_seleccion(copia)
    elif metodo == 'rapido':
        copia = ordenamiento_rapido(copia)

    tiempo_ordenar = time.perf_counter()

    pos_lineal = busqueda_lineal(copia, objetivo)
    tiempo_lineal = time.perf_counter()

    pos_binaria = busqueda_binaria(copia, objetivo)
    tiempo_binaria = time.perf_counter()

    return {
        'pos_lineal': pos_lineal,
        'tiempo_ordenar': (tiempo_ordenar - inicio) * 1000,
        'tiempo_lineal': (tiempo_lineal - tiempo_ordenar) * 1000,
        'pos_binaria': pos_binaria,
        'tiempo_binaria': (tiempo_binaria - tiempo_lineal) * 1000,
        'tiempo_total': (tiempo_binaria - inicio) * 1000
    }

# Programa principal
if __name__ == "__main__":
    # Programa que genera una lista aleatoria y permite buscar números usando distintos algoritmos
    datos = generar_lista()
    print("\nLista generada:", datos)

    while True:
        objetivo = input("\n¿Qué número querés buscar?: ")
        try:
            objetivo = int(objetivo)
        except ValueError:
            print("Ingresá un número válido.")
            continue

        # Búsqueda en la lista original
        inicio = time.perf_counter()
        posicion = busqueda_lineal(datos, objetivo)
        fin = time.perf_counter()

        mensaje = f"posición {posicion}" if posicion != -1 else "no encontrado"
        print(f"\n--- BÚSQUEDA EN LISTA ORIGINAL (SIN ORDENAR) ---")
        print(f"Búsqueda lineal: {mensaje}, tiempo: {(fin - inicio)*1000:.3f} ms")
        print("La búsqueda binaria no aplica si la lista no está ordenada.")

        # Comparar métodos de ordenamiento y búsqueda
        for metodo in ['burbuja', 'insercion', 'seleccion', 'rapido']:
            resultado = ordenar_y_buscar(metodo, datos, objetivo)
            print(f"\n--- {metodo.capitalize()} + búsqueda ---")
            print(f"Ordenar: {resultado['tiempo_ordenar']:.3f} ms")
            print(f"Búsqueda lineal: posición {resultado['pos_lineal']}, tiempo: {resultado['tiempo_lineal']:.3f} ms")
            print(f"Búsqueda binaria: posición {resultado['pos_binaria']}, tiempo: {resultado['tiempo_binaria']:.3f} ms")
            print(f"Total ordenar + buscar: {resultado['tiempo_total']:.3f} ms")

        continuar = input("\n¿Querés buscar otro número? (s/n): ").lower()
        if continuar != 's':
            print("Hasta la próxima!")
            break
