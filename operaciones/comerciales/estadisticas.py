import math


def calculos_estadisticos():
    conjunto=[]
    entrada=input("Escribe los datos separados por espacio: ")
    datos=entrada.split(" ")
    
    for i in datos:
        x=float(i)
        conjunto.append(x)

    print(f"Datos:{conjunto}")


#calcular la media
    def media(lista):
        suma=sum(lista)
        n=len(lista)
        x=suma/n             #formula de la media
        return x
    prom=media(conjunto)


#Calcular los cuadrados
    cuadrados=[]
    def calcularcuadrados(lista):
        for i in lista:
            c=i**2
            cuadrados.append(c)      #recoger lista de cuadrados
        return cuadrados
    cuad=calcularcuadrados(conjunto)

#calcular varianaza
    def varianza(lista):
        n=len(lista)
        suma_cuadrados=sum(lista)
        var=suma_cuadrados/n-prom**2   #formula de varianza
        return var


#llamamos las funciones
    S2=round(varianza(cuad),2)
    s=round(math.sqrt(S2),2)

#imprimir diccionario
    dic={"media":prom,"varianza":S2,"desviación":s}
    print(dic)
