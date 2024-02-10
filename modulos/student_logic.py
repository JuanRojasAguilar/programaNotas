from tabulate import tabulate
from . import app_globals as appG
from . import main_menu as mp
alumno = {
        "id": "",
        "nombre": "",
        "edad": 0,
        "notas": {
            "parciales": [],
            "quices": [],
            "trabajos": []
            }
        }

def add():
    appG.borrar_pantalla()
    ingresar = True
    
    while ingresar == True:
        nombre = input("Ingresa el nombre del estudiante: ").title()
        identificador = input(f"Ingresa el número de identificación de {nombre}: ").upper()
        edad = int(input(f"ingresa la edad de {nombre}: "))

        newAlumno = {
            **alumno,
            "id": identificador,
            "nombre": nombre,
            "edad": edad
            }
        appG.alumnos.append(newAlumno)
        print(f"\nSe ha añadido con éxito a {nombre} en la base de datos!")
        opcion = input("\nDesea añadir otro alumno? S(si), Enter(no): ").capitalize()
        if opcion == "S":
            add()
        else:
            ingresar = False
    mp.main_menu()

def get():
    appG.borrar_pantalla()
    menu = [["1.","Buscar por nombre o Id"],["2.","salir"]]
    print(tabulate(menu,tablefmt="grid"))
    option = input("\n>>")

    if option == "1":
        appG.borrar_pantalla()
        nombre = input("Ingresa el nombre o Id del estudiante que estás buscando: ").title()
        estudiante = appG.buscar_estudiante(nombre)
        print(tabulate([estudiante], headers="keys",tablefmt="grid"))
        input("\nPresiona ENTER para volver")
        get()
    elif option == "2":
        mp.main_menu()
    else:
        get()


def add_grades_init():
    opcion = input("por favor, ingresa el nombre o Id del estudiante a calificar: ").title()
    alumno = appG.buscar_estudiante(opcion)
    add_grades(alumno)

def add_grades(alumno):
    evaluar = True
    while evaluar == True:
        appG.borrar_pantalla()
        print(tabulate([alumno],headers="keys",tablefmt="grid"))
        print("\n1.Para añadir notas de parciales\n2.Para añadir notas de quices\n3.Para añadir notas de trabajos\n4.Salir")
        anotar = input("\n>>")
        if anotar == "1":
            calificar(alumno, "parciales")
        elif anotar == "2":
            calificar(alumno, "quices")
        elif anotar == "3":
            calificar(alumno, "trabajos")
        elif anotar == "4":
            mp.main_menu()
        else:
            add_grades(alumno)
        opcion = input("Quieres seguir calificando a este estudiate? S(si) Enter(no)").upper()
        if opcion == "S":
            add_grades(alumno)
        else:
            evaluar = False

def calificar(alumno:dict, actividad:str):
    appG.borrar_pantalla()
    print(tabulate([alumno["notas"][actividad]], headers="keys",tablefmt="grid"))
    nota = int(input(f"Qué nota sacó el estudiante en {actividad}? "))
    alumno["notas"][actividad].append(nota)
    

