
#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio 4
radio_circulo = float(input("Ingrese el radio del circulo: "))
pi = 3.14159265359

area_circulo = pi * radio_circulo ** 2
perimetro_circulo = 2 * pi * radio_circulo

print(f"El area del circulo es {area_circulo}")
print(f"El perimetro del circulo es {perimetro_circulo}")

#Ejercicio 5
segundos = int(input("Ingrese el numero de segundos: "))

horas = segundos // 3600

print(f"{segundos} segundos equivalen a {horas} hora")

#Ejercicio 6
numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7
numero = int(input("Ingrese un numero mayor que 0: "))
numero_2 = int(input("Ingrese otro numero mayor que 0: "))

if numero > 0 and numero_2 > 0:
    suma = numero + numero_2
    resta = numero - numero_2
    multiplicacion = numero * numero_2
    division = numero / numero_2

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicacion: {multiplicacion}")
    print(f"Division: {division}")
else:
    print("Los numeros ingresados no son mayores que 0")

#Ejercicio 8
altura = float(input("Ingrese la altura de la persona: "))
peso = float(input("Ingrese el peso de la persona: "))
imc = peso / (altura ** 2)

print(f"El IMC de la persona es {imc}")

#Ejercicio 9
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

temp_fahrenheit = (temp_celsius * 1.8) + 32

print(f"La temperatura en Fahrenheit es {temp_fahrenheit}")

#Ejercicio 10
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))
promedio = (numero_1 + numero_2 + numero_3) / 3

print(f"El promedio de los numeros ingresados es {promedio}")
