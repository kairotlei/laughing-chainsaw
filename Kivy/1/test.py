from kivymd.app import MDApp
from kivy.lang import Builder

class MainAPP(MDApp):
    def build(self):
        return Builder.load_file("ui.kv")
    
if __name__ == '__main__':
    MainAPP().run()


