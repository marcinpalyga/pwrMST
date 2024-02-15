import string
import random
def haslo():
        litery = ''.join((random.choice(string.ascii_letters)) for i in range(3)) #wybieramy losowe znaki do naszego hasła
        cyfry = ''.join((random.choice(string.digits)) for i in range(3))
        znaki = ''.join((random.choice(string.punctuation)) for i in range(2))
        haslo = litery + cyfry + znaki
        lista = list(haslo)
        random.shuffle(lista) #zmieniamy losowo kolejność znaków w haśle
        randomhaslo = ''.join(lista)
        return randomhaslo

print(haslo())