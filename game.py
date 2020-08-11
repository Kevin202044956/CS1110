# Kaiwen zhu(kz8pr) Yanwen Wang (yw9cj)
import pygame
import random
import gamebox

# define the size of screen
camera = gamebox.Camera(600, 400)

# the elements of the snake
snake_speed = 0
snake_head = gamebox.from_circle(400, 100, 'salmon', 5)
snake_body = [
    gamebox.from_circle(410, 100, 'gold', 5),
    gamebox.from_circle(420, 100, 'orange', 5),
    gamebox.from_circle(430, 100, 'yellowgreen', 5),
    gamebox.from_circle(440, 100, 'steelblue', 5),
    gamebox.from_circle(450, 100, 'darkslateblue', 5),
    gamebox.from_circle(460, 100, 'mediumvioletred', 5)

]
snake_color = ['salmon', 'gold', 'orange', 'yellowgreen', 'steelblue', 'darkslateblue', 'mediumvioletred']

# the remaining time you have
time = 0
time_text = [
    gamebox.from_text(150, 75, 'Level 1', 45, 'navajowhite'),
    gamebox.from_text(150, 200, 'Level 2', 45, 'navajowhite'),
    gamebox.from_text(150, 325, 'Level 3', 45, 'navajowhite'),
    gamebox.from_text(400, 60, '~~~~ S N A K E ~~~~', 38, 'tomato'),
    gamebox.from_text(400, 125, 'Pick Level by Enter 1, 2, 3', 25, 'tomato'),
    gamebox.from_text(400, 150, 'LEVEL 1: 120S, LOW SPEED, LIFESPAN:5', 22, 'tomato'),
    gamebox.from_text(400, 175, 'LEVEL 2: 90S, MEDIUM SPEED, LIFESPAN:4', 22, 'tomato'),
    gamebox.from_text(400, 200, 'LEVEL 3: 60, HIGH SPEEDd, LIFESPAN:3', 22, 'tomato')
]
remaining_time = gamebox.from_text(80, 120, 'time:', 32, 'dimgrey')

# 3 food at the same time (will be a animation in the future)
normal_food = [gamebox.from_circle(random.randint(235, 565), random.randint(35, 365), 'brown', 10),
               gamebox.from_circle(random.randint(235, 565), random.randint(35, 365), 'brown', 10),
               ]
health_food = gamebox.from_circle(random.randint(235, 565), random.randint(35, 365), 'forestgreen', 8)


# walls (top right area is the place to display remaining time and score
# button right area is the place to display your remaining lives)
arena = [
    gamebox.from_color(300, 0, 'cadetblue', 600, 50),
    gamebox.from_color(300, 400, 'cadetblue', 600, 50),
    gamebox.from_color(0, 200, 'cadetblue', 50, 400),
    gamebox.from_color(600, 200, 'cadetblue', 50, 400),
    gamebox.from_color(150, 200, 'cadetblue', 25, 400),
    gamebox.from_color(80, 200, 'cadetblue', 125, 25)
]

# score
coin = 0

# choose the level, via to different level, the snake's speed will be different
level_choose_area = [
    gamebox.from_color(150, 75, 'cadetblue', 150, 75),
    gamebox.from_color(150, 200, 'cadetblue', 150, 75),
    gamebox.from_color(150, 325, 'cadetblue', 150, 75),
]
level = gamebox.from_text(80, 50, 'level', 32, 'dimgrey')

# the remaining lives you have, displayed by health meter
# (level 1 you get 5, level 2 you get 4, level 3 you get 3)
life = []
life_part1 = gamebox.from_color(40, 300, 'limegreen', 18, 25)
life_part2 = gamebox.from_color(60, 300, 'limegreen', 18, 25)
life_part3 = gamebox.from_color(80, 300, 'limegreen', 18, 25)
life_part4 = gamebox.from_color(100, 300, 'limegreen', 18, 25)
life_part5 = gamebox.from_color(120, 300, 'limegreen', 18, 25)

# health meter
health = gamebox.from_text(80, 265, 'Health Meter:', 22, 'dimgrey')
health_meter = gamebox.from_color(80, 300, 'dimgrey', 100, 25)

# game over
game_over = gamebox.from_text(370, 200, "Game Over!", 50, 'red')

# the state of game
game_on = False

# add image
snake_image = gamebox.from_image(410, 300, 'snake.png')
snake_image.scale_by(0.25)
coin_image = gamebox.load_sprite_sheet('coin.png', 1, 6)
coin_each_image = gamebox.from_image(random.randint(235, 565), random.randint(35, 365), coin_image[0])
coin_each_image.scale_by(0.15)
tick_count = 0


def touching(box1, box2):
    '''
    return true if the boxes are touching
    '''
    if box1.right_touches(box2):
        return True
    if box1.left_touches(box2):
        return True
    if box1.top_touches(box2):
        return True
    if box1.bottom_touches(box2):
        return True
    return False


def pick_level(keys):
    # pick the level you want
    # level 1: 120 seconds, low speed
    # level 2: 90 seconds, medium speed
    # level 3: 60 seconds, high speed
    global time
    global life
    global snake_speed
    global game_on
    global level
    global health_meter
    life = []
    for area in level_choose_area:
        camera.draw(area)
    for text in time_text:
        camera.draw(text)
    camera.draw(snake_image)
    if pygame.K_1 in keys:
        time = 120
        snake_speed = 7
        level = gamebox.from_text(80, 45, '- level 1 -', 32, 'dimgrey')
        life.append(life_part1)
        life.append(life_part2)
        life.append(life_part3)
        life.append(life_part4)
        life.append(life_part5)
        gamebox.stop_loop()
    elif pygame.K_2 in keys:
        time = 90
        snake_speed = 10
        level = gamebox.from_text(85, 45, '- level 2 -', 32, 'dimgrey')
        life.append(life_part1)
        life.append(life_part2)
        life.append(life_part3)
        life.append(life_part4)
        gamebox.stop_loop()
    elif pygame.K_3 in keys:
        time = 60
        snake_speed = 13
        level = gamebox.from_text(85, 45, '- level 3 -', 32, 'dimgrey')
        life.append(life_part1)
        life.append(life_part2)
        life.append(life_part3)
        gamebox.stop_loop()
    camera.display()


def ticks(keys):
    global coin
    global life
    global game_on
    global time
    global snake_head
    global snake_body
    global normal_food
    global health_food
    global tick_count
    global coin_each_image
    # game guide
    # ----- START ------
    # start the game by input 'S', we hope the snake could be controlled by
    # direction keys
    if game_on is False:
        scoreboard = gamebox.from_text(80, 82, 'coin: ' + str(int(coin)), 32, 'goldenrod')
        second = gamebox.from_text(80, 150, str(int(time)) + ' s', 32, 'indianred')
        game_guide = [gamebox.from_text(370, 125, "You have " + str(time) + " seconds!", 25, 'indianred'),
                      gamebox.from_text(370, 150, "Use direction keys to control the snake", 25, 'indianred'),
                      gamebox.from_text(370, 175, "Click 'S' to start game!", 25, 'indianred'),
                      gamebox.from_text(370, 200, "Eat the RED food to increase the LENGTH of the snake", 20, 'tomato'),
                      gamebox.from_text(370, 225, "Eat the GREEN food to increase the LIFESPAN of the snake", 20,
                                        'seagreen'),
                      gamebox.from_text(370, 250, "Eat the SPINNING COIN which worths extra 5 COINS", 20,
                                        'darkorange'),
                      gamebox.from_text(370, 275, "(SPINNING COIN will DECREASE snake's LIFESPAN)", 20, 'darkorange')
                      ]
        camera.clear('whitesmoke')
        for wall in arena:
            camera.draw(wall)
        camera.draw(health_meter)
        camera.draw(health)
        for life_part in life:
            camera.draw(life_part)
        for guide in game_guide:
            camera.draw(guide)
        for part in snake_body:
            camera.draw(part)
        camera.draw(snake_head)
        camera.draw(second)
        camera.draw(scoreboard)
        camera.draw(remaining_time)
        camera.draw(level)
        if pygame.K_s in keys:
            game_on = True
        snake_head.speedx = -snake_speed
        camera.display()

    if game_on is True:

        camera.clear('whitesmoke')
        second = gamebox.from_text(80, 150, str(int(time)) + ' s', 32, 'indianred')
        # draw all walls
        for wall in arena:
            camera.draw(wall)
        camera.draw(health_meter)
        camera.draw(health)
        for life_part in life:
            camera.draw(life_part)
        camera.draw(remaining_time)
        # draw level you choose
        camera.draw(level)

        # ----- SNAKE -----
        # the snake will move at a constant speed based on the level,
        # you can use direction keys to control the snake, each input will
        # make the snake turn left or right in 90' degrees. the original position
        # and length of the fixed.
        camera.draw(snake_head)
        for part in snake_body:
            camera.draw(part)
        if snake_head.speedx > 0:
            if pygame.K_UP in keys:
                snake_head.speedy = -snake_speed
                snake_head.speedx = 0
            if pygame.K_DOWN in keys:
                snake_head.speedx = 0
                snake_head.speedy = snake_speed
            if pygame.K_RIGHT in keys:
                snake_head.speedy = 0
                snake_head.speedx = snake_speed
        if snake_head.speedx < 0:
            if pygame.K_LEFT in keys:
                snake_head.speedy = 0
                snake_head.speedx = -snake_speed
            if pygame.K_UP in keys:
                snake_head.speedy = -snake_speed
                snake_head.speedx = 0
            if pygame.K_DOWN in keys:
                snake_head.speedx = 0
                snake_head.speedy = snake_speed
        if snake_head.speedy < 0:
            if pygame.K_LEFT in keys:
                snake_head.speedy = 0
                snake_head.speedx = -snake_speed
            if pygame.K_UP in keys:
                snake_head.speedy = -snake_speed
                snake_head.speedx = 0
            if pygame.K_RIGHT in keys:
                snake_head.speedy = 0
                snake_head.speedx = snake_speed
        if snake_head.speedy > 0:
            if pygame.K_DOWN in keys:
                snake_head.speedx = 0
                snake_head.speedy = snake_speed
            if pygame.K_LEFT in keys:
                snake_head.speedy = 0
                snake_head.speedx = -snake_speed
            if pygame.K_RIGHT in keys:
                snake_head.speedy = 0
                snake_head.speedx = snake_speed
        snake_head.move_speed()
        if snake_head.speedx != 0 or snake_head.speedy != 0:
            if snake_head.speedy == 0 and snake_head.speedx < 0:
                part = snake_body.pop()
                part.x = snake_head.x + 10
                part.y = snake_head.y
                snake_body = [part] + snake_body
            if snake_head.speedy == 0 and snake_head.speedx > 0:
                part = snake_body.pop()
                part.x = snake_head.x - 10
                part.y = snake_head.y
                snake_body = [part] + snake_body
            if snake_head.speedx == 0 and snake_head.speedy > 0:
                part = snake_body.pop()
                part.x = snake_head.x
                part.y = snake_head.y - 10
                snake_body = [part] + snake_body
            if snake_head.speedx == 0 and snake_head.speedy < 0:
                part = snake_body.pop()
                part.x = snake_head.x
                part.y = snake_head.y + 10
                snake_body = [part] + snake_body

        # ----- COLLISION DETECTION ------
        # any collision beside touching the food will create damage to the snake
        # when the snake hit itself, the snake will lose 1 life and move through its body.
        # when the snake knock its head against a brick wall, it will lose all of its
        # lives immediately.
        for wall in arena:
            if touching(snake_head, wall):
                camera.draw(game_over)
                gamebox.pause()
        for body in snake_body[3:]:
            if touching(snake_head, body):
                camera.draw(game_over)
                gamebox.pause()

        # ----- FOOD ------
        # the original position of the food is fixed, but when the snake touch the food,
        # the old food will disappear and a new food will randomly appear on the gaming area.
        # each successful eat will mak2e the length of snake's body increase by 1(normal food)
        for food in normal_food:
            camera.draw(food)
        camera.draw(health_food)

        # ----- SCORING -----
        # when the snake successfully eat or touch the food, the length of the snake will
        # increase and the scoreboard will display the points you have. each food worth 1 point.
        for food in normal_food:
            if touching(snake_head, food):
                coin += 1
                normal_food.remove(food)
                new_food = gamebox.from_circle(random.randint(235, 565), random.randint(35, 365), 'brown', 9)
                normal_food.append(new_food)
                new_body_part = gamebox.from_circle(snake_head.x, snake_head.y, snake_color[random.randint(1, 6)], 5)
                snake_body.append(new_body_part)

        if touching(snake_head, coin_each_image):
            coin += 5
            coin_each_image = gamebox.from_image(random.randint(235, 565), random.randint(35, 365), coin_image[0])
            coin_each_image.scale_by(0.15)
            life.pop()
            if len(life) == 0:
                camera.draw(game_over)
                gamebox.pause()

        if touching(snake_head, health_food):
            number = len(life)
            new_part = gamebox.from_color(40 + 20 * number, 300, 'limegreen', 18, 25)
            if number < 5:
                life.append(new_part)
            health_food = gamebox.from_circle(random.randint(235, 565), random.randint(35, 365), 'forestgreen', 7)

        scoreboard = gamebox.from_text(80, 82, 'coin: ' + str(int(coin)), 32, 'goldenrod')
        camera.draw(scoreboard)

        # ----- TIME -----
        # the remaining time is also based on the level you choose, level 1 is 120 seconds,
        # level 2 is 90 seconds, level 3 is 60 seconds. the time will counted down and
        # when time become 0, the game will be over.
        time -= 1 / 30
        camera.draw(second)

        # ----- OVER -----
        # when the time become 0 or the remaining lives become 0, the game will be over
        if time <= 0:
            camera.draw(game_over)
            gamebox.pause()
        coin_each_image.image = coin_image[tick_count // 2 % len(coin_image)]
        tick_count += 1
        camera.draw(coin_each_image)

    camera.display()


gamebox.timer_loop(20, pick_level)
gamebox.timer_loop(30, ticks)
