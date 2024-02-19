import random
import pygame
import tkinter as tk
import tkinter.font as font
import os 

final_score = 0
color = '0,255,0'
speed = '20'
highscore_list = [0,0,0,0,0]
def start_game():
    pygame.init()
    pygame.mixer.init()
    width = 500
    height = 400
    game_root = pygame.display.set_mode((width, height))
    pygame.display.update()
    pygame.display.set_caption('Snake game')
    block = 10
    speed_set = int(speed)
    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont('Cambria', 20)

    def dis_score(score):
        value = score_font.render(f'Your score: {score}', True, (255,255,255))
        game_root.blit(value, [0,0])

    def snake(block, snake_list):
        for i in snake_list:
            pygame.draw.rect(game_root, tuple(map(int, color.split(','))), [i[0], i[1], block, block])


    def gameloop():
        game_over = False
        global final_score

        x = width/2
        y = height/2
        x_change = 0
        y_change = 0
        snake_list = []
        length_of_snake = 1
        foodx = round(random.randrange(10, width - block)/10)*10
        foody = round(random.randrange(10, height - block)/10)*10
        while game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -block
                    elif event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = block
            if x >= width or x <= 0 or y <= 0 or y >= height:
                game_over = True
            x += x_change
            y += y_change
            game_root.fill((0,0,0))
            pygame.draw.rect(game_root, (255,0,0), [foodx, foody, block, block])
            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for i in snake_list[:-1]:
                if i == snake_head:
                    game_over = True
            snake(block, snake_list)
            dis_score(length_of_snake - 1)
            pygame.display.update()
            if x == foodx and y == foody:
                foodx = round(random.randrange(block, width - block)/10)*10
                foody = round(random.randrange(block, height - block)/10)*10
                length_of_snake += 1
            clock.tick(speed_set)
        final_score = length_of_snake - 1

        highscore_list.append(final_score)
        pygame.quit()
    gameloop()

def rules_game():
    rules_root = tk.Tk()
    rules_root.geometry('500x400')
    rules_root.configure(background = 'green')
    rules_root.title('Rules')
    rules_root.columnconfigure(0, weight = 1)
    rules_root.columnconfigure(1, weight = 1)
    rules_root.columnconfigure(2, weight = 1)
    rules_root.rowconfigure(0, weight = 1)

    labelfont = font.Font(family = 'Cambria', size = 30)

    label = tk.Label(rules_root, text = "Rules:\n 1. You can't hit yourself\n 2.You can't hit walls\n 3. Eat apples to grow\n 4. Move using arrows", font = labelfont, bg  = 'green')
    label.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = 'N')

def settings_game():
    def get_settings():
        global speed, color
        color = snake_color.get()
        speed = snake_speed.get()
        return speed, color

    settings_root = tk.Toplevel(root)
    settings_root.configure(background = 'green')
    settings_root.geometry('500x400')
    settings_root.title('Settings')
    settings_root.columnconfigure(0, weight = 1)
    settings_root.columnconfigure(1, weight = 1)
    settings_root.columnconfigure(2, weight = 1)
    settings_root.rowconfigure(0, weight = 1)
    settings_root.rowconfigure(1, weight = 1)
    settings_root.rowconfigure(2, weight = 1)
    settings_root.rowconfigure(3, weight = 1)

    labelfont = font.Font(family = 'Cambria', size = 30)

    label = tk.Label(settings_root, text = 'Settings', font = labelfont, bg  = 'green')
    label.grid(column = 1, row = 0, padx = 5, pady = 5)

    colorvar = tk.StringVar()
    colorvar.set('0,255,0')
    snake_color = tk.Entry(settings_root, font = labelfont, textvariable = colorvar)
    snake_color.grid(column = 1, row = 1, padx = 5, pady = 5)

    speedvar = tk.StringVar()
    speedvar.set('20')
    snake_speed = tk.Entry(settings_root, font = labelfont, textvariable = speedvar)
    snake_speed.grid(column = 1, row = 2, padx = 5, pady = 5)

    highscores = tk.Button(settings_root, text = 'Submit', font = labelfont, bg  = 'black', fg = 'white', command = lambda: get_settings())
    highscores.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'NSEW')

    settings_root.mainloop()

def highscores_game():
    global highscore_list
    highscore_list.sort(reverse = True)
    highscore_root = tk.Toplevel()
    highscore_root.configure(background = 'green')
    highscore_root.geometry('500x400')
    highscore_root.title('High Scores')
    highscore_root.columnconfigure(0, weight = 1)
    highscore_root.columnconfigure(1, weight = 1)
    highscore_root.columnconfigure(2, weight = 1)
    highscore_root.rowconfigure(0, weight = 1)
    

    labelfont = font.Font(family = 'Cambria', size = 30)
    
    label = tk.Label(highscore_root, text = f'Top five scores:\n 1. {highscore_list[0]}\n 2. {highscore_list[1]}\n 3. {highscore_list[2]}\n 4. {highscore_list[3]}\n 5. {highscore_list[4]}\n ', bg  = 'green', font = labelfont)
    label.grid(column = 1, row = 0, padx = 55, pady = 5)

    highscore_root.mainloop()

def author_game():
    author_root = tk.Tk()
    author_root.geometry('500x400')
    author_root.configure(background = 'green')
    author_root.title('Information about author')
    author_root.columnconfigure(0, weight = 1)
    author_root.columnconfigure(1, weight = 1)
    author_root.columnconfigure(2, weight = 1)
    author_root.rowconfigure(0, weight = 1)

    labelfont = font.Font(family = 'Cambria', size = 30)

    label = tk.Label(author_root, wraplength = 175, justify = 'center', font = labelfont, bg  = 'green', text = 'Game made by Marcin Pałyga, first year student at Wroclaw University of Science and Technology.\n Field of study: Applied Mathematics\n Interests: Sports, Video games.')
    label.grid(column = 1, row = 0, sticky = 'N', padx = 5, pady = 5)

    author_root.mainloop()


def gui():
    global root
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Menu")
    root.configure(background = 'green')
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)
    root.columnconfigure(2, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight = 1)
    root.rowconfigure(2, weight = 1)
    root.rowconfigure(3, weight = 1)
    root.rowconfigure(4, weight = 1)
    root.rowconfigure(5, weight = 1)
    root.rowconfigure(6, weight = 1)

    labelfont = font.Font(family = 'Cambria', size = 30)
    buttonfont = font.Font(family = 'Cambria', size = 20)

    label = tk.Label(root, text = 'SNAKE', font = labelfont, bg  = 'green')
    label.grid(column = 1, row = 0, padx = 5, pady = 5)

    start = tk.Button(root, text = 'Start', font = buttonfont, bg  = 'black', fg = 'white', command = lambda: start_game())
    start.grid(column = 1, row = 1, padx = 5, pady = 5, sticky= 'NSEW')

    rules = tk.Button(root, text = 'Rules', font = buttonfont, bg  = 'black', fg = 'white', command = lambda: rules_game())
    rules.grid(column = 1, row = 2, padx = 5, pady = 5, sticky = 'NSEW')

    settings = tk.Button(root, text = 'Settings', font = buttonfont, bg  = 'black', fg = 'white', command = lambda: settings_game())
    settings.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'NSEW')

    highscores = tk.Button(root, text = 'High Scores', font = buttonfont, bg  = 'black', fg = 'white', command = lambda: highscores_game())
    highscores.grid(column = 1, row = 4, padx = 5, pady = 5, sticky = 'NSEW')

    author = tk.Button(root, text = 'About Author', font = buttonfont, bg  = 'black', fg = 'white', command = lambda: author_game())
    author.grid(column = 1, row = 5, padx = 5, pady = 5, sticky = 'NSEW')

    end = tk.Button(root, text = 'Quit', font = buttonfont, bg  = 'black', fg = 'white', command = lambda: root.destroy())
    end.grid(column = 1, row = 6, padx = 5, pady = 5, sticky = 'NSEW')

    root.mainloop()

gui()

