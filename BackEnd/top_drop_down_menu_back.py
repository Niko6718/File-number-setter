from tkinter import *

from tkinter import filedialog as fd
import copy
import os


class top_drop_down_menu_back_class():
    def __init__(self):
        pass

    def get_folder(self):
        self.files_name_dir = fd.askdirectory(title='Укажите дирректорию с файлами')
        try:
            files = os.listdir(self.files_name_dir)
        except:
            self.files_name_dir = None
            return
        # Очищаем спиоск
        self.files_name_list.delete(0, END)

        # Заполянем список
        self.files_names = copy.deepcopy(files)
        i = 0
        while i < len(self.files_names):
            self.files_name_list.insert(i, self.files_names[i])
            i += 1

        # Определяем число файлов и число символов в номере
        self.files_num = len(self.files_names)
        self.sumbols_num = 0
        j = self.files_num
        while j >= 1:
            self.sumbols_num += 1
            j /= 10
        print(self.sumbols_num)

        # Выставляем текущую директорию в названии
        self.root.title(self.main_win_title+' '+self.files_name_dir)

