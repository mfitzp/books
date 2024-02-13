from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
MOVE_SENSITIVITY = 256


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)



class Game:

    def reset(self):
        # Initial values, player at middle-bottom of screen.
        self.board = [
            # The board is symmetrical, so we can say it's [x][y] if we want.
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.round = 0

    def handle_input(self):
        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        if acc_x < -MOVE_SENSITIVITY:
            return 'left'
        elif acc_x > MOVE_SENSITIVITY:
            return 'right'
        elif acc_y < -MOVE_SENSITIVITY:
            return 'up'
        elif acc_y > MOVE_SENSITIVITY:
            return 'down'


    def collapse(self, direction):
        # Collapse the blocks, combining blocks of the same value.
        # the direction determines the direction we collapse in.
        if direction == 'left':
            self.collapse_x(1, MAX_COORD+1, 1, -1)
        elif direction == 'right':
            self.collapse_x(MAX_COORD-1, -1, -1, 1)
        elif direction == 'up':
            self.collapse_y(1, MAX_COORD+1, 1, -1)
        elif direction == 'down':
            self.collapse_y(MAX_COORD-1, -1, -1, 1)

    def collapse_x(self, start, stop, step, offset):
        has_moved = True
        while has_moved:
            has_moved = False
            for y in range(MAX_COORD + 1):
                for x in range(start, stop, step):
                    if self.board[x][y]:
                        if self.board[x+offset][y] == 0:
                            self.board[x+offset][y] = self.board[x][y]
                            self.board[x][y] = 0
                            has_moved = True

                        elif self.board[x][y] == self.board[x+offset][y]:
                            self.board[x+offset][y] += 1
                            self.board[x][y] = 0
                            has_moved = True

    def collapse_y(self, start, stop, step, offset):
        has_moved = True
        while has_moved:
            has_moved = False
            for x in range(MAX_COORD + 1):
                for y in range(start, stop, step):
                    print(x, y, start, stop, step, offset)
                    if self.board[x][y]:
                        if self.board[x][y+offset] == 0:
                            self.board[x][y+offset] = self.board[x][y]
                            self.board[x][y] = 0
                            has_moved = True

                        elif self.board[x][y] == self.board[x][y+offset]:
                            self.board[x][y+offset] += 1
                            self.board[x][y] = 0
                            has_moved = True


    def add_new_tile(self):

        while True:
            # Find blank space on board.
            x = random.randint(0, 4)
            y = random.randint(0, 4)

            if not self.board[x][y]:
                self.board[x][y] = random.randint(1, 2) * 2  # 2 or 4
                break


    def draw(self):
        display.clear()

        for x in range(MAX_COORD + 1):
            for y in range(MAX_COORD + 1):

                pixel = self.board[x][y]  # Note!
                display.set_pixel(x, y, pixel)

    def win(self):
        return any(b == 9 for a in self.board for b in a)


# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.CHESSBOARD)
    wait_for_button()

    game.reset() # Reset the game state.
    game.add_new_tile()
    game.draw()

    while not game.win():
        # We move on button press.
        wait_for_button()

        # Reset.
        if button_a.was_pressed():
            break

        direction = game.handle_input()
        if not direction:
            continue # restart loop.

        game.collapse(direction)
        game.add_new_tile()
        game.draw()

        sleep(250)

    if game.win():
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)
    sleep(1000)
