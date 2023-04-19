def on_a_pressed():
    music.play(music.string_playable("- - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_life_zero():
    info.set_life(3)
    info.change_life_by(-1)
info.on_life_zero(on_life_zero)

mySprite: Sprite = None
controller.player2.move_sprite(mySprite)

def on_on_update():
    pass
game.on_update(on_on_update)

def on_update_interval():
    game.reset()
game.on_update_interval(800, on_update_interval)
