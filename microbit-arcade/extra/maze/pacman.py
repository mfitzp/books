from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
MOVE_THRESHOLD = 256
GHOST_SPEED = 5

MAP = [
    [2,1,1,1,1,1,1,3,1,1,1,1,1,1,2],
    [1,3,3,1,3,3,1,3,1,3,3,1,3,3,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,3,3,1,3,1,3,3,3,1,3,1,3,3,1],
    [1,1,1,1,3,1,1,3,1,1,3,1,1,1,1],
    [3,3,3,1,3,3,1,3,1,3,3,1,3,3,3],
    [3,3,3,1,3,1,1,1,1,1,3,1,3,3,3],
    [3,3,3,1,3,1,1,1,1,1,3,1,3,3,3],
    [3,3,3,1,3,3,1,3,1,3,3,1,3,3,3],
    [1,1,1,1,3,1,1,3,1,1,3,1,1,1,1],
    [1,3,3,1,3,1,3,3,3,1,3,1,3,3,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,3,3,1,3,3,1,3,1,3,3,1,3,3,1],
    [2,1,1,1,1,1,1,3,1,1,1,1,1,1,2],
]

MAP_MIN_X = 0
MAP_MAX_X = len(MAP[0]) - 1

MAP_MIN_Y = 0
MAP_MAX_Y = len(MAP) - 1

MAX_BOMBS = 3
BOMB_TICKS = 25

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
        self.x = 5
        self.y = 5
        # Each step we advance by 1.
        self.velocity = (0, 0)

        self.tick = 0
        self.score = 0

        # Position of ghosts on the map
        self.ghosts = [(8,7), (9,7), (10,7), (9,8)]

    def handle_input(self):
        self.tick += 1

        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        prev_x, prev_y = self.x, self.y

        if abs(acc_x) > abs(acc_y):
            if acc_x < -MOVE_THRESHOLD:
                self.velocity = (-1, 0)
            if acc_x > MOVE_THRESHOLD:
                self.velocity = (1, 0)

        else:
            if acc_y < -MOVE_THRESHOLD:
                self.velocity = (0, -1)
            if acc_y > MOVE_THRESHOLD:
                self.velocity = (0, 1)

        self.x += self.velocity[0]
        self.y += self.velocity[1]

        self.x, self.y = constrain(self.x, self.y)

        if MAP[self.y][self.x] == 3:
            self.x = prev_x
            self.y = prev_y

    def eat_dot(self):
        if MAP[self.y][self.x] == 1:
            MAP[self.y][self.x] = 0
            self.score += 1

    def move_ghosts(self):
        if self.tick % GHOST_SPEED != 0:
            return

        print(self.x, self.y, self.ghosts)

        def valid_move(x, y):
            # Valid if not a wall, and no ghost in that position.
            return MAP[y][x] != 3 and (x, y) not in self.ghosts

        ghosts = []
        for x, y in self.ghosts:
            choice = random.randint(0, 3)

            if choice == 1:
                dx, dy = random.randint(-1, 1), 0

            elif choice == 2:
                dx, dy = 0, random.randint(-1, 1)

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
        #display.clear()

        # Draw the active portion of the map on the screen.
        # centered around the users location, out of bounds not drawn.
        map_x_range = range(self.x-2, self.x+2+1)
        map_y_range = range(self.y-2, self.y+2+1)
        for dx, x in enumerate(map_x_range):
            for dy, y in enumerate(map_y_range):

                if out_of_bounds(x, y):
                    pixel = 3

                # Ghost
                elif (x, y) in self.ghosts:
                    pixel = (self.tick % 2) * 3

                # Fruit
                elif MAP[y][x] == 2:
                    pixel = (self.tick % MAP[y][x]) + 1

                # Player (set to solid 2)
                elif dx == 2 and dy == 2:
                    pixel = 2

                else:
                    pixel = MAP[y][x]

                display.set_pixel(dx, dy, pixel * 3)



    def game_over(self):
        return False

# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.PACMAN)
    wait_for_button()

    game.reset() # Reset the game state.
    while not game.game_over():
        game.handle_input()
        game.eat_dot()
        game.move_ghosts()
        game.draw()
        sleep(250)

    display.show(Image.ANGRY)
    sleep(1000)
    display.scroll(game.moves)
