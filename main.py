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

side_car_left = pygame.image.load("jeep-game/imgs/jeep.png").convert_alpha()
top_car_up = pygame.image.load("jeep-game/imgs/top.png").convert_alpha()
width = side_car_left.get_rect().width
height = side_car_left.get_rect().height
side_car_left = pygame.transform.scale(side_car_left, (width*.04, height*.04))
width = top_car_up.get_rect().width
height = top_car_up.get_rect().height
top_car_up = pygame.transform.scale(top_car_up, (width*.07, height*.07))
top_car_up = pygame.transform.rotate(top_car_up, 90)
heading = 3
car = side_car_left
side_car_right = pygame.transform.flip(side_car_left, True, False)
top_car_down = pygame.transform.flip(top_car_up, False, True)
# 0 is north, 1 is south, 2 is east, 3 is west

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def change_dir(input, car):
    if input == 0:
        return input, top_car_up
    elif input == 1:
        return input, top_car_down
    elif input == 2:
        return input, side_car_right
    else:
        return input, side_car_left
        
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
                heading, car = change_dir(3, car)
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
                heading, car = change_dir(2, car)
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
                heading, car = change_dir(0, car)
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
                heading, car = change_dir(1, car)
 
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
time.sleep(1)
 
pygame.quit()
quit()