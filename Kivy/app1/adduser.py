from kivymd.app import MDApp
from kivy.lang import Builder

class MainAPP(MDApp):
    def build(self):
        # Tema oscuro
        #self.theme_cls.theme_style = "Dark"

        # Color principal = naranja
        self.theme_cls.primary_palette = "Orange"

        # Cargar .KV
        return Builder.load_file("adduser.kv")    
    

    # Guardado de datos
    def save_data(self, user_name, user_surname, user_course, user_email, user_telegram):
        
        # Guardar inputs de Kivy en variables
        name = self.root.ids.user_name.text
        surname = self.root.ids.user_surname.text
        course = self.root.ids.user_course.text
        email = self.root.ids.user_email.text
        telegram = self.root.ids.user_telegram.text
        
        # alumno = [datos que conforman el alumno]
        aln = [name, surname, course, email, telegram]
        
        # Intentar, si falla algo se notifica.
        try:
            # Pasar datos a archivo (texto plano, no DB!!)
            # Abrir archivo o crearlo si no existe.
            with open("bd_alumnos.csv", "a+") as file:
                # Pasar cada dato de alumno al archivo, con ";" entre variables para que resulte en un .csv
                # Cada [salto de] línea es un alumno distinto, así que meter un "\n" tras procesar la línea
                for dato in aln:
                    file.write("%s; " %dato)
                    print("escribiendo:  %s\n" %dato)
                    file.write("\n")
            file.close()
            print("fin")

        # En caso de fallo...
        except:
            print(" ")

        self.root.ids.user_name.text = "" 
        self.root.ids.user_surname.text = "" 
        self.root.ids.user_course.text = "" 
        self.root.ids.user_email.text = ""         
        self.root.ids.user_telegram.text = "" 
    
    def exit(self):
        exit()
    
    
if __name__ == '__main__':
    MainAPP().run()

    
    
    
#  ------------------------------------
#            
#      inp. NOMBRE
#      inp. APELLIDOS
#      inp. CURSO
#      inp. EMAIL
#
#
#    bt.LOGIN                 bt.CLEAR
# --------------------------------------
#                                      MDCard