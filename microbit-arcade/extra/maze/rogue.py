from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
MOVE_THRESHOLD = 256
GHOST_SPEED = 5
WALL = 7

MAP = [
    [0,0,0,0,0,0,0,7,0,0,0,0,0,0,0],
    [7,7,7,7,7,7,0,7,0,7,7,0,7,7,0],
    [0,0,0,0,0,0,0,0,0,7,0,0,0,7,0],
    [0,7,7,0,7,7,7,7,7,7,7,0,7,7,0],
    [0,0,0,0,7,0,0,7,0,0,7,0,0,7,0],
    [7,7,7,0,7,7,0,7,0,7,7,0,7,7,7],
    [7,7,7,0,7,0,0,7,0,0,7,0,7,7,7],
    [7,7,7,0,7,0,0,0,0,0,7,0,7,7,7],
    [7,7,7,0,7,7,0,7,0,7,7,0,7,7,7],
    [0,0,7,0,7,0,0,7,0,0,7,0,0,0,0],
    [0,7,7,0,7,0,7,7,7,0,7,0,7,7,0],
    [0,0,7,0,7,0,7,0,0,0,0,0,0,7,0],
    [0,7,7,0,7,7,7,7,0,7,7,7,7,7,0],
    [0,0,0,0,0,0,0,7,0,0,0,0,7,0,0],
]

MAP_MIN_X = 0
MAP_MAX_X = len(MAP[0]) - 1

MAP_MIN_Y = 0
MAP_MAX_Y = len(MAP) - 1

VALID_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


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
        # Initial values
        self.x = 0
        self.y = 0

        self.moves = 0
        self.tick = 0

        # Position of ghosts on the map
        self.ghosts = [(0, 13), (14,13), (7,7), (0,4)]

        while True:
            tx = random.randint(7, MAP_MAX_X)
            ty = random.randint(7, MAP_MAX_Y)
            if MAP[ty][tx] == 0:
                self.treasure = (tx, ty)
                break


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

        if MAP[self.y][self.x] == WALL:
            self.x = prev_x
            self.y = prev_y
        else:
            self.moves += 1

    def move_ghosts(self):
        if self.tick % GHOST_SPEED != 0:
            return

        def valid_move(x, y):
            # Valid if not a wall, and no ghost in that position.
            return (
                not out_of_bounds(x, y) and
                MAP[y][x] != WALL and
                (x, y) not in self.ghosts
                )

        ghosts = []
        for x, y in self.ghosts:
            choice = random.randint(0, 3)

            if choice == 0:
                dx, dy = random.choice(VALID_MOVES)

            else:
                # Determine best direction to player, finding any valid move
                # that brings us closer. Not too smart.
                dx, dy = self.x - x, self.y - y
                dx = int(abs(dx) / dx) if dx else 0
                dy = int(abs(dy) / dy) if dy else 0

            if dx and valid_move(x+dx, y):
                ghosts.append((x+dx, y))

            elif dy and valid_move(x, y+dy):
                ghosts.append((x, y+dy))

            else:
                ghosts.append((x, y))

        self.ghosts = ghosts

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

                # Ghost
                elif (x, y) in self.ghosts:
                    pixel = (self.tick % 3) * 4

                # Goal
                elif (x, y) == self.treasure:
                    pixel = 9

                else:
                    pixel = MAP[y][x]

                display.set_pixel(dx, dy, pixel)

        display.set_pixel(2, 2, 4)

    def win(self):
        return (self.x, self.y) == self.treasure  # Found goal square.

    def die(self):
        return (self.x, self.y) in self.ghosts

# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.SWORD)
    wait_for_button()

    game.reset() # Reset the game state.
    while not (game.win() or game.die()):
        game.handle_input()
        game.draw()
        game.move_ghosts()
        sleep(125)

    if game.win():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SKULL)

    sleep(1000)
    display.scroll(game.moves)