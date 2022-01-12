# Calculadora


def sumar(n1, n2):
    return n1+n2

def restar(n1, n2):
    return n1-n2
    
def multi(n1, n2):
    return n1*n2

def dividir(n1, n2):
    return n1/n2


def start():
    print("-- Bienvenido! --")
    
    n1 = float(input("Primer  número: "))
    n2 = float(input("Segundo número: "))
    hacer = input("¿Qué quieres hacer? ")
    print("")
    return [n1, n2, hacer]

acciones = start()

# sumar
if "um" in acciones[2].lower():
    print("Vale, el resultado es", sumar(acciones[0], acciones[1]) )
    
# multiplicar o producto
if "ul" in acciones[2].lower() or "ro" in acciones[2].lower():
    print("Vale, el resultado es", multi(acciones[0], acciones[1]) )
    
# dividir
if "iv" in acciones[2].lower():
    print("Vale, el resultado es", dividir(acciones[0], acciones[1]) )
    
# restar
if "es" in acciones[2].lower():
    print("Vale, el resultado es", restar(acciones[0], acciones[1]) )     
