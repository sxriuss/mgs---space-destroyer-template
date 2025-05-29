// 01 - Create two variables, projectile and ship, both of which are of type Sprite:
let projectile : Sprite = null
let ship : Sprite = null
// 02 - Create the Space Green Ship.
ship = sprites.create(sprites.space.spaceGreenShip, SpriteKind.Player)
// 03 - Create an Array or List to Store 5 Asteroid Images:
let asteroids = [sprites.space.spaceSmallAsteroid1, sprites.space.spaceSmallAsteroid1, sprites.space.spaceSmallAsteroid2, sprites.space.spaceSmallAsteroid3, sprites.space.spaceSmallAsteroid4, sprites.space.spaceSmallAsteroid5]
// 04a - Prevent the ship from going of screen.
ship.setStayInScreen(true)
// 04b - Set the start position of the ship.
ship.bottom = 120
// 05 - Connect the controller to the Ship so you can move.
controller.moveSprite(ship, 100, 100)
// 06 - Add - Special effects to the background.
effects.starField.startScreenEffect()
// 07 - Give the Player only 3 Lives.
info.setLife(3)
// 09 - Function for Button A - to shoot bullets
// 10 - Function to check if the Projectile hits the Enemy
// 10b - Function to check if the Player hits the Enemy
// 11 - Forever Loop that runs every 500 MilliSeconds - Make the asteroids appear from the top
// 12 - Using the Functions
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    let projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . 7 7 . . .
        . . . 7 7 . . .
        . . . 7 7 . . .
        . . . 7 7 . . .
    `, ship, 0, -200)
    projectile.startEffect(effects.coolRadial, 100)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    scene.cameraShake(4, 500)
    otherSprite2.destroy(effects.disintegrate)
    sprite2.startEffect(effects.fire, 100)
    info.changeLifeBy(-1)
})
game.onUpdateInterval(500, function on_update_interval() {
    let asteroid_enemy = sprites.createProjectileFromSide(asteroids[randint(0, asteroids.length - 1)], 0, 200)
    asteroid_enemy.setKind(SpriteKind.Enemy)
    asteroid_enemy.x = randint(10, 150)
})
