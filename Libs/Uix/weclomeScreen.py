from kivy.uix.screenmanager import Screen

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from .jThemeView import JThemeView
kvFileOpenExistSessionButtonID = "OpenExistSessionButtonID"
kvFileCreateNewSessionButtonID = "CreateNewSessionButtonID"

class WelcomeScreen(Screen):


    def openExistSessionButtonReleased(self):
        button = self.ids[kvFileOpenExistSessionButtonID]

    def createNewSessionButtonReleased(self):
        button = self.ids[kvFileCreateNewSessionButtonID]


class WelcomeScreenSessionListItemView(RecycleDataViewBehavior, Widget, JThemeView):
    filename = StringProperty()
    patient_name = StringProperty()
    filepath = StringProperty()
    selected = BooleanProperty()
    pass