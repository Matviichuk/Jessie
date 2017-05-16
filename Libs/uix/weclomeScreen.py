from kivy.uix.screenmanager import Screen

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

kvFileOpenExistSessionButtonID = "openExistSessionButtonID"
kvFileCreateNewSessionButtonID = "createNewSessionButtonID"

class WelcomeScreen(Screen):

    def openExistSessionButtonPressed(self):
        button = self.ids[kvFileOpenExistSessionButtonID]
        button.background_color = [0.3, 0.3, 0.3, 1]
        button.color = [1, 1, 1, 1]

    def openExistSessionButtonReleased(self):
        button = self.ids[kvFileOpenExistSessionButtonID]
        button.background_color = [0.94, 0.94, 0.94, 1]
        button.color = [0, 0, 0, 1]

    def createNewSesionButtonPressed(self):
        button = self.ids[kvFileCreateNewSessionButtonID]
        button.background_color = [0.24, 0.54, 0.96, 1]
        button.color = [1, 1, 1, 1]

    def createNewSessionButtonReleased(self):
        button = self.ids[kvFileCreateNewSessionButtonID]
        button.background_color = [0, 0, 0, 0]
        button.color = [0, 0, 0, 1]
    pass

class WelcomeScreenSessionListItemView(RecycleDataViewBehavior, Widget):
    filename = StringProperty()
    patient_name = StringProperty()
    filepath = StringProperty()
    selected = BooleanProperty()
    pass