import kivy
from kivy.garden.router import AppRouter
kivy.require('1.9.1')

from .appRouter import MainRouter

class App(AppRouter):
    def build(self):
        self.root = MainRouter()
        self.route = "/"
        return