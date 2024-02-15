import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.font as font

def isfloat(num):
    '''Funkcja sprawdzająca czy funkcja podana w kalkulatorze graficznym jest stałą'''
    try:
        float(num)            #sprawdzamy czy możemy zmienić funkcje na float
        return True           #jeśli tak to zwracamy True, jeśli nie to False
    except ValueError:
        return False

def calc():
    '''Funkcja zawierająca całe GUI i funkcje związane z przyciskami i miejscem do wpisywania funkcji'''
    def retrieve():
        '''Funkcja zawierająca wszystkie przypadki, które dzieją się po kliknięciu przycisku "graph"'''
        legendlist = label.get().split(';')         #z głównego napisu ściągamy string wszystkich funkcji
        try:
            leftlim = float(leftx.get())            #zmieniamy lewą granicę funkcji ze stringa na float, jeśli nie możemy wyrzucamy błąd
        except:
            label.insert('end', '; left limit is not a int or float')
        try:
            rightlim = float(rightx.get())          #zmieniamy prawą granicę funkcji ze stringa na float, jeśli nie możemy wyrzucamy błąd
        except:
            label.insert('end', '; right limit is not a int or float')
        try:
            upperlim = float(uppery.get())          #zmieniamy górna granicę funkcji ze stringa na float, jeśli nie możemy wyrzucamy błąd
        except:
            label.insert('end', '; upper limit is not a int or float')
        try:
            lowerlim = float(lowery.get())          #zmieniamy dolną granicę funkcji ze stringa na float, jeśli nie możemy wyrzucamy błąd
        except:
            label.insert('end', '; lower limit is not a int or float')    
        try:
            equations = label.get()                 #zmieniamy elementy funkcji na elementy z biblioteki numpy
            equations = equations.replace('sin', 'np.sin') 
            equations = equations.replace('cos', 'np.cos')
            equations = equations.replace('sqrt', 'np.sqrt')
            equations = equations.replace('e', 'np.e')
            equations = equations.replace('^', '**')
            if ';' in equations:
                equation = equations.split(';')  #jeśli w stringu głównym znajduje się ';' rozdzielami string na pojedyncze funkcje
                for function in equation:
                    if isfloat(function) == True: #sprawdzamy czy funkcja jest stała, jeśli tak plotujemy na wykresie stałą
                        plt.axhline(float(function), color = 'y')
                        plt.xlim(leftlim, rightlim)
                        plt.ylim(lowerlim, upperlim)
                        plt.grid(True)
                        plt.xlabel('X')
                        plt.ylabel('Y')
                    else:
                        x = np.linspace(leftlim, rightlim, 10000) #jeśli nie plotujemy funkcje w zależności od x
                        y = (function)
                        plt.plot(x, y)
                        plt.xlim(leftlim, rightlim)
                        plt.ylim(lowerlim, upperlim)
                        plt.title("Graphing Calculator")
                        plt.grid(True)
                        plt.xlabel('X')
                        plt.ylabel('Y')
            else:
                if isfloat(equations) == True: #jeśli podano jedną funkcję plotujemy ją na wykres sprawdzając czy jest ona stałą czy nie jak powyżej
                    plt.axhline(float(equation), color = 'y')
                    plt.xlim(leftlim, rightlim)
                    plt.ylim(-5, 5)
                    plt.grid(True)
                    plt.xlabel('X')
                    plt.ylabel('Y')
                else:
                    x = np.linspace(leftlim, rightlim, 10000)
                    plt.plot(x, (equations))
                    plt.xlim(leftlim, rightlim)
                    plt.ylim(lowerlim, upperlim)
                    plt.title("Graphing Calculator")
                    plt.grid(True)
                    plt.xlabel('X')
                    plt.ylabel('Y')
        except:
            label.insert('end', 'Invalid input of functions') #jeśli input funkcji jest niepoprawny wyrzucamy błąd
        if legendvar.get() == 1:
            plt.legend(legendlist) #jeśli checkbox związany z legendą jest zaznaczony dodajemy ją
        plt.show()
                

    root = tk.Tk() #tworzymy okno z tytułem i układem wszystkich kolumn i rzędów w których będziemy ustawiać przyciski
    root.geometry("1100x700")
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
    root.rowconfigure(6, weight = 1)
    root.rowconfigure(7, weight = 1)

    buttonfont = font.Font(family = 'Cambria', size = 20) #tworzymy czcionki do danego przycisku/inputu
    graphfont = font.Font(family = 'Cambria', size = 20)
    labelfont = font.Font(family = 'Cambria', size = 20)
    axisfont = font.Font(family = 'Cambria', size = 12)

    label = tk.Entry(root, font = labelfont) #Miejsce do wpisania funkcji
    label.grid(column = 0, row = 0, columnspan = 3, sticky = 'NSEW')

    legendvar = tk.IntVar() #Checkbox z legendą
    legend = tk.Checkbutton(root, font = buttonfont, text = 'Turn legend on/off', onvalue = 1, offvalue = 0, variable = legendvar)
    legend.grid(column = 3, row = 0) 

    leftvar = tk.StringVar() #lewa granica
    leftvar.set('Set a left limit on X axis')
    leftx = tk.Entry(root, font = axisfont, textvariable = leftvar)
    leftx.grid(column = 0, row = 1, padx = 5, pady = 5)
    
    rightvar = tk.StringVar() #prawa granica
    rightvar.set('Set a right limit on X axis')
    rightx = tk.Entry(root, font = axisfont, textvariable = rightvar)
    rightx.grid(column = 1, row = 1, padx = 5, pady = 5) 

    lowervar = tk.StringVar() #dolna granica
    lowervar.set('Set a lower limit on Y axis')
    lowery = tk.Entry(root, font = axisfont, textvariable = lowervar)
    lowery.grid(column = 2, row = 1, padx = 5, pady = 5)
    
    uppervar = tk.StringVar() #górna granica
    uppervar.set('Set a left limit on X axis')
    uppery = tk.Entry(root, font = axisfont, textvariable = uppervar )
    uppery.grid(column = 3, row = 1, padx = 5, pady = 5)

    plus = tk.Button(root, text = '+', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '+'))
    plus.grid(column=0, row = 2, sticky = 'NSEW', padx = 5, pady = 5) #'+'

    minus = tk.Button(root, text = '-', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '-'))
    minus.grid(column = 1, row = 2, sticky = 'NSEW', padx = 5, pady = 5) #'-'

    div = tk.Button(root, text = '/', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '/'))
    div.grid(column = 2, row = 2, sticky = 'NSEW', padx = 5, pady = 5) #'/'

    multi = tk.Button(root, text = '*', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '*'))
    multi.grid(column = 3, row = 2, sticky = 'NSEW', padx = 5, pady = 5) #'*'

    left = tk.Button(root, text = '(', fg = 'white', bg='black', font = buttonfont, command = lambda: label.insert('end', '('))
    left.grid(column = 0, row = 3, sticky = 'NSEW', padx = 5, pady = 5) #lewy nawias

    right = tk.Button(root, text = ')', fg = 'white', bg='black', font = buttonfont, command = lambda: label.insert('end', ')'))
    right.grid(column = 1, row = 3, sticky = 'NSEW', padx = 5, pady = 5) #prawy nawias

    power = tk.Button(root, text = '^', fg = 'white', bg='black', font = buttonfont, command = lambda: label.insert('end', '^'))
    power.grid(column = 2, row = 3, sticky = 'NSEW', padx = 5, pady = 5) #'^'

    var = tk.Button(root, text = 'x', fg = 'white', bg='black', font = buttonfont, command = lambda: label.insert('end', 'x'))
    var.grid(column = 3, row = 3, sticky = 'NSEW', padx = 5, pady = 5) #'x'

    sin = tk.Button(root, text = 'sin(x)', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'sin(x)'))
    sin.grid(column = 0, row = 4, sticky = 'NSEW', padx = 5, pady = 5) #sinus

    cos = tk.Button(root, text = 'cos(x)', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'cos(x)'))
    cos.grid(column = 1, row = 4, sticky = 'NSEW', padx = 5, pady = 5) #cosinus

    e = tk.Button(root, text = 'e^x', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'e^x'))
    e.grid(column = 2, row = 4, sticky = 'NSEW', padx = 5, pady = 5) #e do potęgi x

    sqrt = tk.Button(root, text = 'sqrt(x)', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', 'sqrt(x)'))
    sqrt.grid(column = 3, row = 4, sticky = 'NSEW', padx = 5, pady = 5) #pierwiastek z x

    nine = tk.Button(root, text = '9', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '9'))
    nine.grid(column = 0, row = 5, sticky = 'NSEW', padx = 5, pady = 5) #'9'
    
    eight = tk.Button(root, text = '8', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '8'))
    eight.grid(column = 1, row = 5, sticky = 'NSEW', padx = 5, pady = 5) #'8'

    seven = tk.Button(root, text = '7', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '7'))
    seven.grid(column = 2, row = 5, sticky = 'NSEW', padx = 5, pady = 5) #'7'

    six = tk.Button(root, text = '6', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '6'))
    six.grid(column = 0, row = 6, sticky = 'NSEW', padx = 5, pady = 5) #'6'

    five = tk.Button(root, text = '5', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '5'))
    five.grid(column = 1, row = 6, sticky = 'NSEW', padx = 5, pady = 5) #'5'

    four = tk.Button(root, text = '4', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '4'))
    four.grid(column = 2, row = 6, sticky = 'NSEW', padx = 5, pady = 5) #'4'

    three = tk.Button(root, text = '3', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '3'))
    three.grid(column = 0, row = 7, sticky = 'NSEW', padx = 5, pady = 5) #'3'

    two = tk.Button(root, text = '2', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '2'))
    two.grid(column = 1, row = 7, sticky = 'NSEW', padx = 5, pady = 5) #'2'

    one = tk.Button(root, text = '1', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '1'))
    one.grid(column = 2, row = 7, sticky = 'NSEW', padx = 5, pady = 5) #'1'

    zero = tk.Button(root, text = '0', fg = 'white', bg = 'black', font = buttonfont, command = lambda: label.insert('end', '0'))
    zero.grid(column = 3, row = 5, sticky = 'NSEW', padx = 5, pady = 5) #'0'

    graph = tk.Button(root, text = 'G\nR\nA\nP\nH', fg = 'white', bg = 'blue', font = graphfont, command = lambda: retrieve())
    graph.grid(column = 3, row = 6, rowspan = 2, sticky = 'NSEW', padx = 5, pady = 5) # przycisk do rysowania wykresów

    root.mainloop()

calc()