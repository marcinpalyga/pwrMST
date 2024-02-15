def html(r, g, b):
    def dectohex(n): #funkcja zamieniająca jedną część trypletu na system 16
        d = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'} #słownik przyporządkowujący liczby większe od 9 odpowiednim literom
        x = n//16 #zmienna która liczy ile wielokrotności 16 zmieści się w podanym n
        y = n - x*16 #zmienna która liczy resztę z dzielenia przez 16
        if x >= 10 and x <= 15: #jeśli x jest w danym przedziale liczba zostaje przyporządkowana literze
            x = d[x]
        if y >= 10 and y <= 15: #jeśli y jest w danym przedziale liczba zostaje przyporządkowana literze
            y = d[y]
        h = str(x) + str(y) #składamy stringi w jeden
        return h
    html = f'#{dectohex(r)}{dectohex(g)}{dectohex(b)}' #zmienna zamieniająca tryplet rgb na html
    return html
print(html(0,255,5))
    
