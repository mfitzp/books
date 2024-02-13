# tag::constants[]
from microbit import *

MIN_COORD = 0
MAX_COORD = 4
GAME_SPEED = 5
BAT_SIZE = 2

# Number of additional pixels for bat (= length -1)
# Simplifies later calculations.
BAT_EXTRA = BAT_SIZE - 1
# end::constants[]

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


# tag::reset[]
class Game:

    def reset(self):
        self.player_1_y = 2
        self.player_2_y = 2

        self.ball_x = 2
        self.ball_y = 2

        self.ball_velocity_y = 1
        self.ball_velocity_x = 1

        self.tick = 0
    # end::reset[]

    # tag::handle_input[]
    def handle_input(self):
        self.tick += 1
        acc_y = accelerometer.get_y()

        if acc_y < -100:
            self.player_1_y -= 1
        elif acc_y > 100:
            self.player_1_y += 1

        # Constrain.
        if self.player_1_y < MIN_COORD:
            self.player_1_y = MIN_COORD

        if self.player_1_y + BAT_EXTRA > MAX_COORD:
            self.player_1_y = MAX_COORD - BAT_EXTRA
    # end::handle_input[]

    # tag::move_ball[]
    def move_ball(self):
        if self.tick % GAME_SPEED:
            return

        self.ball_x += self.ball_velocity_x
        self.ball_y += self.ball_velocity_y
    # end::move_ball[]

    def draw(self):
        display.clear()

        for n in range(BAT_SIZE):
            display.set_pixel(MIN_COORD, self.player_1_y + n, 9)
            display.set_pixel(MAX_COORD, self.player_2_y + n, 9)

        display.set_pixel(self.ball_x, self.ball_y, 9)

    def game_over(self):
        return False

# Main loop

game = Game() # Create our game object.

display.show(Image.SQUARE_SMALL)
wait_for_button()

game.reset() # Reset the game state.

while not game.game_over():
    game.handle_input()
    game.move_ball()
    game.draw()
    sleep(200)
