#Chris Barfield - cdb8da

import pygame
import gamebox
import random

#Start initalizing variables to be used throughout code

p_width = 10
p_height = 80
ball_velocity = 15
player_speed = 14
shipimage_score = 0
ship_speed = 6
score = 60
game_on = False
game_over = False
display_width = 800
display_height = 600
shipx = 800
shipy = 600
timer = 0
life = 120
life1 = 80
astscore = 0
ticker = 0
game_on = False
game_over = False
game_won = False

# Creating general images for background and images to be shown throughout game

camera = gamebox.Camera(shipx,shipy)
sheet = gamebox.load_sprite_sheet("saucer.png", 4, 3)
frame = 0
shipimage = gamebox.from_image(400, 300, sheet[frame])  # gamebox image is first pic in sprite sheet
shipimage.scale_by(1.5)
background = gamebox.from_image(300,100,'background.jpg')
background1 = gamebox.from_image(400,100,'astilte.png')
background2 = gamebox.from_image(400,250,'astback.png')
background2.scale_by(2.25)

#Creating astroids

ast1 = gamebox.from_image(100,100,'asteroid.png')
ast1.scale_by(.1)
ast2 = gamebox.from_image(700,100,'asteroid.png')
ast2.scale_by(.1)
ast3 = gamebox.from_image(100,500,'asteroid.png')
ast3.scale_by(.1)
ast4 = gamebox.from_image(700,500,'asteroid.png')
ast4.scale_by(.1)

#Creating ship shots

shot1 = gamebox.from_image(1000,1000,'shot.png')
shot1.scale_by(.025)
shot2 = gamebox.from_image(1000,1000,'shot.png')
shot2.scale_by(.025)
shot3 = gamebox.from_image(1000,1000,'shot.png')
shot3.scale_by(.025)
shot4 = gamebox.from_image(1000,1000,'shot.png')
shot4.scale_by(.025)
shot5 = gamebox.from_image(1000,1000,'shot.png')
shot5.scale_by(.025)
shot6 = gamebox.from_image(1000,1000,'shot.png')
shot6.scale_by(.025)
shot7 = gamebox.from_image(1000,1000,'shot.png')
shot7.scale_by(.025)
shot8 = gamebox.from_image(1000,1000,'shot.png')
shot8.scale_by(.025)
by = 550
ty = 50
pad = -10

#Creating directions and text to be used throughout parts of the game (these are static texts)

direct = gamebox.from_text(400,500, "Use the arrow keys to navigate and use D and F to shoot. Avoid the astroids to survive the time, and shoot them to earn points!", 18, "white", italic = True)
direct1 = gamebox.from_text(400,545, "Press Space to begin!", 45, "white", italic = True)
direct2 = gamebox.from_text(400,518, "Press Z to end the game early.", 20, "white", italic = True)
startpop = gamebox.from_text(400,575, "Game created by Chris Barfield - cdb8da", 25, "white", italic = True)
end_text = gamebox.from_text(400,300, "You lost, thanks for playing!", 75, "white", italic = True)
win_text = gamebox.from_text(400,300, "Congrats you won!", 100, "white", italic = True)
healthbartxt = gamebox.from_text(80, 25, "Health ", 40, 'white', italic=True)
healthbar1 = gamebox.from_color(80, 50, "black", 120, 25)

#Creating walls

wall1 = gamebox.from_color(400, 600, "white", 1000, 20)
wall2 = gamebox.from_color(400, 0, "white", 1000, 20)
wall3 = gamebox.from_color(0, 200, "white", 20, 1000)
wall4 = gamebox.from_color(800, 400, "white", 20, 1000)


def tick(keys):

    #Initializing global variables

    global timer
    global score
    global game_on
    global game_over
    global game_won
    global frame
    global by
    global ty
    global pad
    global life
    global healthbar
    global astscore
    global life1
    camera.clear("black")

    #Starting game

    if pygame.K_SPACE in keys:
        game_on = True
    if game_on:
        timer += 1
        camera.draw(background)
        if timer % 5 == 0:
            frame += 1
        if frame == 12:
            frame = 0
        shipimage.image = sheet[frame]
        if timer % 40 == 0:
            score -= 1

        #Creating gameboxes to be used and updated during the game (these are changing)

        score_box = gamebox.from_text(620, 30, "COUNTDOWN- " + str(score), 45, "white", italic=True)
        scoreast = gamebox.from_text(620, 550, "SCORE- " + str(astscore), 50, "white", italic=True)
        scoretext = gamebox.from_text(400, 450, "Your final score was " + str(astscore), 50, "white", italic=True)
        healthbar = gamebox.from_color(life1, 50, "red", life, 25)

        #Checking to see if time has ended

        if score == 0:
            game_won = True

        #Stopping ship from leaving the playing screen

        shipimage.move_to_stop_overlapping(wall1)
        shipimage.move_to_stop_overlapping(wall2)
        shipimage.move_to_stop_overlapping(wall3)
        shipimage.move_to_stop_overlapping(wall4)

        #Setting the speed of the shots fired

        shot1.speedx = -15
        shot2.speedx = -12
        shot3.speedx = -10
        shot4.speedx = -8
        shot5.speedx = 15
        shot6.speedx = 12
        shot7.speedx = 10
        shot8.speedx = 8

        #Collision detection to respawn the astroids at random locations and random x andy velocities to go in random directions

        if ast1.touches(wall1, pad):
            ast1.x = random.randint(25,800)
            ast1.y = ty
        if ast1.touches(wall2, pad):
            ast1.x = random.randint(25, 800)
            ast1.y = ty
        if ast1.touches(wall3, pad):
            ast1.x = random.randint(25, 800)
            ast1.y = ty
        if ast1.touches(wall4, pad):
            ast1.x = random.randint(25, 800)
            ast1.y = ty
        ast1.speedx = random.randint(1,10)
        ast1.speedy = random.randint(1,10)
        if ast2.touches(wall1, pad):
            ast2.x = random.randint(25,800)
            ast2.y = ty
        if ast2.touches(wall2, pad):
            ast2.x = random.randint(25, 800)
            ast2.y = ty
        if ast2.touches(wall3, pad):
            ast2.x = random.randint(25, 800)
            ast2.y = ty
        if ast2.touches(wall4, pad):
            ast2.x = random.randint(25, 800)
            ast2.y = ty
        ast2.speedx = random.randint(1,10)
        ast2.speedy = random.randint(1,10)
        if ast3.touches(wall1, pad):
            ast3.x = random.randint(25,800)
            ast3.y = by
        if ast3.touches(wall2, pad):
            ast3.x = random.randint(25, 800)
            ast3.y = by
        if ast3.touches(wall3, pad):
            ast3.x = random.randint(25, 800)
            ast3.y = by
        if ast3.touches(wall4, pad):
            ast3.x = random.randint(25, 800)
            ast3.y = by
        ast3.speedx = -1* (random.randint(1,10))
        ast3.speedy = -1* (random.randint(1,10))
        if ast4.touches(wall1, pad):
            ast4.x = random.randint(25,800)
            ast4.y = by
        if ast4.touches(wall2, pad):
            ast4.x = random.randint(25, 800)
            ast4.y = by
        if ast4.touches(wall3, pad):
            ast4.x = random.randint(25, 800)
            ast4.y = by
        if ast4.touches(wall4, pad):
            ast4.x = random.randint(25, 800)
            ast4.y = by
        ast4.speedx = -1* (random.randint(1,10))
        ast4.speedy = -1* (random.randint(1,10))

        #Collision detection functions for the ship and the astroids

        if shipimage.touches(ast1, pad) or shipimage.touches(ast2, pad) or shipimage.touches(ast3, pad) or shipimage.touches(ast4, pad):
            ast1.x = 50
            ast2.x = 750
            ast3.x = 50
            ast4.x = 750
            life -= 20
            life1 -= 10
            healthbar = gamebox.from_color(80, 50, "red", life, 25)
            if life == 0:
                gamebox.pause()
                game_over = True

        #Movement functions for the ship

        if pygame.K_UP in keys:
            shipimage.top -= 12
            camera.draw(shipimage, shipx+ 10, shipy + 10)
        if pygame.K_LEFT in keys:
            shipimage.x -= 10
        if pygame.K_RIGHT in keys:
            shipimage.x += 10
        if pygame.K_DOWN in keys:
            shipimage.top += 12

        #Shooting functions for the ship

        if pygame.K_d in keys:
            shot1.x = shipimage.x
            shot1.y = shipimage.y
            shot2.x = shipimage.x
            shot2.y = shipimage.y
            shot3.x = shipimage.x
            shot3.y = shipimage.y
            shot4.x = shipimage.x
            shot4.y = shipimage.y
        if pygame.K_f in keys:
            shot5.x = shipimage.x
            shot5.y = shipimage.y
            shot6.x = shipimage.x
            shot6.y = shipimage.y
            shot7.x = shipimage.x
            shot7.y = shipimage.y
            shot8.x = shipimage.x
            shot8.y = shipimage.y

        #Collision detection for astroids getting hit by shots

        if ast1.touches(shot1, pad) or ast1.touches(shot2, pad) or ast1.touches(shot3, pad) or ast1.touches(shot4, pad) or ast1.touches(shot5, pad) or ast1.touches(shot6, pad) or ast1.touches(shot7, pad) or ast1.touches(shot8, pad):
            ast1.x = 50
            astscore += 100
        if ast2.touches(shot1, pad) or ast2.touches(shot2, pad) or ast2.touches(shot3, pad) or ast2.touches(shot4, pad) or ast2.touches(shot5, pad) or ast2.touches(shot6, pad) or ast2.touches(shot7, pad) or ast2.touches(shot8, pad):
            ast2.x = 750
            astscore += 100
        if ast3.touches(shot1, pad) or ast3.touches(shot2, pad) or ast3.touches(shot3, pad) or ast3.touches(shot4, pad) or ast3.touches(shot5, pad) or ast3.touches(shot6, pad) or ast3.touches(shot7, pad) or ast3.touches(shot8, pad):
            ast3.x = 50
            astscore += 100
        if ast4.touches(shot1, pad) or ast4.touches(shot2, pad) or ast4.touches(shot3, pad) or ast4.touches(shot4, pad) or ast4.touches(shot5, pad) or ast4.touches(shot6, pad) or ast4.touches(shot7, pad) or ast4.touches(shot8, pad):
            ast4.x = 750
            astscore += 100
        if pygame.K_z in keys:
            game_over = True

        #Drawing all gamebox objects and moving objects

        camera.draw(healthbartxt)
        camera.draw(score_box)
        camera.draw(wall1)
        camera.draw(wall2)
        camera.draw(wall3)
        camera.draw(wall4)
        camera.draw(healthbar1)
        ast1.move_speed()
        camera.draw(ast1)
        ast2.move_speed()
        camera.draw(ast2)
        ast3.move_speed()
        camera.draw(ast3)
        ast4.move_speed()
        camera.draw(ast4)
        shot1.move_speed()
        camera.draw(shot1)
        shot2.move_speed()
        camera.draw(shot2)
        shot3.move_speed()
        camera.draw(shot3)
        shot4.move_speed()
        camera.draw(shot4)
        shot5.move_speed()
        camera.draw(shot5)
        shot6.move_speed()
        camera.draw(shot6)
        shot7.move_speed()
        camera.draw(shot7)
        shot8.move_speed()
        camera.draw(shot8)
        camera.draw(shipimage)
        camera.draw(healthbar)
        camera.draw(scoreast)
    else:

        #Start screen

        camera.draw(background2)
        camera.draw(direct)
        camera.draw(direct1)
        camera.draw(direct2)
        camera.draw(startpop)
    if game_over:

        #Game lost screen

        camera.clear('black')
        camera.draw(background1)
        camera.draw(startpop)
        camera.draw(end_text)
        camera.draw(scoretext)
        gamebox.pause()
    if game_won:

        #Game won screen

        shipimage.x = 1000
        camera.clear("black")
        camera.draw(background1)
        camera.draw(win_text)
        camera.draw(shipimage)
        camera.draw(scoretext)
        camera.draw(startpop)
        gamebox.pause()
    camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)