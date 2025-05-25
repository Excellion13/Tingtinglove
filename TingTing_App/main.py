
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class TingTingApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        greeting = Label(text="为了你，我亲爱的婷婷，我编写了一个应用程序来学习你的语言", font_size='18sp', halign='center')
        layout.add_widget(greeting)

        vocab = [
            ("Ich liebe dich", "我爱你", "wo_ai_ni.mp3"),
            ("Ich vermisse dich", "我想你", "wo_xiang_ni.mp3")
        ]

        for german, chinese, audio in vocab:
            btn = Button(text=f"{german} - {chinese}", size_hint_y=None, height=50)
            btn.bind(on_press=lambda instance, file=audio: self.play_audio(file))
            layout.add_widget(btn)

        return layout

    def play_audio(self, file_name):
        sound = SoundLoader.load(file_name)
        if sound:
            sound.play()

if __name__ == '__main__':
    TingTingApp().run()
