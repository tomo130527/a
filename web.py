# main.py
from kivy.app import App
from kivy.uix.button import Button

class HelloWorldApp(App):
    def build(self):
        return Button(text='Hello World!')

if __name__ == '__main__':
    HelloWorldApp().run()
