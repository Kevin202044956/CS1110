import pygame
import gamebox
import random

# The game we will create, will be similar to the arcade favorite Space Invaders.
# We will either use AD or arrow keys to move the main character/icon
# In this game the end result will be the highest score accumulated, or by the length of survival.
# With that, we will be sure to implement enemies, a health meter, and animation.
# In general, player has 3 hearts/lives and the health goes down in either 3 increments or 4 increments.
# The players will be able to shoot a laser type weapon as seen in game.

class MyGameStat(): 
    '''
    This class hold the elements in the Space Invaders Game
    '''
    def __init__(self):
        #The game have an enemies list,bombs, a player
        #Also define the speed of the bombs, the score of the player get
        #Player have 3 health. 
        self.score = 0
        self.health = 3
        self.level = 1
        self.enemies = []
        self.player = gamebox.from_image(300, 550, "./boat.png") 
        self.bombspeed = 2
        self.bombs = []
        self.bombscnt = 2
        self.enemyspeed = 1
        self.weapons = [] #the weapons to kill enemies
        self.weaponspeed = 5 # the weapon's attack speed
    
    def check_levelup(self):
        if(self.score >= 100*self.level or len(self.enemies) ==0):
            self.level += 1
            if(self.level >= 3):
                return
            self.load_level()

    def load_level(self):
        # load level elements . When the level changes, we load 
        # different element from file. The file name is like "level_1"
        filename = "level_" + str(self.level)
        self.bombs.clear()
        self.enemies.clear()
        self.weapons.clear()
        fin = open(filename)
        for line in fin:
            location = line.split()
            self.enemies.append(gamebox.from_image(int(location[0]), int(location[1]), "./enemy.png" ))
        self.bombspeed *= 2
        self.bombscnt +=2

    def check_end(self):
        if(self.level >= 2 and self.score >= 200):
            return 1
        if(self.health <= 0):
            return -1
        return 0
    
    def move_enemies(self):
        for en in self.enemies:
            if(en.speedx != self.enemyspeed):
                en.speedx = self.enemyspeed
            en.move_speed()
        if(self.enemies[0].x < self.enemies[0].width/2):
            self.enemyspeed = 1
        elif(self.enemies[len(self.enemies) - 1].x >= camera.width - self.enemies[0].width/2):
            self.enemyspeed = -1

    def launch_bombs(self): 
        # the enemies randomly throw bombs
        for i in range(self.bombscnt - len(self.bombs)):
            enemy_index = random.randint(0, len(self.enemies)-1)
            bomb = gamebox.from_image(self.enemies[enemy_index].x, self.enemies[enemy_index].y, "bomb.png")
            bomb.speedy = self.bombspeed
            self.bombs.append(bomb)
        new_bomb = [] #remove bombs out of camera
        for bomb in self.bombs:
            bomb.move_speed()
            if(bomb.touches(self.player)):
                self.health -= 1
                continue
            if(bomb.y > camera.height):
                self.score += 1
                continue
            new_bomb.append(bomb)
        self.bombs = new_bomb
    
    def add_weapon(self):
        weapon = gamebox.from_color(self.player.x, self.player.y, "red", 10,10)
        weapon.speedy = -self.weaponspeed
        self.weapons.append(weapon)

    def launch_weapons(self):
        new_weapons = []
        for weapon in self.weapons:
            weapon.move_speed()
            attack_success = False
            for en in self.enemies:
                if(weapon.touches(en)):
                    self.enemies.remove(en)
                    attack_success = True
            if(attack_success):
                self.score += 10
                continue
            new_weapons.append(weapon)
        self.weapons = new_weapons

    def move_player(self, direct):
       # move the player to left or right
        if(direct == "left"):
            self.player.x -= 20
            if(self.player.x < self.player.width/2 ):
                self.player.x = self.player.width/2
        elif(direct == "right"):
            self.player.x += 20
            if(self.player.x >= camera.width-self.player.width/2):
                self.player.x = camera.width-self.player.width/2
        else:
            print("wrong!")

    def init_draw(self):
        #draw all the elements(player, bombs, enemies, health hearts) to camera
        camera.draw(self.player)
        score_text = gamebox.from_text(70, 20, "SCORE: " + str(self.score), 25, "Red", bold=True)
        camera.draw(score_text)
        level_text = gamebox.from_text(350, 20, "LEVEL: " + str(self.level), 25, "Red", bold=True)
        camera.draw(level_text)
        for en in self.enemies:
            camera.draw(en)
        for bomb in self.bombs:
            if(bomb.speedy != 0):
                camera.draw(bomb)
        for weapon in self.weapons:
            if(weapon.speedy != 0):
                camera.draw(weapon)
        for i in range(self.health):
            heart = gamebox.from_image(550+30*i, 10,  "./health.png")
            camera.draw(heart)

def tick(keys):
    #check whether the game end
    is_end = game.check_end()
    if(is_end == 1): # game win
        camera.draw(gamebox.from_text(400, 300, "You Win!", 30, "Red", bold=True))
        camera.display()
        return
    if(is_end == -1): #game lose
        camera.draw(gamebox.from_text(400, 300, "You lose!", 30, "Red", bold=True))
        camera.display()
        return
    game.launch_bombs()
    game.move_enemies()
    game.launch_weapons()
    if pygame.K_a in keys: # you can check which keys are being pressed
        game.move_player("left")
    if pygame.K_d in keys: # you can check which keys are being pressed
        game.move_player("right")
    if pygame.K_w in keys:
        game.add_weapon()
    keys.clear()
    game.check_levelup()
    camera.clear("white")
    game.init_draw()
    camera.display() # you almost always want to end this method with this line

if __name__ == "__main__":
    width = 600
    hight = 800
    camera = gamebox.Camera(hight, width)
    game = MyGameStat()
    game.load_level()
    gamebox.timer_loop(30, tick)
