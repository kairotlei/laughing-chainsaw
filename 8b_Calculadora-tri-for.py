# Calculadora notas trimestre
#
#
#

while True:
    print("-- BIENVENIDO --")    
    asigns = {"STFM":"Telefonía", "SIRL":"Sistemas y redes", "TPIT":"Técnicas ICT", "CIST":"Config. ICT", "EST":"Electrónica", "FOL":"FOL"}
    try:
    
        print("Inserte la nota de...")
        
        for asign in asigns:
            nombre_asg = str(asigns[asign])
            asigns[asign] = int(input(asigns[asign]+": "))
            while asigns[asign] >10 or asigns[asign] <1:
                print("La nota no es válida (<1 o >10), vuelva a intentar")
                asigns[asign] = int(str(input(nombre_asg+": ")))
                
        
        nota_media = float((15*asigns["STFM"] + 25*asigns["SIRL"] + 20*asigns["TPIT"] + 30*asigns["CIST"] + 5*asigns["EST"] + 5*asigns["FOL"])/100)
        
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
        
    except Exception as exc:
        print("!! ERROR: !!")
        print("")
        print(str(exc))
        print("")
        print("!! VUELVA A INTENTARLO !!")
        print("")

    