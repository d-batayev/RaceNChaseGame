import pygame
import time
import random
import os

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("RACE & CHASE by Daulet Batayev")
clock = pygame.time.Clock()


carImg = pygame.image.load('./external/racecar.png')
car2Img = pygame.image.load('./external/racecar2.png')
bg = pygame.image.load('./external/bg.png')
gas = pygame.image.load ('./external/gas.png')
moving_bg = pygame.image.load('./external/bg1.png')
moving_grass = pygame.image.load('./external/grass.jpg')
enemy = pygame.image.load('./external/enemy car.png')
arrow = pygame.image.load('./external/arrow.png')
star = pygame.image.load('./external/star.png')

car_width = 73


def welcome_screen():
    game_display.fill(white)
    large_text = pygame.font.Font('freesansbold.ttf', 60)
    TextSurface, TextRect = text_objects("RACE & CHASE", large_text, black)
    TextRect.center = ((display_width / 2), (display_height * 0.35))

    small_text = pygame.font.Font('freesansbold.ttf', 30)
    TextSurface2, TextRect2 = text_objects("Press SPACE To Start The Game", small_text,black)
    TextRect2.center = ((display_width/2), (display_height*0.55))

    TextSurface3, TextRect3 = text_objects("Press \"C\" to Choose A Car", small_text,black)

    TextRect3.center = ((display_width/2), (display_height*0.65))

    name_text_font = pygame.font.Font('./external/ComicSansMS3.ttf', 20)
    TextSurface4, TextRect4 = text_objects('2019, Daulet Batayev', name_text_font, blue)
    TextRect4.center = ((display_width * 0.80), (display_height * 0.90))

    game_display.blit(TextSurface, TextRect)
    game_display.blit(TextSurface2, TextRect2)
    game_display.blit(TextSurface3, TextRect3)
    game_display.blit(TextSurface4, TextRect4)
    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 0
                if event.key == pygame.K_c:
                    return 1

def car_choice_screen():
    arrowx = display_width * 0.315
    arrowy = display_height*0.48

    large_text = pygame.font.Font('freesansbold.ttf', 60)
    TextSurface, TextRect = text_objects("Choose A Car (SPACE)", large_text, black)
    TextRect.center = ((display_width / 2), (display_height * 0.35))


    while True:
        for event1 in pygame.event.get():


            if event1.type == pygame.QUIT:
                pygame.QUIT
                quit()
            if event1.type == pygame.KEYDOWN:
                if event1.key == pygame.K_SPACE:
                    if arrowx == display_width*0.315:
                        return carImg
                    return car2Img

                if event1.key == pygame.K_LEFT and arrowx!=display_width*0.315:
                    arrowx = display_width*0.315
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("./external/menu.mp3")
                    pygame.mixer.music.play(1)
                if event1.key == pygame.K_RIGHT and arrowx!=display_width *0.685:
                    arrowx = display_width * 0.615
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("./external/menu.mp3")
                    pygame.mixer.music.play(1)

        game_display.fill(white)
        game_display.blit(TextSurface, TextRect)
        game_display.blit(carImg, ((display_width * 0.3), (display_height * 0.6)))
        game_display.blit(car2Img, ((display_width * 0.6), (display_height * 0.6)))
        game_display.blit(arrow, (arrowx, arrowy))
        pygame.display.update()
        clock.tick(70)


def instruction_screen():
    game_display.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSufr, TextRect = text_objects("Avoid the Red Kart!", largeText, black)
    TextRect.center = ((display_width / 2), (display_height * 0.3))
    game_display.blit(TextSufr, TextRect)
    game_display.blit(enemy, ((display_width*0.45), (display_height * 0.08)))
    game_display.blit(gas, ((display_width*0.275), (display_height * 0.45)))
    game_display.blit(star, ((display_width*0.17), (display_height * 0.55)))

    gasText = pygame.font.Font('freesansbold.ttf', 25)
    TextSufrgas, TextRectgas = text_objects(" - Turbo to BOOST The Car", gasText, black)
    TextRectgas.center = ((display_width *0.53), (display_height * 0.49))
    game_display.blit(TextSufrgas, TextRectgas)

    startText = pygame.font.Font('freesansbold.ttf', 25)
    TextSufrstart, TextRectstart = text_objects(" - \" Mario Star \" Temporary Immortality", startText, black)
    TextRectstart.center = ((display_width * 0.53), (display_height * 0.59))
    game_display.blit(TextSufrstart, TextRectstart)

    startText1 = pygame.font.Font('freesansbold.ttf', 25)
    TextSufrstart1, TextRectstart1 = text_objects("for the Next THREE Karts",startText1, black)
    TextRectstart1.center = ((display_width * 0.63), (display_height * 0.64))
    game_display.blit(TextSufrstart1, TextRectstart1)


    pygame.display.update()
    time.sleep(4)


def move_grass(grassx, grassy):
    game_display.blit(moving_grass, (grassx, grassy))

def move_bg(bgx, bgy):
    game_display.blit(moving_bg, (bgx, bgy))

def show_gas(gasx,gasy):
    game_display.blit(gas,(gasx, gasy))

def show_star(starx, stary):
    game_display.blit(star, (starx, stary))


def check_if_high_score(cur_dodged, high_score):
    if (high_score < cur_dodged):
        high_score = cur_dodged
        with open("./external/highscore.txt", 'w') as filew:
            filew.write(str(high_score))

def show_high_score(high_score):
    font1 = pygame.font.SysFont(None, 25)
    text1 = font1.render(f"High ", True, white)
    game_display.blit(text1, (0,40))
    text2 = font1.render(f"Score: {str(high_score)}", True, white)
    game_display.blit(text2, (0,65))


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, white)
    game_display.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, colour):
    game_display.blit(enemy, (thingx, thingy))

def car(x,y):
    game_display.blit(carImg,(x,y))


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("./external/crashsound.mp3")
    pygame.mixer.music.play(1)
    game_display.fill(white)
    message_display('YOU CRASHED')
    time.sleep(2)


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSufr, TextRect = text_objects(text, largeText, black)
    TextRect.center = ((display_width/2), (display_height*0.45))
    game_display.blit(TextSufr,TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()




def game_loop():
    pygame.mixer.music.load("./external/BackgroundMusic.mp3")  # background music
    pygame.mixer.music.play(-1)  # playing the music over and over again

    x = (display_width * 0.454)  # initial horizontal position of the car
    y = (display_height * 0.8)  # initial vertical position of the car

    pressed_up = False
    pressed_down = False
    pressed_right = False
    pressed_left = False
    is_gas = False  # if it is the time for the gas to pop out
    gas_started = False  # if the gas icon is falling
    car_turbo = False  # if the car is accelerated
    is_star = False
    star_started = False
    car_star = False

    bgx = (display_width * 0.454) + car_width-45
    bgy = 0
    grassx = 0
    grassy = 0
    grass2x = display_width - 105

    high_score = 0
    thing_width = 73
    thing_startx = random.randrange(0,display_width-thing_width)
    thing_starty= -600
    thing_speed = 7
    thing_height = 82
    dodged = 0
    game = True


    maxThingSpeed = 18

    gas_width = 50
    gas_height = 43
    gas_counter = 0
    turbo_counter = 0

    star_width = 50
    star_height = 43
    star_counter = 0
    car_star_counter = 0

    car_speed = 5

    gasx= random.randrange(5, display_width-gas_width)
    gasy=0

    starx = random.randrange(5, display_width - star_width)
    stary = 0



    if (os.path.exists("./external/highscore.txt")):
        with open('./external/highscore.txt', 'r') as file:
            high_score = int(file.read())

    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pressed_up = True

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pressed_down = True

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pressed_left = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pressed_right = True

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pressed_up = False

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pressed_down = False

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pressed_left = False

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pressed_right = False

        x_change = 0
        y_change = 0

        if pressed_up and y > 20:
            y_change = -car_speed

        if pressed_down and y < (display_height * 0.8):
            y_change = +car_speed

        if pressed_left:
            x_change = -car_speed
        if pressed_right:
            x_change= car_speed

        x += x_change
        y += y_change

        bgy += 3
        grassy += 3

        game_display.blit(bg,(0,0))

        move_bg(bgx, bgy)
        move_grass(grassx,grassy)
        move_grass(grass2x, grassy)
        things(thing_startx, thing_starty, thing_width, thing_height, black)

        car(x,y)

        if gas_started:
            gasy += 3
            show_gas(gasx, gasy)

        if star_started:
            stary += 4
            show_star(starx, stary)

        things_dodged(dodged)
        show_high_score(high_score)
        thing_starty += thing_speed


        if x > display_width - car_width or x<3:
            check_if_high_score(dodged, high_score)
            crash()

        if thing_starty > display_height:
            thing_starty = 0-thing_height
            thing_startx = random.randrange(0, display_width - thing_width)
            dodged += 1

            if car_turbo:
                turbo_counter += 1

                if turbo_counter == 3:
                    turbo_counter = 0
                    car_turbo = False
                    car_speed = 5
                    is_gas = False
                    gas_started = False

            if car_star:
                star_counter += 1

                if star_counter == 3:
                    star_counter = 0
                    car_star = False
                    is_star = False
                    star_started = False


            #if (thing_width < maxThingWidth): #change to variables
                #thing_width += 10
            if thing_speed < maxThingSpeed: #change to variables
                thing_speed += 1
                gas_counter += 1
                car_star_counter +=1
                if gas_counter >= 6 and not car_turbo:
                    is_gas = True
                    gas_started = True
                if car_star_counter >= 8 and not car_star:
                    is_star = True
                    star_started = True
            if thing_speed == maxThingSpeed: # change to variables
                gas_counter = 0
                is_gas = False
                car_star_counter = 0
                is_star = False

                thing_speed = 7

        if dodged >= 20:
            maxThingSpeed = 15

        if bgy+560 > display_height:  # change constants to the variables
            bgy = -44

        if grassy+560>display_height:
            grassy = -90

        if gasy > display_height:
            gasy = 0
            gasx = random.randrange(5, display_width-gas_width)
            gas_started = False
            is_gas = False

        if stary > display_height:
            stary = 0
            starx = random.randrange(5, display_height - star_width)
            star_started = False
            is_star = False

        if ((thing_startx<=x and x<=thing_startx+thing_width) or (x+car_width>=thing_startx and x+car_width<=thing_startx+thing_width)) and ((((thing_starty + thing_height>=y) and (thing_starty<= y  )) or ((thing_starty + thing_height>=y+83) and (thing_starty >= y and thing_starty <= y +83)) or ((thing_starty>y and thing_starty<y+83) and (thing_starty + thing_height>y and thing_starty+thing_height<y+83)))):
                check_if_high_score(dodged, high_score)
                if (not car_star):
                    crash()


        if ((gasx<=x and x<= gasx+gas_width) or (x+car_width>=gasx and x+car_width<=gasx+gas_width)) and (gasy+gas_height>=y):

            gas_started = False
            is_gas = False
            car_speed = 10
            car_turbo = True
            gasy = 0
            gasx = random.randrange(5, display_width - gas_width)

        if ((starx <= x and x <= starx + star_width) or (x + car_width >= starx and x + car_width <= starx + star_width)) and (stary + star_height >= y):

            star_started = False
            is_star = False
            car_star = True
            stary = 0
            starx = random.randrange(5, display_width - star_width)
        if (x>=0 and x<=95) and not car_turbo:
            car_speed = 2
        if (x>95 and x<display_width-95) and not car_turbo:
            car_speed = 5

        if (x>=display_width-170) and not car_turbo:
            car_speed = 2


        pygame.display.update()
        clock.tick(70)

if(not welcome_screen()):
    instruction_screen()
else:
    carImg = car_choice_screen()
    instruction_screen()
game_loop()
pygame.quit()