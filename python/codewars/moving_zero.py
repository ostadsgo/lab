def moving_zeros(a):
    print(sorted(a, key=lambda x: x == 0), reverse=True)


moving_zeros([1, 2, 3, 4, 0, 1, 1, 0])
##assert moving_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1
##                     ] == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

from tkinter import *
from tkinter import ttk
import tkinter as tk

clas Main(tk.Tk):
    def __init__(self, name, age=0):
        self.name = name 
        self.age = age
