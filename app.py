from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from layout.screens import MainScreen, SecondScreen


Builder.load_file('layout/layout.kv')


class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == '__main__':
    #main
    MainApp().run()
