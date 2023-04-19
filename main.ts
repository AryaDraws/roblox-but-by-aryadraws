controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.UntilDone)
})
function Eat_lunch_fruits__apple_juice () {
	
}
info.onLifeZero(function () {
    info.setLife(3)
    info.changeLifeBy(-1)
})
let mySprite: Sprite = null
controller.player2.moveSprite(mySprite)
game.onUpdate(function () {
	
})
game.onUpdateInterval(800, function () {
    game.reset()
})
