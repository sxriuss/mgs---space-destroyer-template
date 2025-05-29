
#01 - Create two variables, projectile and ship, both of which are of type Sprite:
projectile: Sprite = None
ship: Sprite = None




#02 - Create the Space Green Ship.
ship = sprites.create(sprites.space.spaceGreenShip, SpriteKind.player)



#03 - Create an Array or List to Store 5 Asteroid Images:
asteroids = [sprites.space.spaceSmallAsteroid1,
    sprites.space.spaceSmallAsteroid1,
    sprites.space.spaceSmallAsteroid2,
    sprites.space.spaceSmallAsteroid3,
    sprites.space.spaceSmallAsteroid4,
    sprites.space.spaceSmallAsteroid5]
    
#04a - Prevent the ship from going of screen.
ship.set_stay_in_screen(True)



#04b - Set the start position of the ship.
ship.bottom = 120



#05 - Connect the controller to the Ship so you can move.
controller.move_sprite(ship, 100, 100)



#06 - Add - Special effects to the background.
effects.star_field.start_screen_effect()

#07 - Give the Player only 3 Lives.
info.set_life(3)

#09 - Function for Button A - to shoot bullets
def on_a_pressed():
    projectile = sprites.create_projectile_from_sprite(img("""
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . 7 7 . . .
        . . . 7 7 . . .
        . . . 7 7 . . .
        . . . 7 7 . . .
    """),
        ship,
        0,
        -200)
    projectile.start_effect(effects.cool_radial, 100)

#10 - Function to check if the Projectile hits the Enemy
def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.change_score_by(1)

#10b - Function to check if the Player hits the Enemy
def on_on_overlap2(sprite2, otherSprite2):
    scene.camera_shake(4, 500)
    otherSprite2.destroy(effects.disintegrate)
    sprite2.start_effect(effects.fire, 100)
    info.change_life_by(-1)

#11 - Forever Loop that runs every 500 MilliSeconds - Make the asteroids appear from the top
def on_update_interval():
    asteroid_enemy = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 200)
    asteroid_enemy.set_kind(SpriteKind.enemy)
    asteroid_enemy.x = randint(10, 150)
    


#12 - Using the Functions
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)
game.on_update_interval(500, on_update_interval)

