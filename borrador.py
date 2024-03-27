def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        print("¡Error! No se puede dividir entre 0.")
        return None
    return a / b

def multiplicacion(a, b):
    return a * b

def matematicas():
    print("¿Qué operación deseas realizar?")
    print("1) Suma")
    print("2) Resta")
    print("3) División")
    print("4) Multiplicación")
    operacion = input("Elige la operación (1/2/3/4): ")
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    if operacion == '1':
        print("Resultado:", suma(numero1, numero2))
    elif operacion == '2':
        print("Resultado:", resta(numero1, numero2))
    elif operacion == '3':
        if numero2 == 0:
            print ("no se puede dividir entre 0")
        else:
            print("resultado =", division(numero1, numero2))
    elif operacion == '4':
        print("Resultado:", multiplicacion(numero1, numero2))
    else:
        print("Operación no válida.")

# Llamar a la función calculadora para iniciar la calculadora
calculadora()