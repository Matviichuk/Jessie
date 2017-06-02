from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty

class JSearchBarClearIcon(Widget):
    textExist = BooleanProperty()

    def do_search(self,func, SearchString):
        func(SearchString)