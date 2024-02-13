# tag::constants[]
from microbit import *

MIN_COORD = 0
MAX_COORD = 4
# end::constants[]

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

# tag::wrap[]
class Game:

    def wrap(self):
        if self.x > MAX_COORD:
            self.x = MIN_COORD
        if self.x < MIN_COORD:
            self.x = MAX_COORD
        if self.y > MAX_COORD:
            self.y = MIN_COORD
        if self.y < MIN_COORD:
            self.y = MAX_COORD
# end::wrap[]

    def reset(self):
        # Initial values
        self.x = 2
        self.y = 2

    def handle_input(self):
        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        if abs(acc_x) > abs(acc_y):
            if acc_x < -100:
                self.x -= 1
            if acc_x > 100:
                self.x += 1

        else:
            if acc_y < -100:
                self.y -= 1
            if acc_y > 100:
                self.y += 1

    def draw(self):
        display.clear()
        display.set_pixel(self.x, self.y, 9)

    def game_over(self):
        return False


game = Game() # Create our game object.
game.reset() # Reset the game state.

display.show(Image.SNAKE)
wait_for_button()

# tag::main_loop[]
while not game.game_over():
    game.handle_input()
    game.wrap()
    game.draw()
    sleep(250)
# end::main_loop[]
