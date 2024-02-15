def string_comparator(word1, word2):                    #funkcja porównuje dwa podane słowa
    if len(word1) == len(word2) and word1 != word2:     #jeśli długość słów jest taka sama ale słowa się różnią funkcja zwraca daną wiadomość
        return 'Słowa się nie zgadzają'
    elif len(word1) == len(word2) and word1 == word2:   #jeśli długość słów jest taka sama i słowa się zgadzają funkcja zwraca daną wiadomość
        return 'Słowa się zgadzają'
    else:                                               #jeśli słowa mają różną długość funkcja zwraca daną wiadomość
        return 'Słowa mają różną długość'

print(string_comparator('abcd', 'abdde'))
