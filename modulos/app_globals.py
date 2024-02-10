import os
import platform

alumnos = []

titulo_principal = """
        +++++++++++++++++++++++++++++++++++++++++++
        +  SISTEMA REGISTRO NOTAS DE ESTUDIANTES  +
        +++++++++++++++++++++++++++++++++++++++++++
                """

def borrar_pantalla():
    sistema = platform.system()
    if sistema == "Linux" or sistema == "Darwin":
        os.system("clear")
    else:
        os.system("cls")
    print(titulo_principal)

def buscar_estudiante(identificador:str):
    for alumno in alumnos:
        if alumno["nombre"] == identificador:
            return alumno
        elif alumno["id"] == identificador:
            return alumno
        else:
            print("No pude encontrar un alumno con ese nombre")

def buscar_identificador(identificador:str):
    for alumno in alumnos:
        if alumno["id"] == identificador:
            return alumno
        else:
            print("No pude encontrar un alumno con ese identificador")
