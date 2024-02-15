def character_finder(word, letter): #funkcja wskazuje indeks litery w danym słowie
    results = []
    for i in range(len(word)):      #funkcja sprawdza indeks do ostatniej litery słowa
        if word[i] == letter:       #jeśli index podana litera znajduje się w danym słowie funkcja zapisuje jej indeks
            results.append(i)
    return results                  #funkcja zwraca zapisane indeksy

print(character_finder('abdcd','d'))
