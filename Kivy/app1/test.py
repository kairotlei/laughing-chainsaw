from kivymd.app import MDApp
from kivy.lang import Builder

class MainAPP(MDApp):
    def build(self):
        return Builder.load_file("login.kv")
    
    def login(self, user_login, pass_login):
        users = {"test":"abc"}
        if pass_login == users[user_login]:
            self.root.ids.login_status.text = "logged!"
        else:
            self.root.ids.login_status.text = ":("            
        
    def clear(self):
        self.root.ids.user_login.text = ""   
        self.root.ids.pass_login.text = ""        
        
    
if __name__ == '__main__':
    MainAPP().run()

    
#  ------------------------------------
#            
#             ( icono persona )
#
#
# 
#             inp. USUARIO
#
#             inp. PASSWD
#
#
#    bt.LOGIN                 bt.CLEAR
# --------------------------------------
#                                      MDCard