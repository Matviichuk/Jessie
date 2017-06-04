from kivy.garden.router import Router, route

from .Uix.weclomeScreen import WelcomeScreen
from .Uix.workspaceScreen import WorkspaceScreen
class MainRouter(Router):
    @route("/")
    def index(self):
        return WelcomeScreen()
    @route("/workspace")
    def workspace(self):
        return WorkspaceScreen()
