from tkinter import *


class top_drop_down_menu_class():
    def __init__(self):
        self.__parent = self.root
        self.tdd_menu = Menu(self.__parent)
        self.__parent.config(menu=self.tdd_menu)

        self.open_files_dir = None


        # Файл
        self.filemenu = Menu(self.tdd_menu, tearoff=0)
        self.filemenu.add_command(label="Открыть...", command=self.get_folder)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Закрыть программу", command=self.close_main_win)

        self.tdd_menu.add_cascade(label="Файл", menu=self.filemenu)
