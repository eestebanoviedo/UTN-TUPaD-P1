# -------- Ejercicio 1: Validación de contraseña --------

# contrasena_correcta = "programacion1"
# intentos_restantes = 3

# contrasena_correcta = "programacion1"
# contrasena_usuario = input("Introduce la contraseña: ")

# if contrasena_usuario == contrasena_correcta:
#     print("Contraseña correcta. Bienvenido.")
# else:
#     print("Contraseña incorrecta. Intenta de nuevo.")

# -------- ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas? --------

# El programa no lo acepta porque la comparación es sensible a mayúsculas/minúsculas.

# -------- ¿Cómo mejorarías el programa para dar más intentos? --------

# contrasena_correcta = "programacion1"
# intentos = 3

# while intentos > 0:
#     contrasena_usuario = input("Introduce la contraseña: ")
#     if contrasena_usuario == contrasena_correcta:
#         print("Contraseña correcta. Bienvenido.")
#         break
#     else:
#         intentos -= 1
#         if intentos > 0:
#             print(f"Contraseña incorrecta. Te quedan {intentos} intento(s).")
#         else:
#             print("Has agotado todos los intentos. Acceso denegado.")


# -------- # Ejercicio 2: Identificador de vocales --------

# letra = input("Introduce una letra: ")

# letra = letra.lower()

# if letra in ["a", "e", "i", "o", "u"]:
#     print("La letra ingresada es una vocal.")
# else:
#     print("La letra ingresada no es una vocal.")


# -------- ¿Cómo manejarías vocales acentuadas (á, é)? --------

# vocales = {"a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"}
# letra = input("Introduce una letra: ").strip().lower()

# if len(letra) != 1:
#     print("Por favor, introduce solo una letra.")
# elif letra in vocales:
#     print(f"La letra '{letra}' es una vocal.")
# else:
#     print(f"La letra '{letra}' no es una vocal.")


# -------- ¿Qué estructura usarías para simplificar las comparaciones?  --------

# Usamos un array con todas las vocales y verificamos si la letra está en esa lista con in. Para evitar escribir muchos if separados.

# -------- Ejercicio 3: Clasificador de números --------

# numero = float(input("Introduce un número: "))

# if numero > 0:
#     print("El número es positivo.")
# elif numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es cero.")

# --------  ¿Qué ocurre si el usuario ingresa un texto? --------

# Si el usuario escribe texto el programa da un error (ValueError), porque float() no puede convertir letras a numero. 

# -------- ¿Cómo adaptarías el código para números decimales? --------

# Usando float

# -------- # Ejercicio 4: Comparador de números --------

# num1 = float(input("Introduce el primer número: "))
# num2 = float(input("Introduce el segundo número: "))

# if num1 > num2:
#     print("El primer número ingresado es mayor.")
# elif num1 < num2:
#     print("El primer número ingresado es menor.")
# else:
#     print("Los números ingresados son iguales.")

# -------- ¿Cómo modificarías el programa para comparar más de dos números? --------
# -------- ¿Qué pasa si se ingresan valores no numéricos? --------

# try:
#     numeros = []
#     cantidad = int(input("¿Cuántos numeros deseas comparar? "))
    
#     for i in range(cantidad):
#         numero = float(input(f"Introduce el numero {i + 1}: "))
#         numeros.append(numero)
    
#     mayor = max(numeros)
#     menor = min(numeros)
    
#     print(f"El número mayor es: {mayor}")
#     print(f"El número menor es: {menor}")
    
#     if len(set(numeros)) == 1:
#         print("Todos los números son iguales.")
# except ValueError:
#     print("Por favor, introduce valores numericos validos.")

# -------- # Ejercicio 5: Clasificar temperaturas en rangos. --------


# temperatura = float(input("Introduce la temperatura actual en °C: "))
# if temperatura <= 10:
#     print("Hace frío")
# elif 10 < temperatura <= 25:
#     print("Está templado")
# else:
#     print("Hace calor")


# -------- ¿Cómo adaptarías el programa para usar °F? --------

# temperatura_f = float(input("Introduce la temperatura actual en °F: "))
# temperatura_c = (temperatura_f - 32) * 5 / 9  # Conversión a °C

# if temperatura_c <= 10:
#     print("Hace frío")
# elif 10 < temperatura_c <= 25:
#     print("Está templado")
# else:
#     print("Hace calor")

# -------- ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")? --------

# temperatura = float(input("Introduce la temperatura actual en °C: "))
# if temperatura <= 0:
#     print("Hace mucho frío")
# elif 0 < temperatura <= 10:
#     print("Hace frío")
# elif 10 < temperatura <= 25:
#     print("Está templado")
# elif 25 < temperatura <= 35:
#     print("Hace calor")
# else:
#     print("Hace mucho calor")

# -------- Ejercicio 6: Detector de años bisiestos --------

# anio = int(input("Introduce un año: "))

# if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#     print("Se ingresó un año bisiesto.")
# else:
#     print("Se ingresó un año no bisiesto.")

# -------- ¿Por qué el año 1900 no es bisiesto? --------

# Porque es divisible por 100 pero no por 400. La regla dice que los años divisibles por 100 no son bisiestos, a menos que también sean divisibles por 400.

# -------- ¿Cómo validarías que el año sea positivo? -------- 

# anio = int(input("Introduce un año: "))

# if anio <= 0:
#     print("Por favor, ingresa un año positivo.")
# else:
#     if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#         print("Se ingresó un año bisiesto.")
#     else:
#         print("Se ingresó un año no bisiesto.")

# -------- Ejercicio 7: Ajustador de frases --------

# frase = input("Introduce una frase o palabra: ").strip()
# if not frase.endswith("."):
#     frase += "."
# print("Frase ajustada:", frase)

# -------- ¿Cómo manejarías frases que terminan con espacios? --------

# frase = input("Introduce una frase o palabra: ").strip()
# frase = frase.rstrip()  
# if not frase.endswith("."):
#     frase += "."
# print("Frase ajustada:", frase)

# -------- ¿Qué otros caracteres de puntuación podrías considerar?  --------

# frase = input("Introduce una frase o palabra: ").strip()
# if not frase.endswith((".", "!", "?")):  
#     frase += "."
# print("Frase ajustada:", frase)

# -------- # Ejercicio 8: Validador de contraseña segura --------

# contraseña = input("Crea una contraseña: ")

# longitud_valida = 8 <= len(contraseña) <= 20
# tiene_mayuscula = any(c.isupper() for c in contraseña)
# tiene_numero = any(c.isdigit() for c in contraseña)

# if longitud_valida and tiene_mayuscula and tiene_numero:
#     print("¡Felicitaciones! Creaste tu contraseña.")
# else:
#     print("La contraseña no es segura.")

# -------- ¿Cómo añadirías la regla de usar un carácter especial? --------

# contraseña = input("Crea una contraseña: ")

# longitud_valida = 8 <= len(contraseña) <= 20
# tiene_mayuscula = any(c.isupper() for c in contraseña)
# tiene_numero = any(c.isdigit() for c in contraseña)
# tiene_caracter_especial = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in contraseña)

# if longitud_valida and tiene_mayuscula and tiene_numero and tiene_caracter_especial:
#     print("¡Felicitaciones! Creaste tu contraseña.")
# else:
#     print("La contraseña no es segura. Asegúrate de incluir al menos un carácter especial.")


# -------- ¿Por qué es importante limitar la longitud máxima? --------

# Porque contraseñas largas pueden afectar el rendimiento del sistema.

# -------- # Ejercicio 9: Mejorando mensajes de error --------

# contraseña = input("Crea una contraseña: ")

# if len(contraseña) < 8:
#     print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
# elif len(contraseña) > 20:
#     print("La contraseña no es segura. Debe tener no más de 20 caracteres.")
# elif not any(c.isupper() for c in contraseña):
#     print("La contraseña no es segura. Debe tener al menos una mayúscula.")
# elif not any(c.isdigit() for c in contraseña):
#     print("La contraseña no es segura. Debe tener al menos un número.")
# else:
#     print("¡Felicitaciones! Creaste tu contraseña.")

# -------- ¿Cómo evitarías repetir código al verificar cada condición? --------

# contraseña = input("Crea una contraseña: ")

# errores = []

# if len(contraseña) < 8:
#     errores.append("Debe tener al menos 8 caracteres.")
# if len(contraseña) > 20:
#     errores.append("Debe tener no más de 20 caracteres.")
# if not any(c.isupper() for c in contraseña):
#     errores.append("Debe tener al menos una mayúscula.")
# if not any(c.isdigit() for c in contraseña):
#     errores.append("Debe tener al menos un número.")

# if errores:
#     print("La contraseña no es segura:")
#     for error in errores:
#         print(f"- {error}")
# else:
#     print("¡Felicitaciones! Creaste tu contraseña.")

# -------- ¿Qué ventajas tiene este enfoque para el usuario? --------

# El usuario ve todos los problemas de su contraseña de una vez, no solo uno por intento, esto ahorra tiempo.

# -------- Ejercicio 10: Clasificador de edades --------

# jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
# jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# if jugador1 == jugador2:
#     print("EMPATE")
# elif (jugador1 == "piedra" and jugador2 == "tijera") or \
#      (jugador1 == "papel" and jugador2 == "piedra") or \
#      (jugador1 == "tijera" and jugador2 == "papel"):
#     print("GANA JUGADOR 1")
# else:
#     print("GANA JUGADOR 2")

# -------- ¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)? --------

# opciones_validas = ["piedra", "papel", "tijera"]

# jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
# jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
#     print("Error: jugada inválida. Debes elegir entre 'piedra', 'papel' o 'tijera'.")
# else:
#     if jugador1 == jugador2:
#         print("EMPATE")
#     elif (jugador1 == "piedra" and jugador2 == "tijera") or \
#          (jugador1 == "papel" and jugador2 == "piedra") or \
#          (jugador1 == "tijera" and jugador2 == "papel"):
#         print("GANA JUGADOR 1")
#     else:
#         print("GANA JUGADOR 2")


# -------- ¿Qué estructura usarías para simplificar las comparaciones? --------

# opciones_validas = ["piedra", "papel", "tijera"]

# resultados = {
#     ("piedra", "piedra"): "EMPATE",
#     ("piedra", "papel"): "GANA JUGADOR 2",
#     ("piedra", "tijera"): "GANA JUGADOR 1",
#     ("papel", "piedra"): "GANA JUGADOR 1",
#     ("papel", "papel"): "EMPATE",
#     ("papel", "tijera"): "GANA JUGADOR 2",
#     ("tijera", "piedra"): "GANA JUGADOR 2",
#     ("tijera", "papel"): "GANA JUGADOR 1",
#     ("tijera", "tijera"): "EMPATE"
# }

# jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower().strip()
# jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower().strip()

# if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
#     print("Error: jugada inválida. Debes elegir entre 'piedra', 'papel' o 'tijera'.")
# else:
#     resultado = resultados[(jugador1, jugador2)]
#     print(resultado)





