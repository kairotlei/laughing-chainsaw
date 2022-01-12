# No detener ejecución...
while True:
    # Si funciona bien...
    try:
        # Pedir al usuario que introduzca las notas, admitiendo decimales
        nota_examen = float(input("Nota de examen: "))
        nota_pract = float(input("Nota de prácticas: "))
        
        # Calcular nota final, con 55% a examen y 45% a prácticas
        nota_final = (nota_examen*0.55) + (nota_pract*0.45)
        
        # debug
        print(nota_examen*0.55, nota_pract*0.45, nota_final)
        
        # Si la nota es igual o inferior a 10, calcular
        if nota_final <= 10.0:
            if nota_final < 5.0:
                print("Tu nota final es: " + str(nota_final) + ", así que suspendes")
                print("")                
            else:
                print("Tu nota final es: " + str(nota_final) + ", así que apruebas.")
                print("")
            
        # Si la nota es superior a 10, avisar.    
        else:
            print("!!  La nota da más de 10  !!")
            print("")
            
    # En caso de error...        
    except:
        # Si los inputs no son numéricos, avisar.
        print("!!  Carácter no numérico  !!")
        print("")