# Calculadora notas trimestre
#
#
#

while True:
    print("-- BIENVENIDO --")    
    try:
    
        print("Inserte la nota de...")        
        asign = "STFM"
        
        while asign == "STFM":
            STFM = int(input("Telefonía: "))
            if STFM >10 or STFM <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
            else:
                asign = "SIRL"
                break
        
        
        while asign == "SIRL":
            SIRL = int(input("Sistemas y redes: "))
            if SIRL >10 or SIRL <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
            else:
                asign = "TPIT"
                break
            
                
        while asign == "TPIT":
            TPIT = int(input("Técnicas ICT: "))
            if TPIT >10 or TPIT <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
            else:
                asign = "EST"
                break
        
        while asign == "EST":
            EST = int(input("Electrónica: "))
            if EST >10 or EST <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
            else:
                asign = "CIST"
                break
                
        
        while asign == "CIST":
            CIST = int(input("Configuración ICT: "))
            if CIST >10 or CIST <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
            else:
                asign = "FOL"
                break
            
        while asign == "FOL":
            FOL = int(input("FOL: "))
            if FOL >10 or FOL <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
            else:
                break
        
        nota_media = float((15*STFM + 25*SIRL + 20*TPIT + 30*EST + 5*FOL + 5*CIST)/100)
        
        if nota_media < 5:
            print("Tu nota media es", nota_media, "así que SUSPENDES.")
        elif nota_media >= 5 and nota_media <6:
            print("Tu nota media es", nota_media, "así que APRUEBAS con SUFICIENTE.")
        elif nota_media >= 6 and nota_media <7:
            print("Tu nota media es", nota_media, "así que APRUEBAS con BIEN.")
        elif nota_media >= 7 and nota_media <8:
            print("Tu nota media es", nota_media, "así que APRUEBAS con NOTABLE.")
        elif nota_media >= 8 and nota_media <10:
            print("Tu nota media es", nota_media, "así que APRUEBAS con SOBRESALIENTE.")
        elif nota_media == 10:
            print("Tu nota media es", nota_media, "así que APRUEBAS con MAT. DE HONOR.")
        
        print("")
        
    except:
        print("!! ERROR, VUELVA A INTENTARLO !!")
        print("")

    