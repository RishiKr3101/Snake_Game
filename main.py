import pygame
import random
import math

pygame.init()

#WINDOW
screen= pygame.display.set_mode((800,600))
background= pygame.transform.scale(pygame.image.load('images/bg.png'), (800, 600))
pygame.display.set_caption("Snake by RISHI")

s=0.5 #setting speed

SnakeImg = pygame.transform.scale(pygame.image.load('images/snake.png'), (32,32))
snake_X = random.randint(50, 750)
snake_Y = 0
snake_X_Change = 0
snake_Y_Change = 0


FoodImg = pygame.transform.scale(pygame.image.load('images/food.png'), (32,32))
Food_X = random.randint(50, 750)
Food_Y = random.randint(50, 550)

Snake_Body_X=[]
Snake_Body_Y=[]
Position_x = []
Position_y = []



score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

over_font = pygame.font.Font('freesansbold.ttf', 64)

def snake(x,y):
    
    screen.blit(SnakeImg,(x,y))
    
        

def snake_body():
    l= len(Snake_Body_Y)
    k=0
    for i in range(len(Position_x)-1,len(Position_x)-l , -1):
        screen.blit(SnakeImg, (Position_x[i], Position_y[i]))
        Snake_Body_X[k]= Position_x[i]
        Snake_Body_Y[k] = Position_y[i]

        k=k+1






def food(x,y):
    screen.blit(FoodImg,(x,y))



def Eat(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2)))
    if distance < 20:
        return True
        
    else:
        return False

def body_collision():
     x1 = Snake_Body_X[0]
     y1 = Snake_Body_Y[0]
     for i in range(2, len(Snake_Body_Y)):
         
         x2= Snake_Body_X[i]
         y2 = Snake_Body_Y[i]
         distance = math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2)))
         if distance < 15:
            
             return True
         
     return False
         

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0,0,0))
    screen.blit(score, (x, y))

def game_over(x,y):
    Over = font.render("Game Over  ::   Final Score :" + str(score_value), True, (0,0,0))
    screen.blit(Over, (x,y))



runtime= True
End=False
c=0
while runtime :
    c=c+1
    screen.blit(background, (0, 0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            runtime =False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                snake_X_Change = -s
                snake_Y_Change = 0
            if event.key == pygame.K_RIGHT :
                snake_X_Change = s
                snake_Y_Change = 0
            if event.key == pygame.K_UP :
                snake_Y_Change = -s
                snake_X_Change = 0
            if event.key == pygame.K_DOWN :
                snake_Y_Change = s
                snake_X_Change =0

    if snake_X <= 0:
        snake_X = 0
    elif snake_X >= 736:
        snake_X = 736
    if snake_Y <= 0:
        snake_Y = 0
    elif snake_Y>= 536:
        snake_Y= 536
    
    snake_X += snake_X_Change
    snake_Y += snake_Y_Change


    if Eat(snake_X, snake_Y, Food_X, Food_Y) :
        
        Food_X = random.randint(50, 750)
        Food_Y = random.randint(50, 550)
        score_value+=10
        
        l= len(Position_x)
        Snake_Body_X.append(Position_x[l-5])
        Snake_Body_Y.append(Position_y[l-5])
        





    if(len(Snake_Body_Y) >1):
        
        if(body_collision()):
            game_over(200,180)
            End = True
        
        elif( End):
            game_over(200,180)

        
        else:
            snake(snake_X, snake_Y)
            if(snake_X_Change != 0 or snake_Y_Change !=0):
                snake_body()
        
            food(Food_X, Food_Y)
            show_score(10,10)
        
    else :
        snake(snake_X, snake_Y)
        if(snake_X_Change != 0 or snake_Y_Change !=0):
            snake_body()
        
        food(Food_X, Food_Y)
        show_score(10,10)

    if c==70 :
        Position_x.append(snake_X)
        Position_y.append(snake_Y)
        
        c=0



    pygame.display.update()