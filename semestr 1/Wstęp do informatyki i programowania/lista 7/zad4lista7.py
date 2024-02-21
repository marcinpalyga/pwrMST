import sys
import pygame

#Rozmiar okna
SZEROKOSC = 1200
WYSOKOSC = 600

#Rozmiar rakiety
SZEROKOSC_RAKIETY = WYSOKOSC_RAKIETY = 32

class Rocket:
    
    #inicjalizujemy klasę
    def __init__(self, x = 0, y = 0, xpredkosc = 0, ypredkosc = 0) -> None:
        self.x = x
        self.y = y
        self.xpredkosc = xpredkosc
        self.ypredkosc = ypredkosc
    
    #funkcja przesuwająca rakietę
    def przesun(self):
        self.x += self.xpredkosc
        self.y += self.ypredkosc
        
    #funkcja nadająca rakiecie przyspieszenie
    def przyspiesz(self, x, y):
        self.xpredkosc = self.xpredkosc + x if self.xpredkosc <= 1 else self.xpredkosc
        self.ypredkosc = self.ypredkosc + y if self.ypredkosc <= 1 else self.ypredkosc

    #funkcja symulująca siłę oporu
    def zwolnij(self):
        self.xpredkosc *= 0.8
        self.ypredkosc *= 0.8

    #funkcja utrzymująca rakietę na ekranie
    def granice(self):

        if self.x <= 0 or self.x + SZEROKOSC_RAKIETY >= SZEROKOSC:
            self.xpredkosc = -self.xpredkosc
        if self.y <= 0 or self.y + WYSOKOSC_RAKIETY >= WYSOKOSC:
            self.ypredkosc = -self.ypredkosc

    #funkcja pozwalająca na grę
    def graj(self):
        
        pygame.init()
        
        #utworzenie okienka
        ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
        pygame.display.set_caption("RAKIETA")
        ikona = pygame.image.load('semestr 1/Wstęp do informatyki i programowania/lista 7/rakieta.png')
        pygame.display.set_icon(ikona)
        rakieta = pygame.image.load('semestr 1/Wstęp do informatyki i programowania/lista 7/rakieta.png')
        framecount = 0
        n = 0
        RAKIETA = pygame.transform.rotate(rakieta, n)
        
        
        running = True
        while running:

            #przypisanie klawiszy do ruchu rakiety i zapewnienie obrotu rakiety w odpowiednią stronę
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False

                klawisz=pygame.key.get_pressed()

                if klawisz[pygame.K_UP]:
                    self.przyspiesz(0, -0.3)
                    RAKIETA = pygame.transform.rotate(rakieta, 0)                        

                elif klawisz[pygame.K_DOWN]:
                    self.przyspiesz(0, 0.3)
                    RAKIETA = pygame.transform.rotate(rakieta, 180)

                elif klawisz[pygame.K_RIGHT]:
                    self.przyspiesz(0.3, 0)
                    RAKIETA = pygame.transform.rotate(rakieta, 270)
                    
                elif klawisz[pygame.K_LEFT]:
                    self.przyspiesz(-0.3, 0)
                    RAKIETA = pygame.transform.rotate(rakieta, 90)
                    
                    
                elif klawisz[pygame.K_ESCAPE]:
                    running = False            

            self.przesun()
            self.granice()

            if framecount % 100 == 0:
                self.zwolnij()

            #przedstawienie rakiety na ekranie
            self.pozycja = [self.x, self.y]
            ekran.fill((150, 210, 255))
            ekran.blit(RAKIETA, self.pozycja)
            pygame.display.update()

            framecount += 1



def main():

    rakieta = Rocket(SZEROKOSC/2, WYSOKOSC/2)
    rakieta.graj()

if __name__ == '__main__':
    main()
