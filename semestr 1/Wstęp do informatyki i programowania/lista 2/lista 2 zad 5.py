import time                                             #zaimportowanie modułu time

def my_counter(word, letter):                           #funkcja z zadania 4.                   
    start = time.time()                                 #moduł time zaczyna odliczanie czasu potrzebne funkcji na wykonanie zadania 10**5 raza
    for i in range(10**5):
        results = 0
        for i in range(len(word)):
            if word[i] == letter:
                results = results + 1
    end = time.time()                                   #moduł time zaczyna odliczanie czasu potrzebne funkcji na wykonanie zadania
    return results, end-start                           #funkcja zwraca ilość występowania litery w słowie i czas potrzebny na wykonanie zadania

print(my_counter('abbabb', 'b'))


def python_counter(word,letter):                        #funkcja sprawdzająca ilość występowania litery za pomocą funkcji .count oraz czas potrzebny na wykonanie zadania 10**5 raza
    start = time.time()
    for i in range(10**5):
        end = time.time()
    return word.count(letter), end-start                
print(python_counter('abbabb', 'b'))

