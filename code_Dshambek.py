from PIL import Image
from pyzbar.pyzbar import decode
#import picamera
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import TextInput
from data import key_by_num
from time import sleep
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 400)


class Menu_Screen(Screen):
    def __init__(self, **kw):
        super(Menu_Screen, self).__init__(**kw)
        #self.data = str(self.data_qr[0][0][0:])[1:]
        #self.data_qr = decode(Image.open('qr_data.png'))
        bl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))
        bl.add_widget(Button(text="Scan QR", on_press=lambda x: self.on_press(), size_hint=(0.3, 0.02), pos=(350, 200)))
        bl.add_widget(Button(text="Reg", on_press=lambda x: self.registr(), size_hint=(0.3, 0.02), pos=(350, 200)))
        self.add_widget(bl)
    def registr(self):
        print(1)
        set_screen("input")

    def on_press(self):
        set_screen("m_box")
       #try:
           # camera = picamera.PiCamera(resolution=(1280, 720))
           # for i in range(3):
             #   sleep(1)
              #  camera.capture('qr_data.png')
               # self.data_qr = decode(Image.open('qr_data.png'))
               # try:
                #    self.data = str(self.data_qr[0][0][0:])[1:]
               # except:
                 #   print("no")
        #finally:
           # camera.close()
           # print("End of program")
        #for id_man in data:

class Menu_of_box(Screen):
    def __init__(self, **kw):
        super(Menu_of_box, self).__init__(**kw)
        gl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))
        gl.add_widget(Button(text="BOx_1", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_2", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_3", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_4", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_5", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_6", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_7", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_8", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="BOx_9", on_press=lambda x: self.on_press()))
        gl.add_widget(Button(text="НАЗАД", on_press=lambda x: self.on_press()))
        self.add_widget(gl)
    def on_press(self):
        self.qr_answer = 'key0'
        key_by_num(self.qr_answer, 'ничего')
        set_screen("menu")
        pass
class Regestration(Screen):
    def __init__(self, **kw):
        super(Regestration, self).__init__(**kw)
        self.cols = 2
        gl = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.75, .75), pos=(250, 100))

        gl.add_widget(Label(text="First Name: "))
        self.name1 = TextInput(multiline=False)
        print (self.name1.text)
        self.name1.bind(text = self.on_text())
        gl.add_widget(self.name1)
        gl.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        gl.add_widget(self.lastName)

        gl.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        gl.add_widget(self.email)
        self.add_widget(gl)

    def on_text(instance,  value):
        print('The widget', instance, 'have:', value)


    #
sm = ScreenManager()
sm.add_widget(Menu_Screen(name='menu'))
sm.add_widget(Menu_of_box(name='m_box'))
sm.add_widget(Regestration(name='input'))


def set_screen(name_screen):
    assert isinstance(name_screen, object)
    sm.current = name_screen


class TestApp(App):
    def build(self):
        set_screen('menu')
        return sm


if __name__ == '__main__':
    TestApp().run()
