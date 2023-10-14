import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
from bzip2 import BZ2

class App:
    def __init__(self, master):
        self.master = master
        self.setupgui()
        self.selected_path = ""

    def setupgui(self):
        self.master.title("bz2 converter")
        self.select_button = tk.Button(self.master, text="Select path", command=self.select_path)
        self.select_button.pack(expand=True, ipadx=50, ipady=10)

        self.convert_button = tk.Button(self.master, text="Convert", command=lambda:BZ2.compress_folder(self.selected_path))
        self.convert_button.pack(expand=True, ipadx=50, ipady=10)
        self.convert_button['state'] = 'disabled'

    def select_path(self):
        self.selected_path = filedialog.askdirectory()

        if self.selected_path != "":
            self.convert_button['state'] = "normal"

root = tk.Tk()
app = App(root)
root.geometry("250x250")