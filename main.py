from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from webcam_photo_sharer.screens import CameraScreen, ImageScreen
from webcam_photo_sharer.filesharer import FileSharer

Builder.load_file("webcam_photo_sharer/frontend.kv")


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
