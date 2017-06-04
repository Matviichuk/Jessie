import os.path
from kivy.lang import Builder
KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.kv'))
Builder.load_file(KV_PATH)

from nilearn import image

from kivy.factory import Factory
#from .jThemeView import JThemeView
#Factory.register('JThemeView', JThemeView)

from .weclomeScreen import WelcomeScreen
from .workspaceScreen import WorkspaceScreen
#from .jTheme import JTheme

__all__ = ("WelcomeScreen",
           "WorkspaceScreen"
           )


