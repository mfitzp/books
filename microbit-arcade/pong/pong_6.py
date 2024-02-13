from microbit import *

MIN_COORD = 0
MAX_COORD = 4
GAME_SPEED = 5
BAT_SIZE = 2

# Number of additional pixels for bat (= length -1)
# Simplifies later calculations.
BAT_EXTRA = BAT_SIZE - 1


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

# tag::reset[]
class Game:

    def reset(self):
        self.player_1_y = 2
        self.player_2_y = 2

        self.ball_x = 1
        self.ball_y = 3

        self.ball_velocity_y = 1
        self.ball_velocity_x = 1

        self.tick = 0
        # end::reset[]

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

    # tag::move_ball[]
    def move_ball(self):
        if self.tick % GAME_SPEED:
            return

        self.ball_x += self.ball_velocity_x
        self.ball_y += self.ball_velocity_y
        return True
    # end::move_ball[]

    # tag::rebound_ball[]
    def rebound_ball(self):
        # Check for rebound off wall.
        if self.ball_y <= MIN_COORD:
            self.ball_y = MIN_COORD
            self.ball_velocity_y = -self.ball_velocity_y

        elif self.ball_y >= MAX_COORD:
            self.ball_y = MAX_COORD
            self.ball_velocity_y = -self.ball_velocity_y
    # end::rebound_ball[]

    # tag::draw[]
    def draw(self):
        display.clear()

        for n in range(BAT_SIZE):
            display.set_pixel(MIN_COORD, self.player_1_y + n, 9)
            display.set_pixel(MAX_COORD, self.player_2_y + n, 9)

        for n in range(MAX_COORD + 1):
            display.set_pixel(2, n, 4)

        display.set_pixel(self.ball_x, self.ball_y, 9)
    # end::draw[]

    def game_over(self):
        return False

# Main loop

game = Game() # Create our game object.

display.show(Image.SQUARE_SMALL)
wait_for_button()

game.reset() # Reset the game state.

# tag::main_loop[]
while not game.game_over():
    game.handle_input()
    if game.move_ball():
        # Ball moved, check collisions.
        game.rebound_ball()
    game.draw()
    sleep(200)
# end::main_loop[]