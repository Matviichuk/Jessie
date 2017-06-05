from kivy.uix.screenmanager import Screen

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty

from kivy.uix.modalview import ModalView

from os.path import sep, expanduser, isdir, dirname
from kivy.garden.filebrowser import FileBrowser
from kivy.utils import platform

#from .jThemeView import JThemeView

kvFileOpenExistSessionButtonID = "OpenExistSessionButtonID"
kvFileCreateNewSessionButtonID = "CreateNewSessionButtonID"



class WelcomeScreen(Screen):

    modalView = ""

    def openExistSessionButtonReleased(self):

        button = self.ids[kvFileOpenExistSessionButtonID]
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')])

        view = ModalView(auto_dismiss=False)

        browser.bind(
            on_success=self._fbrowser_success,
            on_canceled=view.dismiss)


        view.add_widget(browser)
        view.open()

    def _fbrowser_success(self, instance):
        print(instance.selection)

    def createNewSessionButtonReleased(self):
        button = self.ids[kvFileCreateNewSessionButtonID]


class WelcomeScreenSessionListItemView(RecycleDataViewBehavior, Button):
    filename = StringProperty()
    patient_name = StringProperty()
    filepath = StringProperty()
    selected = BooleanProperty()
    pass