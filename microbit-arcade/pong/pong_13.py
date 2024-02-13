# tag::constants[]
from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
GAME_SPEED = 5
BAT_SIZE = 2
DIFFICULTY = 20  # Random mistakes by computer player. Lower = more frequent mistakes.
WINNING_SCORE = 10  # First player to this wins.

# Number of additional pixels for bat (= length -1)
# Simplifies later calculations.
BAT_EXTRA = BAT_SIZE - 1
# end::constants[]

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

def constrain_speed(ys):
    if ys < -1:
        return -1
    if ys > 1:
        return 1
    return ys

def constrain_bat(y):
    if y < MIN_COORD:
        return = MIN_COORD

    if y + BAT_EXTRA > MAX_COORD:
        return MAX_COORD - BAT_EXTRA

def calculate_delta(ball_y, player_y):
    if ball_y == player_y:
        return -1
    return 1


class Game:

    def reset(self):
        self.player_1_y = 2
        self.player_2_y = 2

        self.ball_x = 2
        self.ball_y = 2

        self.ball_velocity_y = 1
        self.ball_velocity_x = 1

        self.tick = 0

    def reset_scores(self):
        self.player_1_score = 0
        self.player_2_score = 0

    def handle_input(self):
        self.tick += 1
        acc_y = accelerometer.get_y()

        if acc_y < -100:
            self.player_1_y -= 1
        elif acc_y > 100:
            self.player_1_y += 1

        # Constrain.
        self.player_1_y = constrain_bat(self.player_1_y)

    def computer_move(self):
        # Change direction only occasionally, determined by DIFFICULTY.
        if random.randint(0, DIFFICULTY):
            # Determine position of the ball and change the bat direction.
            if self.ball_y < self.player_2_y:
                self.player_2_velocity_y = -1

            elif self.ball_y > self.player_2_y + BAT_EXTRA:
                self.player_2_velocity_y = 1

        # Update the computer player's bat position (every tick)
        self.player_2_y += self.player_2_velocity_y

        # Constrain.
        self.player_2_y = constrain_bat(self.player_2_y)

    def move_ball(self):
        if self.tick % GAME_SPEED:
            return

        self.ball_x += self.ball_velocity_x
        self.ball_y += self.ball_velocity_y
        return True

    def rebound_ball(self):
        # Check for rebound off wall.
        if self.ball_y <= MIN_COORD:
            self.ball_y = MIN_COORD
            self.ball_velocity_y = -self.ball_velocity_y

        elif self.ball_y >= MAX_COORD:
            self.ball_y = MAX_COORD
            self.ball_velocity_y = -self.ball_velocity_y

    def check_bats(self):
        # Player 1 bat.
        if (
            self.ball_x == MIN_COORD + 1 and
            self.ball_y >= self.player_1_y and
            self.ball_y <= self.player_1_y + BAT_EXTRA
        ):
            self.ball_velocity_x = -self.ball_velocity_x

            veloc_delta = calculate_delta(self.ball_y, self.player_1_y)
            self.ball_velocity_y = constrain_speed(self.ball_velocity_y + veloc_delta)

        # Player 2 bat.
        if (
            self.ball_x == MAX_COORD -1 and
            self.ball_y >= self.player_2_y and
            self.ball_y <= self.player_2_y + BAT_EXTRA
        ):
            self.ball_velocity_x = -self.ball_velocity_x

            veloc_delta = calculate_delta(self.ball_y, self.player_2_y)
            self.ball_velocity_y = constrain_speed(self.ball_velocity_y + veloc_delta)

    def draw(self):
        display.clear()

        for n in range(BAT_SIZE):
            display.set_pixel(MIN_COORD, self.player_1_y + n, 9)
            display.set_pixel(MAX_COORD, self.player_2_y + n, 9)

        for n in range(MAX_COORD + 1):
            display.set_pixel(2, n, 4)

        display.set_pixel(self.ball_x, self.ball_y, 9)

    def game_over(self):
        if self.ball_x == MIN_COORD:
            self.player_2_score += 1
            return True
        elif self.ball_x == MAX_COORD:
            self.player_1_score += 1
            return True

# Main loop
# tag::main_loop[]
game = Game() # Create our game object.
while True:

    game.reset_scores() # Reset both players scores.

    while True:

        display.show(Image.SQUARE_SMALL)
        wait_for_button()
        game.reset() # Reset the game state.

        while not game.game_over():
            game.handle_input()
            game.computer_move()
            if game.move_ball():
                # Ball moved, check collisions.
                game.rebound_ball()
                game.check_bats()
            game.draw()
            sleep(200)

        sleep(1000)
        # Allocate points
        score_message = '{}:{}'.format(game.player_1_score, game.player_2_score)
        display.scroll(score_message)

        if game.player_1_score == WINNING_SCORE:
            display.scroll("Player 1 wins!")
            break

        if game.player_2_score == WINNING_SCORE:
            display.scroll("Player 2 wins!")
            break
# end::main_loop[]