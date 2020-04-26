import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        # self.add_widget(Label(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        # self.add_widget(Label(text='password'))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)

    def set_scores(self, player_scores):
        self.add_widget(Label(text=player_scores[0]))
        self.add_widget(Label(text=player_scores[1]))

class MyApp(App):
    def build(self):
        l = LoginScreen()
        l.set_scores(['222', '111'])
        return l
        # return Label(text='Hello World')

def open_gui():
    # if __name__ == '__main__':
    m = MyApp()
    m.run()

open_gui()