# -*- encoding:utf-8 -*-

import tkinter as tk
from tkinter import filedialog

from importdata import transfer

class Dataprocess():
    def __init__(self):
        self.top = tk.Tk()
        self.label = tk.Label(self.top, text='输出数据')
        self.label.pack()

        self.btn1 = tk.Button(self.top, text='选择原始文件', command=self.openfile)
        self.btn1.pack()

        self.btn2 = tk.Button(self.top, text='输出文件', command=self.output)
        self.btn2.pack()

    def openfile(self):
        self.filepath = filedialog.askopenfilename(title='选择原始文件')
        return self.filepath


    def output(self):
        transfer(self.filepath)


def main():
    process = Dataprocess()
    tk.mainloop()


if __name__ == "__main__":
    main()