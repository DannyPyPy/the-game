def on_a_pressed():
    global mySprite2
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 6 6 . . . . . . .
            . . . . . . . 6 6 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.projectile)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite2: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . f f f f f f f f . . . .
        . . . . f 2 2 2 2 2 2 f . . . .
        . . . . f 2 2 2 2 2 2 f . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . . f 2 2 2 2 2 2 f . . . .
        . . . . f 2 2 2 2 2 2 f . . . .
        . . . . f f f f f f f f . . . .
        . . . . f f f f f f f f . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)