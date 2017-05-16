import os.path
from kivy.lang import Builder

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.kv'))

Builder.load_file(KV_PATH)
