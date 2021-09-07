from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import requests
import wikipedia

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()

    def download_image(self):
        filename = f'images/image.jpg'
        image_url = self.get_image_url()

        headers = {
            # bogus User Agent to keep Wikipedia happy
            'User-Agent': 'WikiImageSearch/1.0 (https://doesnotexist.com) generic-library/1.0'
        }

        resp = requests.get(image_url, headers=headers)
        resp.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(bytes(resp.content))

        return filename

    def get_image_url(self):
        query = self.manager.current_screen.ids.user_query.text
        page = wikipedia.page(query)
        return page.images[0]


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
