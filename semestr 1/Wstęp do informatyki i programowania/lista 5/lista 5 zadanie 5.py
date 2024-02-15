def palindrom(word):
    word=word.lower() #zmieniamy wszystkie litery na małe
    new_word=''.join(char for char in word if char.isalnum()) #usuwamy tą funkcją wszystkie znaki specjalne
    for i in range(1,len(word)): #pętla sprawdzająca czy odpowiednie indeksy słowa się zgadzają
        if new_word[i-1] == new_word[-i]:
            continue
        else:
            return 'Słowo nie jest palindromem!'
    return 'Słowo jest palindromem!'
print(palindrom('11:11'))
