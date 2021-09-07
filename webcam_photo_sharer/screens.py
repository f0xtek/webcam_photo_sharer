import time

from kivy.uix.screenmanager import Screen


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_control.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_control.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime("%Y%m%d_%H%M%S")
        self.ids.camera.export_to_png(f'images/image_{current_time}.png')


class ImageScreen(Screen):
    pass
