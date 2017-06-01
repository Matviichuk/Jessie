from kivy.garden.router import Router, route

from .uix.weclomeScreen import WelcomeScreen

class MainRouter(Router):
    @route("/")
    def index(self):
        return WelcomeScreen()
    @route("workspace")
    def workspace(self):
        return WelcomeScreen()
