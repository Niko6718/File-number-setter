from tkinter import *

class file_names_list_class():
    def __init__(self):
        self.__parent = self.root
        self.__frames_color = self.frames_color
        self.__frames_padx = self.frames_padx
        self.__frames_pady = self.frames_pady

        self.__file_names_list_frame = Frame(self.__parent, bg=self.__frames_color, height=15, width=50)

        # Список фреймов
        self.files_name_list = Listbox(self.__file_names_list_frame, selectmode=SINGLE)
        self.__files_name_list_scroll = Scrollbar(self.__file_names_list_frame, orient="vertical")
        self.__files_name_list_scroll.config(command=self.files_name_list.yview)
        self.files_name_list.config(yscrollcommand=self.__files_name_list_scroll.set)

        self.__pack_elements()

    def __pack_elements(self):
        self.__file_names_list_frame.pack(side=LEFT, padx=self.__frames_padx, pady=self.__frames_pady, fill=BOTH,
                                          expand=True)

        self.__files_name_list_scroll.pack(side=RIGHT, fill=Y)
        self.files_name_list.pack(side=RIGHT, padx=2, pady=2, fill=BOTH, expand=True)
