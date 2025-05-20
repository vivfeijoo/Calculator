def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

print("Calculadora básica")
print("Selecciona la operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1/2/3/4): ")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if opcion == "1":
    print("Resultado:", suma(a, b))
elif opcion == "2":
    print("Resultado:", resta(a, b))
elif opcion == "3":
    print("Resultado:", multiplicacion(a, b))
elif opcion == "4":
    print("Resultado:", division(a, b))
else:
    print("Opción no válida")