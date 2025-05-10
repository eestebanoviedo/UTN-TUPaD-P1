# -------- Ejercicio 1 --------

# for i in range(0, 101):
#     print(i)

# -------- Ejercicio 2 --------

# numero_entero = input("Ingresa un número entero: ").strip()

# if numero_entero.isdigit():
#     cantidad_digitos = len(numero_entero)
#     print(f"El número {numero_entero} tiene {cantidad_digitos} dígitos.")
# else:
#     print("El valor ingresado no es un número entero válido.")

# -------- Ejercicio 3 --------

# num1 = int(input("Ingresa el primer número: "))
# num2 = int(input("Ingresa el segundo número: "))
# suma = 0
# if num1 < num2:
#     for i in range(num1 + 1, num2):
#         suma += i
# else:
#     for i in range(num2 + 1, num1):
#         suma += i
# print(f"La suma de los números enteros entre {num1} y {num2} es: {suma}")

# -------- Ejercicio 4 --------

# suma = 0
# while True:
#     numero = int(input("Ingresa un número entero para sumar (0 para salir): "))
#     if numero == 0:
#         break
#     suma += numero
# print(f"La suma total acumulada es: {suma}")

# -------- Ejercicio 5 --------

# import random
# numero_aleatorio = random.randint(0, 9)
# intentos = 0
# while True:
#     intento = int(input("Adivina el número entre 0 y 9: "))
#     intentos += 1
#     if intento == numero_aleatorio:
#         print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
#         break
#     elif intento < numero_aleatorio:
#         print("El número es mayor.")
#     else:
#         print("El número es menor.")

# -------- Ejercicio 6 --------

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, -1, -2):
#     print(i)

# -------- Ejercicio 7 --------

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# numero = int(input("Ingresa un número entero positivo: "))
# suma = 0
# for i in range(1, numero + 1):
#     suma += i
# print(f"La suma de los números entre 0 y {numero} es: {suma}")

# -------- Ejercicio 8 --------

# contador_pares = 0
# contador_impares = 0
# contador_positivos = 0
# contador_negativos = 0
# for i in range(100):
#     numero = int(input(f"Ingrese el número {i + 1}: "))
#     if numero % 2 == 0:
#         contador_pares += 1
#     else:
#         contador_impares += 1
#     if numero > 0:
#         contador_positivos += 1
#     elif numero < 0:
#         contador_negativos += 1
# print(f"Números pares: {contador_pares}")
# print(f"Números impares: {contador_impares}")
# print(f"Números positivos: {contador_positivos}")
# print(f"Números negativos: {contador_negativos}")

# -------- Ejercicio 9 --------

# N = 5  
# suma = 0

# for i in range(N):
#     x = int(input(f"Ingrese el entero {i+1}/{N}: "))
#     suma += x

# media = suma / N
# print(f"\nLa media de los {N} números ingresados es {media:.2f}")

# -------- Ejercicio 10 --------

# numero = input("Ingresa un número: ")
# numero_invertido = numero[::-1]
# print(f"El número invertido es: {numero_invertido}")



