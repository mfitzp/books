from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4

DIRECTIONS = [ (1, 0), (0, -1), (-1, 0), (0, 1) ]
MIN_DIRECTION, MAX_DIRECTION = 0, len(DIRECTIONS) - 1

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

        self.direction = 1 # x, y
        self.tail = [(self.x, self.y)]  # Start in this spot.

        self.food = None
        self.moves = 0
        self.score = 0


    def handle_input(self):
        if button_a.was_pressed():
            self.direction += 1

        if button_b.was_pressed():
            self.direction -= 1

        if self.direction < MIN_DIRECTION:
            self.direction = MAX_DIRECTION

        if self.direction > MAX_DIRECTION:
            self.direction = MIN_DIRECTION

    def move(self):
        # Add current position to tail.
        self.tail.append((self.x, self.y))
        self.tail = self.tail[-self.length:]

        direction = DIRECTIONS[self.direction]
        self.x += direction[0]
        self.y += direction[1]

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