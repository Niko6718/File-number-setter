from tkinter import *

from FrontEnd.filename_list import file_names_list_class as f_n_l
from FrontEnd.inst_pan import inst_pan_class as i_p
from FrontEnd.top_drop_down_menu import top_drop_down_menu_class as t_d_d_m

from BackEnd.top_drop_down_menu_back import top_drop_down_menu_back_class as t_d_d_m_back
from BackEnd.inst_pan_back import inst_pan_back_class as i_p_back


class main_window(f_n_l,
                  i_p, i_p_back,
                  t_d_d_m, t_d_d_m_back):
    def __init__(self,
                 main_win_width=800, main_win_height=600,
                 main_win_resize_x=True, main_win_resize_y=True, min_size_flag=False,
                 main_win_title="Files number setter", main_win_color='white'):
        # Параметры ...

        # ... главного окна
        self.main_win_width = main_win_width
        self.main_win_height = main_win_height
        self.main_win_resize_x = main_win_resize_x
        self.main_win_resize_y = main_win_resize_y
        self.min_size_flag = min_size_flag
        self.main_win_title = main_win_title
        self.main_win_color = main_win_color

        # ... рамок
        self.frames_padx = 2
        self.frames_pady = 2
        self.frames_color = 'gray'
        self.frames_border_color = 'black'
        self.frames_border_thick = 1

        # ... внутренние переменные
        self.files_names = None
        self.files_name_dir = None
        self.files_num = 0
        self.sumbols_num = 0

        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close_main_win)

    def open_main_win(self):
        # Размеры и положение
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        main_x = screen_width/2 - self.main_win_width/2
        main_y = screen_height/2 - self.main_win_height/2
        self.root.geometry("+%d+%d" % (main_x, main_y))
        self.root.geometry(str(self.main_win_width) + 'x' + str(self.main_win_height))
        if self.main_win_resize_y == 'True':
            self.root.minsize(self.main_win_width, self.main_win_height)
        else:
            self.root.minsize(0, 0)
        self.root.resizable(width=self.main_win_resize_x, height=self.main_win_resize_y)

        # Наименование и иконка
        self.root.title(self.main_win_title)

        # Список названий файлов
        f_n_l.__init__(self)

        # Панелька инструментов
        i_p.__init__(self)

        # Верхнее меню
        t_d_d_m.__init__(self)
        t_d_d_m_back.__init__(self)

        # Открытие основоного окна
        self.root.mainloop()

    def close_main_win(self, event=None):
        self.root.destroy()
        print("Закрыл")
