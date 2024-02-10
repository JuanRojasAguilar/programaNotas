from tabulate import tabulate

from . import app_globals as appG
from . import student_logic

def main_menu():
    appG.borrar_pantalla()
    menu=[["1.", "Añadir estudiante"],["2.","Reporte estudiante"],["3.","Añadir notas"],["4.","Salir"]]
    print(tabulate(menu,tablefmt="grid"))
    option = input("\n>")

    if option == "1":
        student_logic.add()
    elif option == "2":
        student_logic.get()
    elif option == "3":
        student_logic.add_grades_init()
    elif option == "4":
        print("Hasta la próxima profesor!")
        input()
        return
    else:
        main_menu()

