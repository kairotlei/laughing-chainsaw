class Coche():
    

    
    def __init__(self):
        self.marca = input("Introduzca la marca de su coche: ")
        self.modelo = input("Introduzca el modelo de su coche: ")
        #seatself.color = input("Introduzca el color de su coche: ")
        self.potencia = int(input("Introduzca la potencia de su coche: "))    
    
    def impr(self):
        #print("Mi coche es un", self.marca, self.modelo, "con", self.potencia, "CV de potencia.")
        
        self.euros = 1000
        if self.marca.lower() in "renault citroen opel vw volkswagen peugeot seat kia toyota kia":
            self.valor_marca = 5000
        if self.marca.lower() in "tesla audi mercedes bmw bmv":
            self.valor_marca = 10000
        if self.marca.lower() in "ferrari lamborghini f1":
            self.valor_marca = 30000
        self.valor_cv = self.potencia**2 + self.potencia*(self.valor_marca / 1000)
        self.euros = self.valor_cv+self.valor_marca
        print("Tu", self.marca, self.modelo, "vale", self.euros, "€")
    
coche = Coche()

coche.impr()