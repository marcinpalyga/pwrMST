
import pygame
import random


pygame.init()
width = 500
height = 400
game_root = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption('Snake game')
block = 10
speed = 20
clock = pygame.time.Clock()
score_font = pygame.font.SysFont('Cambria', 20)

def dis_score(score):
    value = score_font.render(f'Your score: {score}', True, (255,255,255))
    game_root.blit(value, [0,0])

def snake(block, snake_list):
    for i in snake_list:
        pygame.draw.rect(game_root, (0,255,0), [i[0], i[1], block, block])


def gameloop():
    game_over = False
    game_close = False

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
        clock.tick(speed)

    pygame.quit()
    quit()

gameloop()