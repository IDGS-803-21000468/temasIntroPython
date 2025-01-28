import os

class Diccionario:
    # Constructor de la clase
    def __init__(self):
        self.palabra1 = ""
        self.palabra2 = ""
        self.palabra3 = ""
    
    def menu(self):
        print("1. Agregar palabra")
        print("2. Buscar palabra")
        print("3. Salir")
    
    def agregar(self):
        with open("diccionario.txt", "a") as f:  
            x = f"{self.palabra1}:{self.palabra2}\n"
            f.write(x)
        print("Palabra agregada con éxito.")
        input("Presiona enter para continuar")
        os.system("cls")
    
    def buscar(self):
            with open("diccionario.txt", "r") as f:
                encontrado = False
                for linea in f:
                    if self.palabra3 in linea:
                        print("La palabra encontrada es: {}".format(linea))
                        encontrado = True
                        break
                if not encontrado:
                    print("La palabra no se encontró en el diccionario.")
                input("Presiona enter para continuar")
                os.system("cls")


def main():
    obj = Diccionario()
    while True:
        obj.menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            obj.palabra1 = input("Ingrese la palabra en inglés: ")
            obj.palabra2 = input("Ingrese la palabra en español: ")
            obj.agregar()
        elif opcion == "2":
            obj.palabra3 = input("Ingrese la palabra a buscar: ")
            obj.buscar()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
            input("Presiona enter para continuar")
            os.system("cls")


if __name__ == "__main__":
    main()
