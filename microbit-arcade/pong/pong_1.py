from microbit import *

MIN_COORD = 0
MAX_COORD = 4

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


class Game:

    def reset(self):
        self.ball_x = 2
        self.ball_y = 2

    def draw(self):
        display.clear()
        display.set_pixel(self.ball_x, self.ball_y, 9)

    def game_over(self):
        return False

# Main loop

game = Game() # Create our game object.

display.show(Image.SQUARE_SMALL)
wait_for_button()

game.reset() # Reset the game state.

while not game.game_over():
    # We move on button press.
    game.draw()

    sleep(200)
