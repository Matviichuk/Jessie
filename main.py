#!/usr/bin/python3

import gettext
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
#Config.set('graphics','resizable',0)

import kivy.app

from Libs.uix.weclomeScreen import WelcomeScreen

#Global constants
__appName__ = 'pyMRI'
__appCodeName__ = 'Jessie'

ApplicationLanguage = ''

kivy.require('1.9.1')

class MainApp(kivy.app.App):
    def build(self):
        cm = ScreenManager()
        cm.add_widget(WelcomeScreen())
        return cm


if __name__ == '__main__':
    MainApp().run()