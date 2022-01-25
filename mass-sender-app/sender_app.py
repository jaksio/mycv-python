from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty



class MyGrid(Widget):
    ''' draws layout based on kv file '''
    phone_numbers = ObjectProperty(None)

    def btn(self):
        print("dziala przycisk")


class SenderApp(App):
    ''' Kivy sender application | inherites from kivy module app'''

    def build(self):
        ''' build application interface '''
        return MyGrid()


if __name__ == "__main__":
    SenderApp().run()