import random
import math

class Vector():
    def __init__(self, size):
        """Konstruktor"""
        self.size = size
        self.axis = []



    def random(self):
        """Metoda do losowej generacji elementów wektora """
        for i in range(self.size):
            os = random.randint(-15, 15)
            self.axis.append(os)
        return self.axis

    def overwrite(self):
        """Metoda do wczytywania elementów wektora z listy podanej jako argument"""
        axisoverwrite = []
        listinput = input("Podaj współrzędne wektora oddzielając je spacją: ").split(" ")
        if len(listinput) == self.size:
            for coordinate in listinput:
                coordinate = int(coordinate)
                axisoverwrite.append(coordinate)
            self.axis = axisoverwrite
            return self.axis
        else:
            raise ValueError("Podany wektor jest innego wymiaru")
    def __add__(self, other):
        """Operator dodawania dwóch wektorów"""
        equal = []
        if self.size == other.size:
            for i in range(self.size):
               x = self.axis[i] + other.axis[i]
               equal.append(x)
            return equal 
        else:
            raise ValueError("Wektory są różnego wymiaru") 

    def __sub__(self, other):
        """Operator odejmowania dwóch wektorów"""
        equal = []
        if self.size == other.size:
            for i in range(self.size):
               x = self.axis[i] - other.axis[i]
               equal.append(x)
            return equal 
        else:
            raise ValueError("Wektory są różnego wymiaru") 

    def __mul__(self, scalar):
        """Mnożenie wektora przez skalar"""
        equal = []
        for i in range(self.size):
           x = self.axis[i]*scalar
           equal.append(x)
        return equal 

    def size(self):
        """Metoda sprawdzająca rozmiar"""
        return self.size

    def length(self):
        """Metoda wyliczającą długość wektora"""
        x = 0
        for i in range(self.size):
            x = x + (self.axis[i])**2
        dlugosc = math.sqrt(x)
        return dlugosc

    def sum(self):
        """Metoda wyliczającą sumę elementów wektora"""
        x = 0
        for i in range(self.size):
            x += self.axis[i]
        return x

    def __str__(self):
        """Reprezentacja tekstowa wektora - co się dzieje gdy zrobimy str(nasz_obiekt)"""
        return f"{self.axis}"

    def __repr__(self):
        """Reprezentacja tekstowa wektora - co się dzieje gdy zrobimy print(nasz_obiekt)"""
        return f"{self.axis}"

    def scalar_product(self, other):
        """Metoda wyliczającą iloczyn skalarny dwóch wektorów"""
        prod = 0
        if self.size == other.size:
            for i in range(self.size):
                x = self.axis[i]*other.axis[i]
                prod += x
            return prod
        else:
            raise ValueError("Wektory są różnego wymiaru")
    def __getitem__(self, a):
        """Operator [] pozwalający na dostęp do konkretnych elementów wektora"""
        if a <= self.size and a>0:
            return self.axis[a-1]
        else:
            raise IndexError("Wektor jest mniejszego wymiaru")

    def __contains__(self, a):
        """Operator in sprawdzający przynależność elementu do wektora."""
        for element in self.axis:
            if element == a:
                return True
            else:
                return False
                
