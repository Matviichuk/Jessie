from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

class WorkspaceScreen(Screen):
    def __init__(self, **kwargs):
        super(WorkspaceScreen, self).__init__(**kwargs)
        medialibrarySearchBar = self.ids["MediaLibrarySearchBar"]
        medialibrarySearchBar.bind(on_search_text=self._filer_medialibrary_data)



    def new_session_button_pressed(self):
        print("new_session_button_pressed")
    def open_session_button_pressed(self):
        print("open_session_button_pressed")
    def save_session_button_pressed(self):
        print("save_session_button_pressed")
    def add_to_library_button_pressed(self):
        print("add_to_library_button_pressed")

    def _filer_medialibrary_data(self, filterStr):

        print(filterStr)
        pass

