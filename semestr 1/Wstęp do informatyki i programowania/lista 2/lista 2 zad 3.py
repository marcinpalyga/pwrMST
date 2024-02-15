def character_finder(word, letter, start):      #funkcja sprawdza indeks podanej litery w danym słowie i rozpoczyna działanie od podanego indeksu
    results = []
    for i in range(start,len(word)):            #funkcja sprawdza każdą literę po kolei zaczynając od podanego indeksu i zapisuje ten indeks
        if word[i] == letter:
            results.append(i)
    return results                              #funkcja zwraca zapisane indeksy

print(character_finder('aaadaaa','a', 4))
