from tkinter import ttk
import tkinter as tk
import requests
import json
import datetime
try:
    data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json() #probujemy pobrac dane z internetu i zapisujemy je w pliku typu json
    kursy = list(data['rates'])  #tworzymy liste nazw walut
    kursy1 = data['rates'] #odpowiadajace nazwom wartości
    with open('currency.json', 'w') as f:
        json.dump(data, f)
except:
    with open('currency.json', 'r+') as file:  #przy braku internetu odczytujemy dane z wczesniejszego zapisu
        data = json.load(file)
    kursy = list(data['rates'])
    kursy1 = data['rates']

def waluty():
    def potwierdz():  #funkcja zbierajaca dane po naciśnięciu przycisku potwierdź
        waluta_wymieniana = lista_walut.get()
        ilosc = ilosc_waluty.get()
        waluta_otrzymywana = lista_walut1.get()
        try:
            ilosc_float = abs(float(ilosc))
        except:
            wartosc = ttk.Label(okno, text = f'Niewłaściwe dane') #jesli w polu z ilością waluty znajdują się inne znaki niż liczby wyrzucamy błąd na ekran
            wartosc.config(font= ('TimesNewRoman', 20), background='violet')
            wartosc.pack()
        if waluta_wymieniana == 'Wybierz walutę' or waluta_otrzymywana =='Wybierz walutę' or ilosc =='': #jeśli któraś z wartości nie została wybrana wyrzucamy błąd na ekran
            wartosc = ttk.Label(okno, text = f'Niewłaściwe dane')
            wartosc.config(font= ('TimesNewRoman', 20), background='violet')
            wartosc.pack()
        else:
            waluta_wymieniana = lista_walut.get() 
            ilosc = float(ilosc_waluty.get())
            waluta_otrzymywana = lista_walut1.get()
            ilosc_float = ilosc / kursy1[waluta_wymieniana] #zamieniamy wartość waluty na odpowiadające im dolary które są podstawową walutą programu
            ilosc_float = round(ilosc_float*(kursy1[waluta_otrzymywana]), 2) #zamieniamy walutę i wyrzucamy na ekran napis z jej wartością
            wartosc = ttk.Label(okno, text = f'Za {ilosc} {waluta_wymieniana} otrzymasz {ilosc_float} {waluta_otrzymywana}')
            wartosc.config(font= ('TimesNewRoman', 15), background='violet')
            wartosc.pack()
        


        
    okno = tk.Tk() #tworzenie okna
    okno.geometry("800x400")
    okno.title("Zamiana walut")
    okno.config(bg='violet')
    
    napis_zamiana = ttk.Label(okno, text = 'Zamiana walut') #napis na samej górze
    napis_zamiana.config(font=('TimesNewRoman', 25), background='violet')
    napis_zamiana.pack()

    dzien = ttk.Label(okno, text = "Dzisiejsza data to: " + str(datetime.datetime.now().strftime('%d %B %Y'))) #napis z datą
    dzien.config(font=('TimesNewRoman', 20), background='violet')
    dzien.pack()

    napis_zamieniana = ttk.Label(okno, text = 'Waluta wymieniana') #napis z waluta wymieniana
    napis_zamieniana.config(font=('TimesNewRoman', 10), background='violet')
    napis_zamieniana.pack()

    lista_walut = ttk.Combobox(okno, values = kursy, width = 35, state = 'readonly') #rozwijana lista walut
    lista_walut.set('Wybierz walutę')
    lista_walut.config(font=('TimesNewRoman', 10), background='violet')
    lista_walut.pack(padx = 10, pady = 10)
 
    napis_zamieniona = ttk.Label(okno, text = 'Waluta wymieniona') #napis z waluta na którą zamieniamy
    napis_zamieniona.config(font=('TimesNewRoman', 10), background='violet')
    napis_zamieniona.pack()

    lista_walut1 = ttk.Combobox(okno, values = kursy, width = 35, state = 'readonly') #rozwijana lista walut
    lista_walut1.set('Wybierz walutę')
    lista_walut1.config(font=('TimesNewRoman', 10), background='violet')
    lista_walut1.pack(padx = 10, pady = 10)

    ilosc_waluty = tk.Entry(okno, width = 30, font=('TimesNewRoman')) #okno na wpisanie waluty
    ilosc_waluty.pack()
    
    przycisk = tk.Button(okno, text = "Potwierdź", command = lambda: potwierdz(), width = 10) #przycisk potwiedz
    przycisk.config(font=('TimesNewRoman', 10))
    przycisk.pack(padx = 10, pady = 10)
    
    okno.mainloop()
waluty()