# not use, will use in future !!!!
from .jTheme import JTheme

class JThemeView:
    theme = JTheme()
    def get_color_for_element(self, element):
        return [0, 0, 0, 1]
    pass