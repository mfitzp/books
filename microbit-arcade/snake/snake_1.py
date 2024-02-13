from microbit import *


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


class Game:

    def reset(self):
        # Initial values
        self.x = 2
        self.y = 2

    def draw(self):
        display.clear()
        display.set_pixel(self.x, self.y, 9)

    def game_over(self):
        return False


display.show(Image.SNAKE)
wait_for_button()

game = Game() # Create our game object.
game.reset() # Reset the game state.

# Main loop
while not game.game_over():
    game.handle_input()
    game.draw()
    sleep(250)