from tkinter import ttk
import tkinter as tk
import requests
import json
import datetime
try:
    data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = list(data['rates'])
    currencies1 = data['rates']
    with open('currency.json', 'w') as f:
        json.dump(data, f)
except:
    with open('currency.json', 'r+') as file:
        data = json.load(file)
    currencies = list(data['rates'])
    currencies1 = data['rates']

def gui():
    def retrieve():
        exchange_from = box.get()
        initial_amount = entry.get()
        exchange_to = box1.get()
        try:
            amount = float(initial_amount)
        except:
            value = ttk.Label(middleframe, text = f'Invalid input')
            value.config(font= ('Cambria', 20), background='lightblue')
            value.pack()
        if exchange_from == 'Pick currency' or exchange_to =='Pick currency' or initial_amount =='':
            value = ttk.Label(middleframe, text = f'Invalid input')
            value.config(font= ('Cambria', 20), background='lightblue')
            value.pack()
        else:
            exchange_from = box.get()
            initial_amount = float(entry.get())
            exchange_to = box1.get()
            amount = initial_amount / currencies1[exchange_from]
            amount = round(amount*(currencies1[exchange_to]), 2)
            value = ttk.Label(middleframe, text = f'For {initial_amount} {exchange_from} you will get {amount} {exchange_to}s')
            value.config(font= ('Cambria', 15), background='lightblue')
            value.pack()
        
    root = tk.Tk()
    root.geometry("1000x400")
    root.title("Currency Converter")
    root.config(bg='lightblue')
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=3)
    root.columnconfigure(3, weight=3)

    leftframe = tk.Frame(root)
    leftframe.columnconfigure(0, weight = 3)
    leftframe.grid(sticky='nw', pady = 50)
    leftframe.config(bg='lightblue')

    middleframe = tk.Frame(root)
    middleframe.columnconfigure(1, weight = 3)
    middleframe.config(bg='lightblue')

    rightframe = tk.Frame(root)
    rightframe.columnconfigure(2, weight = 3)
    rightframe.grid(sticky='ne', pady = 50)
    rightframe.config(bg='lightblue')
    
    label = ttk.Label(middleframe, text = 'Currency converter')
    label.grid(column = 1, row = 0)
    label.config(font=('Cambria', 25), background='lightblue')
    label.pack()

    date = ttk.Label(middleframe, text = "Today's date is: " + str(datetime.datetime.now().strftime('%d %B %Y')))
    date.config(font=('Cambria', 20), background='lightblue')
    date.pack()

    Label = ttk.Label(leftframe, text = 'Currency you want to exchange from:')
    Label.grid(column=0, row= 0)
    Label.config(font=('Cambria', 10), background='lightblue')
    Label.pack()

    box = ttk.Combobox(leftframe, values = currencies, width = 35, state = 'readonly')
    box.set('Pick currency')
    box.config(font=('Cambria', 10), background='lightblue')
    box.pack(padx = 10, pady = 5)

    entry = tk.Entry(middleframe, width = 30, font=('Cambria'), bd=5)
    entry.pack()
    
    button = tk.Button(middleframe, text = "Submit", command = lambda: retrieve(), width = 10,activebackground='#AAAAAA', cursor='hand1')
    button.config(font=('Cambria', 10))
    button.pack(padx = 10, pady = 10)

    Label = ttk.Label(rightframe, text = 'Currency you want to exchange to:')
    Label.config(font=('Cambria', 10), background='lightblue')
    Label.pack()

    box1 = ttk.Combobox(rightframe, values = currencies, width = 35, state = 'readonly')
    box1.set('Pick currency')
    box1.config(font=('Cambria', 10), background='lightblue')
    box1.pack(padx = 10, pady = 5)

    leftframe.grid(column=0,row=0)
    middleframe.grid(column=1, row=0)
    rightframe.grid(column=2, row=0)
    root.mainloop()
gui()