from kivymd.app import MDApp
from kivy.lang import Builder

class MainAPP(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("adduser.kv")    
    
    def save_data(self, user_name, user_surname, user_course, user_email, user_telegram):
        # Guardado de datos
        name = self.root.ids.user_name.text
        surname = self.root.ids.user_surname.text
        course = self.root.ids.user_course.text
        email = self.root.ids.user_email.text
        telegram = self.root.ids.user_telegram.text
        
        aln = [name, surname, course, email, telegram]
        
        with open("bd_alumnos.txt", "a+") as file:
            print("abriendo archivo...")
            for dato in aln:
               file.write("%s; " %dato)
               print("escribiendo:  %s\n" %dato)
            file.write("\n") 

                      
        file.close()
        print("fin")

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