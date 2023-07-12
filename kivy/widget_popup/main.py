from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class PopupApp(App):
    box = BoxLayout(orientation='vertical')
    lbl = Label(text="Falta completar campos")
    btn = Button(text="Volver")
    box.add_widget(lbl)
    box.add_widget(btn)
    popupCampos = Popup(title='Registro Login', content=box, auto_dismiss=False, size_hint=(.6, .8))
    btn.bind(on_press=popupCampos.dismiss)

if __name__ == '__main__':
    PopupApp().run()