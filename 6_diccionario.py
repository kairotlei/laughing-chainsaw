# Mostrar resultado de la IP perteneciente a una persona

# Ejecución infinita... (hasta que falle, try/except no implementado)
while True:
    # Diccionario con IPs asignadas a X persona
    dicc = {"Manolo":"10.22.22.222", "Juan":"10.22.22.223", "Ana":"10.22.22.224", "Santiago":"10.22.22.225"}
    
    # Buscar mediante print(dicc{nombre})
    print("IP:", dicc[input("Escribir nombre: ")])
