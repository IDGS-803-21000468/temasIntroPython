import os

def funcion1():
    os.system("cls")
    print("Dame dos numeros")
    num1 = int(input())
    num2 = int(input())
    print("El resultado de la suma es: ", num1 + num2)   
    input("Presiona enter para continuar")
    os.system("cls")


def funcion2():
    print("Dame dos numeros")
    num1 = int(input())
    num2 = int(input())
    print("El resultado de la resta es: ", num1 - num2)    
    input("Presiona enter para continuar")
    os.system("cls")


def funcion3():
    print("Dame dos numeros")
    num1 = int(input())
    num2 = int(input())
    print("El resultado de la multiplicación es: ", num1 * num2)
    input("Presiona enter para continuar")
    os.system("cls")


def funcion4():
    print("Dame dos numeros")
    num1 = int(input())
    num2 = int(input())
    print("El resultado de la división es: ", num1 / num2)
    input("Presiona enter para continuar")
    os.system("cls")


def run():
    os.system("cls")
    while True:
        print("Bienvenido a la calculadora")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            funcion1()
        elif opcion == "2":
            funcion2()
        elif opcion == "3":
            funcion3()
        elif opcion == "4":
            funcion4()
        elif opcion == "5":
            break
        else:
            break

if __name__ == "__main__":
    run()