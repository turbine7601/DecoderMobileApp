from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from Decoder import Decoder

Builder.load_file("DecoderInterface.kv")

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class CaesarView(Screen):
    translator = Decoder.decode_caesar
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
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
        if not self.ids.rus.active:
            self.ids.dtext.text = Decoder.Atbash(txt, "en")
        else:
            self.ids.dtext.text = Decoder.Atbash(txt, "ru")

class VignereView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def clicked(self):
        txt = self.ids.text_to_decode.text
        key = self.ids.key.text
        if not self.ids.mode.active:
            if not self.ids.rus.active:
                self.ids.dtext.text = Decoder.Vignere(txt, key, "en")
            else:
                self.ids.dtext.text = Decoder.Vignere(txt, key, "ru")
        else:
            if not self.ids.rus.active:
                self.ids.dtext.text = Decoder.Vignere(txt, key, "en", 'encrypt')
            else:
                self.ids.dtext.text = Decoder.Vignere(txt, key, "ru", 'encrypt')

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        self.title = "Дешифровщик"
        sm.add_widget(MainScreen(name="menu"))
        sm.add_widget(CaesarView(name="caesar"))
        sm.add_widget(AtbashView(name="atbash"))
        sm.add_widget(VignereView(name="vignere"))
        sm.add_widget(InfoScreen(name="info"))

        return sm
    
MainApp().run()
