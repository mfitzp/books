from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
MOVE_THRESHOLD = 256

MAP = [
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,0,1,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,1,1,1,1,1,1,1,0,1,1,0],
    [0,0,0,0,1,2,0,1,0,0,1,0,0,1,0],
    [1,1,1,0,1,1,0,1,0,1,1,0,1,1,1],
    [1,1,1,0,1,0,0,1,0,0,1,0,1,1,1],
    [1,1,1,0,1,0,0,0,0,0,1,0,1,1,1],
    [1,1,1,0,1,1,0,1,0,1,1,0,1,1,1],
    [0,0,1,0,1,0,0,1,0,0,1,0,0,0,0],
    [0,1,1,0,1,0,1,1,1,0,1,0,1,1,0],
    [0,0,1,0,1,0,1,0,0,0,0,0,0,1,0],
    [0,1,1,0,1,1,1,1,0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
]

MAP_MIN_X = 0
MAP_MAX_X = len(MAP[0]) - 1

MAP_MIN_Y = 0
MAP_MAX_Y = len(MAP) - 1


def out_of_bounds(x, y):
    return (x > MAP_MAX_X or
     x < MAP_MIN_X or
     y > MAP_MAX_Y or
     y < MAP_MIN_Y)

def constrain(x, y):
    if x > MAP_MAX_X:
        x = MAP_MAX_X
    if x < MAP_MIN_X:
        x = MAP_MIN_X
    if y > MAP_MAX_Y:
        y = MAP_MAX_Y
    if y < MAP_MIN_Y:
        y = MAP_MIN_Y
    return x, y

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

def visible(px, py, x, y):
    # Check if x & y is visible, based on player px & py
    if (
        (x >= px -2 and x <= px + 2) and
        (y >= py -2 and y <= py + 2)
        ):
            return True


class Game:

    def reset(self):
        # Initial values, start at top left.
        self.x = 0
        self.y = 0

        self.moves = 0
        self.tick = 0


    def handle_input(self):
        self.tick += 1

        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        prev_x, prev_y = self.x, self.y

        if abs(acc_x) > abs(acc_y):
            if acc_x < -MOVE_THRESHOLD:
                self.x -= 1
            if acc_x > MOVE_THRESHOLD:
                self.x += 1

        else:
            if acc_y < -MOVE_THRESHOLD:
                self.y -= 1
            if acc_y > MOVE_THRESHOLD:
                self.y += 1

        self.x, self.y = constrain(self.x, self.y)

        # If there is a block in new position, undo move.
        if MAP[self.y][self.x] == 1:
            self.x = prev_x
            self.y = prev_y
        else:
            # Count valid moves.
            self.moves += 1



    def draw(self):
        # Draw the active portion of the map on the screen.
        # centered around the users location, out of bounds not drawn.
        map_x_range = range(self.x-2, self.x+2+1)
        map_y_range = range(self.y-2, self.y+2+1)

        for dx, x in enumerate(map_x_range):
            for dy, y in enumerate(map_y_range):

                # Areas around the map are drawn solid.
                if out_of_bounds(x, y):
                    pixel = 7

                # Goal
                elif MAP[y][x] == 2:
                    pixel = (self.tick % MAP[y][x]) * 9

                # Player (center pixel)
                elif dx == 2 and dy == 2:
                    pixel = 2

                else:
                    pixel = MAP[y][x] * 7

                display.set_pixel(dx, dy, pixel)

    def win(self):
        return MAP[self.y][self.x] == 2  # Found goal square.

# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.DIAMOND)
    wait_for_button()

    game.reset() # Reset the game state.
    while not game.win():
        game.handle_input()
        game.draw()
        sleep(250)

    display.show(Image.HAPPY)
    sleep(1000)
    display.scroll(game.moves)
