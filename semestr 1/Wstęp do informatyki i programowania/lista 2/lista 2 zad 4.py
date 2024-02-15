def my_counter(word, letter):           #funkcja sprawdzająca ilość występowania litery w słowie
    results = 0
    for i in range(len(word)):          #funkcja sprawdza ilość wystąpień od pierwszej do ostaniej litery słowa
        if word[i] == letter:
            results = results + 1       #jeśli litera występuje w słowie funkcja zapisuje ile razy i zwraca tę wartość
    return results

print(my_counter('abbabbb', 'b'))
