
# convertir a binario: bin(variable)

# Ejecutar siempre...
while True:
    # Realizar esto, si falla se acude a -except-
    try:
        # Solicitar input para escribir un número.
        num = int(input("Escribe un número (sin decimales): "))
    
        # Mostrar el número introducido y sus conversiones.
        print("Número actual:  "+ str(num))
        print("En binario:     " + bin(num))
        print("En hexadecimal: " + hex(num))
        
        # Despedida.
        print("""
        Hecho. Adiós mundo...
        """)
    
    # En caso de fallo, avisar al usuario y volver a -try-
    except:
        print("""
        !! Input inválido. Vuelve a intentarlo.
        """)
        