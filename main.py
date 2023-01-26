import pygame
import time
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
tan = (221, 204, 184)
 
dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Car game')
 
game_over = False
 
x1 = dis_width/2
y1 = dis_height/2
 
snake_block=10
 
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock()
snake_speed=30
 
font_style = pygame.font.SysFont(None, 50)

car = pygame.image.load("jeep-game/imgs/car2.png").convert_alpha()
width = car.get_rect().width
height = car.get_rect().height
car = pygame.transform.scale(car, (width*.2, height*.2))
heading = 3
# 0 is north, 1 is south, 2 is east, 3 is west

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def change_dir(heading, input, car):
    if heading == 0:
        if input == 1:
            car = pygame.transform.rotate(car, 180)
        if input == 2:
            car = pygame.transform.rotate(car, 90)
        if input == 3:
            car = pygame.transform.rotate(car, 270)
        return input, car
    if heading == 1:
        if input == 0:
            car = pygame.transform.rotate(car, 180)
        if input == 2:
            car = pygame.transform.rotate(car, 270)
        if input == 3:
            car = pygame.transform.rotate(car, 90)
        return input, car
    if heading == 2:
        if input == 1:
            car = pygame.transform.rotate(car, 90)
        if input == 3:
            car = pygame.transform.rotate(car, 180)
        if input == 0:
            car = pygame.transform.rotate(car, 270)
        return input, car
    if heading == 3:
        if input == 0:
            car = pygame.transform.rotate(car, 90)
        if input == 1:
            car = pygame.transform.rotate(car, 270)
        if input == 2:
            car = pygame.transform.rotate(car, 180)
        return input, car

 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
                heading, car = change_dir(heading, 3, car)
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
                heading, car = change_dir(heading, 2, car)
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
                heading, car = change_dir(heading, 0, car)
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
                heading, car = change_dir(heading, 1, car)
 
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(tan)
    # pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    # imp = pygame.image.load("jeep-game/imgs/car.png").convert()
    dis.blit(car, (x1, y1))
    pygame.display.update()
 
    clock.tick(snake_speed)
 
message("You lost",red)
pygame.display.update()
time.sleep(2)
 
pygame.quit()
quit()