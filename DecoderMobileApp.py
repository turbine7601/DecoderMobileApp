from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from Decoder import Decoder

Builder.load_file('DecoderInterface.kv')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CaesarView(Screen):
    translator = Decoder.decode_caesar
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def clicked(self):
        txt = self.ids.text_to_decode.text #текст для расшифровки
        dlt = self.ids.shift.text or "1" #сдвиг
        self.ids.dtext.text = self.translator(text=txt, shift=dlt)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        self.title = "Дешифровщик"
        sm.add_widget(MainScreen(name='menu'))
        sm.add_widget(CaesarView(name='caesar'))
        return sm
    
MainApp().run()