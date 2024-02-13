from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4

DIRECTIONS = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1),
}

FOOD_FLASH = [9, 0, 9, 0, 9, 0]

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

class Game:

    def reset(self):
        # Initial values
        self.x = 2
        self.y = 2

        self.length = 2

        self.direction = 'right'  # x, y
        self.tail = [(self.x, self.y)]  # Start in this spot.

        self.food = None
        self.moves = 0
        self.score = 0

    def handle_input(self):
        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        if abs(acc_x) > abs(acc_y):
            if acc_x < -100:
                self.direction = "left"
            if acc_x > 100:
                self.direction = "right"

        else:
            if acc_y < -100:
                self.direction = "up"
            if acc_y > 100:
                self.direction = "down"

    def move(self):
        # Append the current self.x and self.y to tail as a 2-tuple.
        self.tail.append((self.x, self.y))
        self.tail = self.tail[-self.length:]

        # Look up the tuple x_speed, y_speed, unpack to the variables.
        x_speed, y_speed = DIRECTIONS[self.direction]

        self.x += x_speed
        self.y += y_speed

        self.moves += 1
        self.score += self.length

    def wrap(self):
        if self.x > MAX_COORD:
            self.x = MIN_COORD
        if self.x < MIN_COORD:
            self.x = MAX_COORD
        if self.y > MAX_COORD:
            self.y = MIN_COORD
        if self.y < MIN_COORD:
            self.y = MAX_COORD

    def eat_food(self):
        # Check if food eaten, add new.
        if (self.x, self.y) == self.food:
            self.food = None
            self.length += 1

    def add_food(self):
        if self.food is None: # No food, add it.
            # Pick random spot on map, that isn't in tail.
            # If we clash, wait til next tick -- get's harder!
            position = (
                random.randint(MIN_COORD, MAX_COORD),
                random.randint(MIN_COORD, MAX_COORD)
            )
            if position != (self.x, self.y) and position not in self.tail:
                self.food = position

    def draw(self):
        display.clear()

        for pos in self.tail:
            display.set_pixel(pos[0], pos[1], 7)

        display.set_pixel(self.x, self.y, 9)

    def draw_food(self, intensity):
        if self.food:
            display.set_pixel(self.food[0], self.food[1], intensity)

    def game_over(self):
        return self.moves > 1 and (self.x, self.y) in self.tail


game = Game() # Create our game object.

# Main loop
while True:

    display.show(Image.SNAKE)
    wait_for_button()


    game.reset() # Reset the game state.

    while not game.game_over():
        game.handle_input()
        game.move()
        game.wrap()
        game.draw()

        game.eat_food()
        game.add_food()

        # Wait while blinking the food location.
        for intensity in FOOD_FLASH:
            game.draw_food(intensity)
            sleep(50)

    display.show(Image.ANGRY)
    sleep(1000)
    display.scroll(game.score)