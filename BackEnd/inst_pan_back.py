from tkinter import *
import copy
import os


class inst_pan_back_class():
    def __init__(self):
        pass

    def num_defenition(self):
        old_names = copy.deepcopy(self.files_names)
        i = 0
        while i < self.files_num:
            # Удаляем символы до "_"
            j = 0
            while j < self.sumbols_num+1:
                try:
                    if self.files_names[i][j] == '_':
                        try:
                            temp = int(self.files_names[i][:j])
                        except:
                            break
                        self.files_names[i] = self.files_names[i][j+1:]
                        break
                except:
                    return
                j += 1

            k = copy.deepcopy(i+1)
            cur_sumbols = 0
            while k >= 1:
                cur_sumbols += 1
                k /= 10

            if cur_sumbols != self.sumbols_num:
                self.files_names[i] = str(i+1)+'_'+self.files_names[i]
                l = self.sumbols_num - cur_sumbols
                while l!=0:
                    self.files_names[i] = '0'+self.files_names[i]
                    l -= 1
            else:
                self.files_names[i] = str(i+1) + '_' + self.files_names[i]

            i += 1

        # Отображаем новый список
        i = 0
        self.files_name_list.delete(0, END)
        while i < len(self.files_names):
            self.files_name_list.insert(i, self.files_names[i])
            i += 1

        # Переименовываем файлы
        i = 0
        while i < len(self.files_names):
            try:
                os.renames(self.files_name_dir+'/'+old_names[i], self.files_name_dir+'/'+self.files_names[i])
            except:
                return
            i += 1

    def num_delete(self):
        old_names = copy.deepcopy(self.files_names)
        i = 0
        while i < self.files_num:
            j = 0
            while j < len(self.files_names[i]):
                try:
                    if self.files_names[i][j] == '_':
                        try:
                            temp = int(self.files_names[i][:j])
                        except:
                            break
                        self.files_names[i] = self.files_names[i][j+1:]
                        break
                except:
                    return
                j += 1

             # Заменяем символы "_" на пробел
            self.files_names[i] = self.files_names[i].replace('_', ' ')
            try:
                os.renames(self.files_name_dir + '/' + old_names[i], self.files_name_dir + '/' + self.files_names[i])
            except:
                pass
            i += 1

        # Отображаем новый список
        i = 0
        self.files_name_list.delete(0, END)
        while i < len(self.files_names):
            self.files_name_list.insert(i, self.files_names[i])
            i += 1
