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


Bonus = pygame.transform.scale(pygame.image.load('images/bonus.png'), (32,32))
Bonus_X = 0
Bonus_Y = 0


Snake_Body_X=[]
Snake_Body_Y=[]
Position_x = []
Position_y = []

Start = False


score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)
font_inst = pygame.font.Font('freesansbold.ttf', 18)

over_font = pygame.font.Font('freesansbold.ttf', 64)

Intro = pygame.font.Font('freesansbold.ttf', 74)


def Menu() :
    main_intro = Intro.render("Snake Game", True, (0,0,0))
    screen.blit(main_intro, (180, 10))
    screen.blit(FoodImg, (30, 200))
    screen.blit(Bonus,(30, 250))
    food_inst = font_inst.render(": Eat food for 10 Points and body will grow by one unit", True, (0,0,0))
    bonus_inst = font_inst.render(": Eat Bonus(will appear in between) for 20 Points and body will decrease by 3 units", True, (0,0,0))
    inst = font.render("Press [SPACE] to Start", True, (0,0,0))
    screen.blit(food_inst, (80, 200))
    screen.blit(bonus_inst, (80, 250))
    screen.blit(inst, (200,400))

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






def food(x,y,x1, y1):
    screen.blit(FoodImg,(x,y))
    if score_value%100 == 0 and not(score_value == 0):
        screen.blit(Bonus,(x1,y1))



def Eat(x1, y1, x2, y2, x3 ,y3):
    distance = math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2)))
    distance1 =  math.sqrt(math.pow(x1 - x3, 2) + (math.pow(y1 - y3, 2)))
    if distance < 20:
        return True, False
        
    
    
    if score_value%100 == 0 and not(score_value == 0):
        if distance1 < 20:
            
            return True, True
            
        else:
            return False , True
    
    else:
        return False , False


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
            if event.key == pygame.K_SPACE :
                Start = True
    
    
    if(Start == True):
        c=c+1

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


        food_eat , bonus_eat = Eat(snake_X, snake_Y, Food_X, Food_Y, Bonus_X, Bonus_Y)


        if food_eat :
            
            Food_X = random.randint(50, 750)
            Food_Y = random.randint(50, 550)

            Bonus_X = random.randint(50, 750)
            Bonus_Y = random.randint(50, 550)
            if bonus_eat :
                score_value+=20
                Snake_Body_X.pop()
                Snake_Body_X.pop()
                Snake_Body_X.pop()
                Snake_Body_Y.pop()
                Snake_Body_Y.pop()
                Snake_Body_Y.pop()
            else :
                score_value += 10
            
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
            
                food(Food_X, Food_Y, Bonus_X, Bonus_Y)
                show_score(10,10)
            
        else :
            snake(snake_X, snake_Y)
            if(snake_X_Change != 0 or snake_Y_Change !=0):
                snake_body()
            
            food(Food_X, Food_Y, Bonus_X,Bonus_Y)
            show_score(10,10)

        if c==70 :
            Position_x.append(snake_X)
            Position_y.append(snake_Y)
            
            c=0
    
    else:
        Menu()



    pygame.display.update()