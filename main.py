from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


# for future check out
Window.size = (300,500)
# class Demo(FloatLayout):
#     pass


class Main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'LightBlue'
        return Builder.load_file("main.kv")

    def navigation_draw(self):
        print("navigation")


Main().run()
