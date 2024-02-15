class Rocket:
    
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        
    def przesun(self, x, y):
        self.x += x 
        self.y += y


    def pozycja(self):
        return self.x, self.y

    def dystans(self, other):
        return ((self.x - other.x)**2 + (self.x - other.y)**2)**0.5
        
