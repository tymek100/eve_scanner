from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('layout.kv')


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class MyButton(MDRaisedButton, TouchBehavior):

    def on_long_touch(self, *args):
        print("<on_long_touch> event")

    def on_double_tap(self, *args):
        print("<on_double_tap> event")
        

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")


class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SecondScreen(name='setcond'))
        return sm

if __name__ == '__main__':
    MainApp().run()
