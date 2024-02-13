# tag::constants[]
from microbit import *

DIRECTIONS = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1),
}
# end::constants[]

MIN_COORD = 0
MAX_COORD = 4


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

# tag::move[]
class Game:

    def move(self):
        # Look up the tuple x_speed, y_speed, by direction and unpack to the variables.
        x_speed, y_speed = DIRECTIONS[self.direction]  # <1>

        self.x += x_speed  # <2>
        self.y += y_speed
# end::move[]

# tag::handle_input[]
    def handle_input(self):
        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        if abs(acc_x) > abs(acc_y):
            if acc_x < -100:
                self.direction = 'left'
            if acc_x > 100:
                self.direction = 'right'

        else:
            if acc_y < -100:
                self.direction = 'up'
            if acc_y > 100:
                self.direction = 'down'
# end::handle_input[]

# tag::reset[]
    def reset(self):
        # Initial values
        self.x = 2
        self.y = 2

        self.direction = 'right'
# end::reset[]

    def wrap(self):
        if self.x > MAX_COORD:
            self.x = MIN_COORD
        if self.x < MIN_COORD:
            self.x = MAX_COORD
        if self.y > MAX_COORD:
            self.y = MIN_COORD
        if self.y < MIN_COORD:
            self.y = MAX_COORD

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
    game.move()
    game.wrap()
    game.draw()
    sleep(250)
# end::main_loop[]
