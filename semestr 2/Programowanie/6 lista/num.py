import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.font as font
from Equation import Expression

def calc():
    def retrieve():
        x = np.arange(-5, 5, 0.1)
        equations = label.get().split(';')
        np_eq = []
        for equation in equations:
            if equation == 'ln(x)':
                plt.plot(x, np.log(x), color = 'r')
                plt.xlim(-5, 5)
                plt.ylim(-5, 5)
                plt.grid(True)
                plt.xlabel('X')
                plt.ylabel('Y')
            else:
                equation = Expression(equation)
                np_eq.append(equation)
        for i in np_eq:
            y = i(x)
            print(type(y))
            if type(y) == int or type(y) == float:
                plt.axhline(y, color = 'y')
            else:
                plt.plot(x, y)
            plt.legend(equations)
            plt.xlim(-5, 5)
            plt.ylim(-5, 5)
            plt.grid(True)
            plt.xlabel('X')
            plt.ylabel('Y')
        plt.show()
        

    root = tk.Tk()
    root.geometry("800x700")
    root.title("Graphing calculator")
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)
    root.columnconfigure(2, weight = 1)
    root.columnconfigure(3, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 1)
    root.rowconfigure(3, weight = 1)
    root.rowconfigure(4, weight = 1)
    root.rowconfigure(5, weight = 1)

    buttonfont = font.Font(family = 'Cambria', size = 20)
    graphfont = font.Font(family = 'Cambria', size = 20)
    labelfont = font.Font(family = 'Cambria', size = 20)

    label = tk.Entry(root, font = labelfont)
    label.grid(column = 0, row = 0, columnspan = 4, sticky = 'NSEW')

    plus = tk.Button(root, text = '+', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '+'))
    plus.grid(column=0, row = 1, sticky = 'NSEW', padx = 5, pady = 5)

    minus = tk.Button(root, text = '-', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '-'))
    minus.grid(column = 1, row = 1, sticky = 'NSEW', padx = 5, pady = 5)

    div = tk.Button(root, text = '/', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '/'))
    div.grid(column = 2, row = 1, sticky = 'NSEW', padx = 5, pady = 5)

    multi = tk.Button(root, text = '*', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '*'))
    multi.grid(column = 3, row = 1, sticky = 'NSEW', padx = 5, pady = 5)

    sin = tk.Button(root, text = 'sin(x)', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'sin(x)'))
    sin.grid(column = 0, row = 2, sticky = 'NSEW', padx = 5, pady = 5)

    cos = tk.Button(root, text = 'cos(x)', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'cos(x)'))
    cos.grid(column = 1, row = 2, sticky = 'NSEW', padx = 5, pady = 5)

    e = tk.Button(root, text = 'e^x', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'e^x'))
    e.grid(column = 2, row = 2, sticky = 'NSEW', padx = 5, pady = 5)

    lnx = tk.Button(root, text = 'ln(x)', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'ln(x)'))
    lnx.grid(column = 3, row = 2, sticky = 'NSEW', padx = 5, pady = 5)

    nine = tk.Button(root, text = '9', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '9'))
    nine.grid(column = 0, row = 3, sticky = 'NSEW', padx = 5, pady = 5)
    
    eight = tk.Button(root, text = '8', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '8'))
    eight.grid(column = 1, row = 3, sticky = 'NSEW', padx = 5, pady = 5)

    seven = tk.Button(root, text = '7', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '7'))
    seven.grid(column = 2, row = 3, sticky = 'NSEW', padx = 5, pady = 5)

    six = tk.Button(root, text = '6', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '6'))
    six.grid(column = 0, row = 4, sticky = 'NSEW', padx = 5, pady = 5)

    five = tk.Button(root, text = '5', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '5'))
    five.grid(column = 1, row = 4, sticky = 'NSEW', padx = 5, pady = 5)

    four = tk.Button(root, text = '4', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '4'))
    four.grid(column = 2, row = 4, sticky = 'NSEW', padx = 5, pady = 5)

    three = tk.Button(root, text = '3', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '3'))
    three.grid(column = 0, row = 5, sticky = 'NSEW', padx = 5, pady = 5)

    two = tk.Button(root, text = '2', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '2'))
    two.grid(column = 1, row = 5, sticky = 'NSEW', padx = 5, pady = 5)

    one = tk.Button(root, text = '1', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '1'))
    one.grid(column = 2, row = 5, sticky = 'NSEW', padx = 5, pady = 5)

    zero = tk.Button(root, text = '0', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '0'))
    zero.grid(column = 3, row = 5, sticky = 'NSEW', padx = 5, pady = 5)

    graph = tk.Button(root, text = 'G\nR\nA\nP\nH', fg = 'white', bg = 'blue', font = graphfont, command = lambda: retrieve())
    graph.grid(column = 3, row = 3, rowspan = 2, sticky = 'NSEW', padx = 5, pady = 5)

    root.mainloop()

calc()