def triangulo_rectangulo (b,h):
    area=b*h
    hip=b**2+h**2
    perimetro=b+h+hip
    dicc={"Area:":area,"Perimetro:":perimetro}

def cuadrado (l):
    area=l*l
    perimetro=4*l
    dicc={"Area:":area,"Perimetro:":perimetro}

def rectangulo (b,h):
    area=b*h
    perimetro=2*b+2*h
    dicc={"Area:":area,"Perimetro:":perimetro}

def  circulo (r):
    area=3.14159*r**2
    perimetro=2*3.14159*r
    dicc={"Area:":area,"Perimetro:":perimetro}    
