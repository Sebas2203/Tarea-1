"""
Tarea 1
Estudiante: Sebastián Mora Rodríguez
"""

# Realizar un programa que permite ingresar valores numéricos en dos arreglos de un tamaño de 5 posiciones y el resultado será  los valores ordenados descendentemente en un tercer arreglo. lo pueden hacer en python , java o C#, el estudiante elige
# ejemplo:
# arreglo 1: 3 2 6
# arreglo 2: 9 1 0
# Arreglo3:  9 6 3 2 1 0

def sort_arrays():
    # arrays    
    array1 = []
    array2 = []

    # menu
    # arreglo 1
    print("\n--Arreglo 1--")
    print("\nIngrese 5 números")
    for i in range(1,6):
        try:
            number = int(input(f"{i}-> "))
            array1.append(number)
        except ValueError:
            print("\nIngrese un valor correcto.\n")
    array1.sort(reverse=True)

    # arreglo 2
    print("\n--Arreglo 2--")
    print("\nIngrese 5 números")
    for i in range(1,6):
        try:
            number = int(input(f"{i}-> "))
            array2.append(number)
        except ValueError:
            print("\nIngrese un número.\n")
    array2.sort(reverse=True)

    # arreglo 3 
    # union de array1 y array2 para hacer un array3
    array3 = [*array1,*array2]
    array3.sort(reverse=True)

    # print sorted arrays 
    print("--Arreglo 1--")
    print(array1)
    print("--Arreglo 2--")
    print(array2) 
    print("--Arreglo 3--")
    print(array3)
    print(type(array3))

sort_arrays()
