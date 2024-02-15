import random
import pygame
import tkinter as tk
import tkinter.font as font


wynik = 0                                #zmienne globalne
wyniki_lista = [0,0,0,0,0]
def gra():                            #funkcja z grą
    pygame.init()                     
    pygame.mixer.init()        #przypisujemy dźwięki gry do zmiennych
    szer = 500                                         #rozmiary okna
    wys = 400
    okno_gra = pygame.display.set_mode((szer, wys))     #inicjujemy okno
    pygame.display.update()
    pygame.display.set_caption('Snake game')      #nazwa okna
    kwadrat = 10                              #wielkość kwadratu 
    pred = 10                               #częstość odświeżania się okna przy tym też prędkość węża
    czas = pygame.time.Clock()
    czcionka = pygame.font.SysFont('NewTimesRoman', 20)        #czcionka używana przy wiadomościach

    def wyswietl_wynik(wynik):
        wyswietl = czcionka.render(f'Twój wynik: {wynik}', True, (0,200,255))   #wyświetlenie wyniku na ekranie podczas gry
        okno_gra.blit(wyswietl, [szer/4,0])

    def przegrana_wiad(tekst, kolor):                             #funkcja, która pozwala nam później wyświetlić wiadomość przy przegranej
        wiad = czcionka.render(tekst, True, kolor)
        okno_gra.blit(wiad, [0, 0])

    def snake(kwadrat, lista):           #funkcja rysująca węża
        for i in lista:
            pygame.draw.rect(okno_gra, (0,255,0), [i[0], i[1], kwadrat, kwadrat])


    def petla_gra():
        wyjscie = False               #zmienne kontrolujące pętle
        przegrana = False

        global wynik

        x = szer/2           #pozycja startująca węża
        y = wys/2
        przejsciex = 0       #zmienna w której zapisujemy zmianę pozycji wężą względem pozycji początkowej
        przejsciey = 0
        lista = []
        dlugosc_waz = 1   #zmienna w której zapisujemy długość węża
        dobrex = round(random.randrange(10, szer - kwadrat)/10)*10    #losujemy współrzędne dobrego i złego jabłka
        dobrey = round(random.randrange(10, wys - kwadrat)/10)*10
        zlex = round(random.randrange(10, szer - kwadrat)/10)*10
        zley = round(random.randrange(10, wys - kwadrat)/10)*10
        while wyjscie == False:                    #pętla z grą
            while przegrana == True:              #jeśli użytkownik przegra wyświetlamy wiadomość z możliwym wyborem ponowej gry i powrotu do menu
                okno_gra.fill((0,0,0))
                przegrana_wiad("Przegrałeś! 1 - ponowna gra, 2 - wyjdź", (255,0,0))
                pygame.display.update()
    
                for event in pygame.event.get():             #pętla w która kontroluje wybór użytkownika po wyświetleniu wiadomości
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_2:
                            wyjscie = True
                            przegrana = False
                        if event.key == pygame.K_1:
                            petla_gra()
            for event in pygame.event.get():            #pętla kontrulująca ruch węża strzałkami
                if event.type == pygame.QUIT:
                    wyjscie = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        przejsciex = -kwadrat
                        przejsciey = 0
                    elif event.key == pygame.K_RIGHT:
                        przejsciex = kwadrat
                        przejsciey = 0
                    elif event.key == pygame.K_UP:
                        przejsciex = 0
                        przejsciey = -kwadrat
                    elif event.key == pygame.K_DOWN:
                        przejsciex = 0
                        przejsciey = kwadrat
            if x >= szer or x <= 0 or y <= 0 or y >= wys:     #if dzięki któremu uderzenie w bandy skutkuje przegraną
                przegrana = True
            x += przejsciex  #aktualizacja pozycji węża
            y += przejsciey
            okno_gra.fill((0,0,0))
            pygame.draw.rect(okno_gra, (255,0,0), [dobrex, dobrey, kwadrat, kwadrat])       #rysowanie dobrego i złego jabłka
            pygame.draw.rect(okno_gra, (255,255,255), [zlex, zley, kwadrat, kwadrat])
            snake_glowa = []
            snake_glowa.append(x)     #zapisanie współrzędnych pierwszego kwadratu
            snake_glowa.append(y)
            lista.append(snake_glowa)
            if len(lista) > dlugosc_waz:  
                del lista[0]

            for i in lista[:-1]:          #wejście w siebie skutkuje końcem gry
                if i == snake_glowa:
                    przegrana = True
            snake(kwadrat, lista)     #rysowanie węża
            wyswietl_wynik(dlugosc_waz - 1) #wyświetlanie wyniku
            pygame.display.update()
            if x == dobrex and y == dobrey:                        #zebranie dobrego jabłka co skutkuje wydłużeniem, po nim losujemy nowe miejsca złego i dobrego jabłka
                dobrex = round(random.randrange(kwadrat, szer - kwadrat)/10)*10
                dobrey = round(random.randrange(kwadrat, wys - kwadrat)/10)*10          
                zlex = round(random.randrange(kwadrat, szer - kwadrat)/10)*10
                zley = round(random.randrange(kwadrat, wys - kwadrat)/10)*10
                dlugosc_waz += 1
            if x == zlex and y == zley:           #zebranie złego jabłka co skutkuje porażką
                przegrana = True    
            czas.tick(pred)
        wynik = dlugosc_waz - 1    #zapisanie wyniku do listy, którą wyświetlamy w menu
        wyniki_lista.append(wynik)
        if wyjscie == True:
            pygame.display.quit()
    petla_gra()

def zasady():
    okno_zasady = tk.Toplevel()
    okno_zasady.geometry('500x400')                              #okno z zasadami gry w menu
    okno_zasady.configure(background = 'violet')
    okno_zasady.title('Zasady')
    okno_zasady.columnconfigure(0, weight = 1)
    okno_zasady.columnconfigure(1, weight = 1)
    okno_zasady.columnconfigure(2, weight = 1)
    okno_zasady.rowconfigure(0, weight = 1)

    czcionka_napis = font.Font(family = 'NewTimesRoman', size = 20)

    napis = tk.Label(okno_zasady, text = "Zasady \n 1. Nie możesz wejść w siebie \n 2. Nie możesz wejść w ściany.\n 3. Zbieraj czerwone jabłka aby urosnąć \n 4. Nie możesz zebrać białego jabłka", font = czcionka_napis, bg  = 'violet')
    napis.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = 'N')

def wyniki():
    global wyniki_lista
    wyniki_lista.sort(reverse = True)
    wyniki_okno = tk.Toplevel()
    wyniki_okno.configure(background = 'violet')        #okno z wynikami sesji gry
    wyniki_okno.geometry('500x400')
    wyniki_okno.title('Wyniki sesji')
    wyniki_okno.columnconfigure(0, weight = 1)
    wyniki_okno.columnconfigure(1, weight = 1)
    wyniki_okno.columnconfigure(2, weight = 1)
    wyniki_okno.rowconfigure(0, weight = 1)
    

    czcionka_napis = font.Font(family = 'NewTimesRoman', size = 30)
    
    napis = tk.Label(wyniki_okno, text = f'Najlepsze wyniki:\n 1. {wyniki_lista[0]}\n 2. {wyniki_lista[1]}\n 3. {wyniki_lista[2]}\n 4. {wyniki_lista[3]}\n 5. {wyniki_lista[4]}\n ', bg  = 'violet', font = czcionka_napis)
    napis.grid(column = 1, row = 0, padx = 55, pady = 5)

    wyniki_okno.mainloop()

def gui():
    global root
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Menu")
    root.configure(background = 'violet')
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)             #okno menu głównego
    root.columnconfigure(2, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 1)
    root.rowconfigure(3, weight = 1)
    root.rowconfigure(4, weight = 1)

    czcionka_napis = font.Font(family = 'NewTimesRoman', size = 30)
    czcionka_przycisk = font.Font(family = 'NewTimesRoman', size = 20)

    napis = tk.Label(root, text = 'SNAKE', font = czcionka_napis, bg  = 'violet')
    napis.grid(column = 1, row = 0, padx = 5, pady = 5)

    start_przycisk = tk.Button(root, text = 'Start', font = czcionka_przycisk, command = lambda: gra())
    start_przycisk.grid(column = 1, row = 1, padx = 5, pady = 5, sticky= 'NSEW')

    zasady_przycisk = tk.Button(root, text = 'Zasady', font = czcionka_przycisk, command = lambda: zasady())
    zasady_przycisk.grid(column = 1, row = 2, padx = 5, pady = 5, sticky = 'NSEW')

    wyniki_przycisk = tk.Button(root, text = 'Wyniki sesji', font = czcionka_przycisk, command = lambda: wyniki())
    wyniki_przycisk.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'NSEW')

    wyjście = tk.Button(root, text = 'Wyjdź', font = czcionka_przycisk, command = lambda: root.destroy())
    wyjście.grid(column = 1, row = 4, padx = 5, pady = 5, sticky = 'NSEW')

    root.mainloop()

gui()

