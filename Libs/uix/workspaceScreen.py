from kivy.uix.screenmanager import Screen


class WorkspaceScreen(Screen):
    def new_session_button_pressed(self):
        print("new_session_button_pressed")
    def open_session_button_pressed(self):
        print("open_session_button_pressed")
    def save_session_button_pressed(self):
        print("save_session_button_pressed")
    def add_to_library_button_pressed(self):
        print("add_to_library_button_pressed")
    pass