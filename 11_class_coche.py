class Coche:
    def __init__(self):
        self.marca = input("Introduce la marca del coche: ")
        self.modelo = input("Introduce el modelo del coche: ")
        self.color = input("Introduce el color del coche: ")
        self.extra = input("Extras? ")
        
        #if self.extra != "":
            #print("El coche es un", self.marca, self.modelo, "de color", self.color, "y tiene", self.extra, "como extras")
            
        #else:
            #print("El coche es un", self.marca, self.modelo, "de color", self.color)
        
coche1 = Coche()



if coche1.extra != "":
    print("El coche es un", coche1.marca, coche1.modelo, "de color", coche1.color, "y tiene", coche1.extra, "como extras")
    
else:
    print("El coche es un", coche1.marca, coche1.modelo, "de color", coche1.color)

print(coche1).aa