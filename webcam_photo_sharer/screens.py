import os
import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.clipboard import Clipboard

from .filesharer import FileSharer


class FilestackApiKeyMissing(BaseException):
    pass


try:
    filestack_api_key = os.environ['FILESTACK_API_KEY']
except KeyError:
    raise FilestackApiKeyMissing('FILESTACK_API_KEY not set')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_control.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_control.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime("%Y%m%d_%H%M%S")
        self.filepath = f"images/image_{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_msg = "Create a link first!"

    def create_link(self):
        global filestack_api_key
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        file_sharer = FileSharer(file_path, api_key=filestack_api_key)
        self.link = file_sharer.share()
        self.ids.link_label.text = self.link

    def copy_link(self):
        try:
            Clipboard.copy(self.link)
        except AttributeError:
            self.ids.link_label.text = self.link_msg

    def open_link(self):
        try:
            webbrowser.open(self.link)
        except AttributeError:
            self.ids.link_label.text = self.link_msg
