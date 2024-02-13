# tag::constants[]
from microbit import *

MIN_COORD = 0
MAX_COORD = 4
# end::constants[]

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


# tag::constrain[]
class Game:

    def handle_input(self):
        acc_x = accelerometer.get_x()

        if acc_x < -0:
            self.x -= 1
        if acc_x > 0:
            self.x += 1

        # Constrain to width of the display.
        if self.x > MAX_COORD:
            self.x = MAX_COORD

        if self.x < MIN_COORD:
            self.x = MIN_COORD

    # end::constrain[]

    def reset(self):
        # Initial values
        self.x = 2

    def draw(self):
        display.clear()
        display.set_pixel(self.x, 4, 9)

    def game_over(self):
        return False


display.show(Image.TARGET)
wait_for_button()

game = Game() # Create our game object.
game.reset() # Reset the game state.


while not game.game_over():
    game.handle_input()
    game.draw()
    sleep(150)


