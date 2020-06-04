from tkinter import *

class inst_pan_class():
    def __init__(self):
        self.parent = self.root
        self.__frames_color = self.frames_color
        self.__frames_padx = self.frames_padx
        self.__frames_pady = self.frames_pady

        self.__inst_pan_frame = Frame(self.parent, bg=self.__frames_color, width=105)

        # Элементы присвоения номера, удаления нумерации
        self.__inst_pan_frame_P1 = Frame(self.__inst_pan_frame, bg=self.__frames_color)
        self.__num_define_but = Button(self.__inst_pan_frame_P1, text="Пронумеровать", command=self.num_defenition)
        self.__num_delete_but = Button(self.__inst_pan_frame_P1, text="Удалить нумерацию", command=self.num_delete)

        self.__pack_elements()

    def __pack_elements(self):
        self.__inst_pan_frame.pack(side=LEFT, padx=self.__frames_padx, pady=self.__frames_pady, fill=BOTH)

        # Элементы присвоения номера, удаления нумерации
        self.__inst_pan_frame_P1.pack(side=TOP, padx=self.__frames_padx, pady=self.__frames_pady, fill=BOTH)
        self.__num_define_but.pack(side=TOP, padx=1, pady=1, fill=BOTH)
        self.__num_delete_but.pack(side=TOP, padx=1, pady=1, fill=BOTH)
