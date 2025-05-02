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
        if not self.ids.rus.active:
            self.ids.dtext.text = Decoder.decode_caesar(text=txt, shift=dlt)
        else:
            self.ids.dtext.text = Decoder.decode_caesar_ru(text=txt, shift=dlt)

class AtbashView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def clicked(self):
        txt = self.ids.text_to_decode.text
        self.ids.dtext.text = Decoder.Atbash(txt, 'ru')
        

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        self.title = "Дешифровщик"
        sm.add_widget(MainScreen(name='menu'))
        sm.add_widget(CaesarView(name='caesar'))
        sm.add_widget(AtbashView(name='atbash'))
        return sm
    
MainApp().run()
