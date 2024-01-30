from entradas.INPUT import *
from entradas.OPCIONALES import *
from operaciones.artimeticas.geometricas import *
from operaciones.artimeticas.operaciones_basicas import *
from operaciones.comerciales.estadisticas import *
from operaciones.comerciales.financieras import *

print("PROGRAMA PARA EFECTUAR OPERACIONES BÁSICAS")

def recoge_datos():

    datos_entrada=entrada()
    print("INTRODUCE INFORMACIÓN ADICIONAL:")
    datos_adicionales=datos_opcionales()

    print("Confirma dus datos:")
    for i in datos_entrada:
        print(i)
    for j in datos_adicionales:
        print(j)
    return datos_entrada

lista=recoge_datos()
nombre=lista[0]

confirma=input("Introduce SI o NO: ").lower()

while confirma!="no" and confirma!="si":
    print("Error.")
    confirma=input("Por favor, introduce SI o NO: ").lower()

while confirma=="no":
    recoge_datos()
    confirma=input("Introduce SI o NO: ").lower()



print(f"BIENVENIDO {nombre}¿Qué operación vas a realizar?")
print("ARTIMETICAS, GEOMÉTRICAS, ESTADISTICAS, COMERCIALES")
eleccion=input("ingresa el nombre del tipo de operación: ")


if eleccion=="ARITMETICAS":
    srmd=input("Deseas realizar suma (s), resta (s), multiplicación (m) o división (d): ")
    if srmd.lower()=="s":
        print("Resultado= ", suma(int(input("primer sumando= ")),int(input("primer sumando= "))))

    elif srmd.lower()=="r":
        print("Resultado= ", resta(int(input("minuendo= ")),int(input("sustraendo= "))))

    elif srmd.lower()=="m":
        print("Resultado= ", producto(int(input("primer factor= ")),int(input("primer factor= "))))

    elif srmd.lower()=="d":
        print("Resultado= ", cociente(int(input("dividendo= ")),int(input("divisor= "))))




if eleccion=="GEOMETRICAS":
    pass

if eleccion=="ESTADISTICAS":
    pass

if eleccion=="COMERCIALES":
    pass


