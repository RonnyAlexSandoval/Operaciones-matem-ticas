#Funcion para calcular IVA para un monto de factura y una una tasa de impuesto
def impuestos():
    def calcula_iva(factura,iva):
        impuesto=factura*iva/100
        total=factura+impuesto
        return total

    pagar=float(input("Monto de factura: "))
    porc_iva=float(input("%IVA: "))

    while porc_iva<0 or pagar<0:
        print("Introduzca solo valores positivos")
        pagar=float(input("Monto de factura: "))
        porc_iva=float(input("%IVA: "))

    if porc_iva=="":
        porc_iva=21

    resultado=calcula_iva(pagar,porc_iva)
    print("Factura con IVA= "+str(resultado))



#Función para calcular el factorial de un número entero
def factorial(num):
    a=1
    for i in range (1,num):
        a*=i+1
    print(f"{num}!={a}")
    return a


