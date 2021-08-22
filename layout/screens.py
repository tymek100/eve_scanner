from kivy.uix.screenmanager import Screen
from .buttons import MyButton

class MainScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.startButton = MyButton(text="PRESS ME", pos_hint= {"center_x": .5, "center_y": .5})
        self.startButton.on_release = self.switch_screen
        self.add_widget(self.startButton)

    def switch_screen(self, *args):
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.startButton = MyButton(text="COME BACK", pos_hint= {"center_x": .5, "center_y": .5})
        self.startButton.on_release = self.switch_screen
        self.add_widget(self.startButton)

    def switch_screen(self, *args):
        self.manager.current = 'main'
