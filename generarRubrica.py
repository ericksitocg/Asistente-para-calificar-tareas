import pyperclip as clipboard
from playsound import playsound
from time import sleep
import json

def crearRubrica():
    temas = {}
    principal = ""
    c = 0
    while principal != "-1":
        c+=1
        print("Tema " + str(c) + "\n")
        subtemas = {}
        opc = ingresaFormato()
        while opc != "-1":
            criterio,puntaje = opc.split("|")
            puntaje_total = int(puntaje)
            subtemas[criterio] = puntaje_total
            print("Temas ingresados : %d\n"%(len(subtemas)))
            opc = ingresaFormato()
        temas["Tema " + str(c)] = subtemas
        principal = input("\nIngresar nuevo tema? Enter: \nIngrese -1 para terminar el programa: ")
    with open('rubrica.json', 'w') as fp:
        json.dump(temas, fp)
    return temas

def calificarRubrica(dic):
    print("-"*10 + "Ingreso de calificaciones" + "-"*10)
    total = 0
    salida = ""
    for key in dic:#{"Tema1":{"Criterio1":nota_total,"Criterio2":nota_total},"Tema2":{"Criterio1":nota}}
        salida = salida + "\t"*3 + key + "\n"
        print("\t"*3 + key + "\n")
        for criterio in dic[key]:
            mensaje = ""
            estu = input("Cuanto saco sobre %s en: %s?"%(dic[key][criterio],criterio))
            if estu=="":
                estu=str(dic[key][criterio])
            else:
                mensaje = input("Mensaje: ")
            total += int(estu)
            salida += criterio + "\t" + estu + "/" + str(dic[key][criterio]) + "\n"  + mensaje + "\n"*2
    encabezado = "Calificacion Final    " + str(total) + "/100" + "\n"*2
    salida = encabezado + salida + "\n"*2
    print("-"*40)
    #Logica de copia y pega
    clipboard.copy(salida)
    print("La rubrica esta en el portapapeles")
    #return salida

def ingresaFormato():
    entrada = input("Ingresar el tema a evaludar|puntaje_total\nIngrese -1 para terminar tema: ")
    while not validaFormato(entrada):
        #print("Ingrese el tema a evaluar|puntaje total!")
        entrada = input("Please,Ingresar el tema a evaludar|puntaje_total\nIngrese -1 para terminar tema: ")
    return entrada

def validaFormato(entrada):
    return  ("|" in entrada and entrada.count("|")== 1) or entrada== "-1"
"""
rubrica = {
    "Tema1":{
        "Lectura csv":10,
        "Ordenamiento de valores":10,
        "Seleccion de columnas":5,
        "Slicing de los 10 mayores":5,
        "Creacion de grafico de barras":10
    },
    "Tema2":{
	    "Identificar a las filas de Ecuador":10,
	    "Seleccionar las filas con magnitud mayor a 6":10,
	    "Creacion de grafico de lineas":10
	},
    "Tema3":{
	    "Seleccion de columnas type":10,
	    "Contabilizar los valores":10,
	    "Creacion de grafico de pastel":10
	}
}
"""
with open('rubrica.json') as json_file: 
    rubrica = json.load(json_file) 

print("Inicio proceso de calificacion de deberes")
print("""
	1)Crear rubrica
	2)Presentar rubrica actual
	3)Calificar usando la rubrica actual
	""")
op = input("Ingrese opcion:")
if op == "1":
	rubrica = crearRubrica()
elif op == "2":
	print(rubrica)
elif op == "3":
	opcion = input("Desea calificar un deber ? enter|-1")
	while opcion != "-1":
	    calificarRubrica(rubrica)

	    playsound("inicio.mp3")
	    sleep(10)
	    playsound("fin.mp3")

	    opcion = input("Desea calificar un nuevo deber? enter|-1")
	print("Los deberes han sido calificados")
else:
	print("opcion no valida")
"""
clipboard.copy(corregido)
playsound("inicio.mp3")
sleep(10)
playsound("fin.mp3")
sleep(18)
"""