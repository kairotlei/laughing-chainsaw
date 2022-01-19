from kivymd.app import MDApp
from kivy.lang import Builder
import json

class MainAPP(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("adduser_json.kv")    
    
    def save_data(self, user_name, user_surname, user_course, user_email, user_telegram):
        # Guardado de datos
        name = self.root.ids.user_name.text
        surname = self.root.ids.user_surname.text
        course = self.root.ids.user_course.text
        email = self.root.ids.user_email.text
        telegram = self.root.ids.user_telegram.text
        
        aln = [(name, surname, course, email, telegram)]
        data = []
        
        for name, surname, course, email, telegram in aln:
            data.append({"Name": name, "Surname":surname, "Course":course, "Email":email, "Telegram":telegram})
        
        with open("bd_alumnos.json", "a+",newline="\n") as file_json:
            json.dump(data,file_json)
        print("Se guardaron los datos del alumno")

                      
        file_json.close()
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