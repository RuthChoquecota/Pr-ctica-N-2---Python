#Item 8
numero = int(input("Ingresa un número entero: "))
if numero > 0:
    suma = (numero * (numero + 1)) // 2
    print(f"La suma de los números de 1 hasta {numero} es {suma}.")
else:
    print("Ingresa un número entero: ")