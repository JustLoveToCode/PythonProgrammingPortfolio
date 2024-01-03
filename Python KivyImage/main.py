from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import mainthread

import wikipedia
import requests
from concurrent.futures import ThreadPoolExecutor
import functools

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        query = self.manager.current_screen.ids.user_query.text

        def download_image(image_link):
            headers = {'User-agent': 'Mozilla/5.0'}
            # Using the get requests:
            req = requests.get(image_link, headers=headers)
            imagepath = 'files/image.jpg'
            with open(imagepath, 'wb') as file:
                file.write(req.content)
            self.update_image(imagepath)

        with ThreadPoolExecutor() as executor:
            future = executor.submit(wikipedia.page, query)
            future.add_done_callback(
                functools.partial(self.handle_search_result, query=query)
            )

    @mainthread
    def update_image(self, imagepath):
        self.manager.current_screen.ids.img.source = imagepath

    def handle_search_result(self, future, query):
        try:
            page = future.result()
            image_link = page.images[0]
            self.download_image(image_link)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Ambiguous query: {e.options}")
        except wikipedia.exceptions.HTTPTimeoutError:
            print("Timeout while fetching data from Wikipedia")
        except wikipedia.exceptions.WikipediaException as e:
            print(f"Wikipedia API error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def download_image(self, image_link):
        with ThreadPoolExecutor() as executor:
            executor.submit(self._download_image, image_link)

    def _download_image(self, image_link):
        headers = {'User-agent': 'Mozilla/5.0'}
        req = requests.get(image_link, headers=headers)
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        self.update_image(imagepath)


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()

