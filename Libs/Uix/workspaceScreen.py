from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

kvFileMediaLibrarySearchBarID = "MediaLibrarySearchBar"
kvFileSegmentsLibrarySearchBarID = "SegmentsLibrarySearchBar"

class WorkspaceScreen(Screen):

    def __init__(self, **kwargs):
        super(WorkspaceScreen, self).__init__(**kwargs)
        medialibrarySearchBar = self.ids[kvFileMediaLibrarySearchBarID]
        medialibrarySearchBar.bind(on_search_text=self._filer_medialibrary_tab_data)
        segmentsLibrarySearchBar = self.ids[kvFileSegmentsLibrarySearchBarID]
        segmentsLibrarySearchBar.bind(on_search_text=self._filter_segments_tab_data)


        #temporary
        self.mediaLibraryShowData.clear()
        for item in self.mediaLibraryAllData:
            self.mediaLibraryShowData.append(item)
    # tmp source
    mediaLibraryAllData = [{'label_text': "Slice #" + str(x), 'index_path': x} for x in range(5)]
    mediaLibraryShowData = ListProperty()

    def new_session_button_pressed(self):
        print("new_session_button_pressed")
    def open_session_button_pressed(self):
        print("open_session_button_pressed")
    def save_session_button_pressed(self):
        print("save_session_button_pressed")
    def add_to_library_button_pressed(self):
        print("add_to_library_button_pressed")

    def _filer_medialibrary_tab_data(self, filterStr):
        tmp = [i for i in self.mediaLibraryAllData if i["label_text"].lower().__contains__(filterStr.lower())]
        self.mediaLibraryShowData = []
        if filterStr != "":
            for item in tmp:
                formated_item = item.copy()
                substr_start = formated_item["label_text"].lower().find(filterStr.lower())
                substr_end = substr_start + len(filterStr)
                str_len = len(formated_item["label_text"])
                start_markup = "[b][color=0000ff]"
                end_markup = "[/color][/b]"
                formated_text = formated_item["label_text"][0:substr_start] + start_markup+ formated_item["label_text"][substr_start:substr_end] + end_markup + formated_item["label_text"][substr_end: str_len]
                formated_item["label_text"] = formated_text
                self.mediaLibraryShowData.append(formated_item)
        else:
            for item in tmp:
                self.mediaLibraryShowData.append(item)
        pass
    def _filter_segments_tab_data(self, filterStr):
        print(filterStr)

