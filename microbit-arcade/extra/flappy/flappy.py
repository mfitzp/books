from microbit import *
import random

Y_ACCELERATION = -0.3
Y_GRAVITY = 0.1
LEVEL_INCREMENT = 50

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


class Game:

    def reset(self):
        self.y = 2  # x is always 0 (far left)
        self.yf = 2.0
        self.y_velocity = 0

        # Initial values, player at middle-bottom of screen.
        self.map = [
            # The visible map, we add features to the top, scroll it down
            # line by line each tick. Map is transposed when displayed.
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.score = 0

        self.tick = 0
        self.difficulty = 10  # Reverse. decrease to increase diff.
        self.speed = 3

    def handle_input(self):
        self.tick +=1
        if button_a.was_pressed() or button_b.was_pressed():
            self.y_velocity += Y_ACCELERATION

    def update_position(self):
        self.yf += self.y_velocity
        self.y_velocity += Y_GRAVITY

        if self.yf < 0:
            self.yf = 0
            self.y_velocity = 0

        elif self.yf > 4:
            self.yf = 4
            self.y_velocity = 0

        self.y = int(self.yf)

    def maybe_add_bar(self):
        if self.tick % self.speed:
            return

        self.map = self.map[1:]
        self.score += 1

        if len(self.map) > 5:
            return

        if random.randint(0, 1):
            self.map.append([0, 0, 0, 0, 0])

        else:
            # Add bar.
            bar_length = random.randint(0, 4)
            bar = [1] * bar_length
            zeros = [0] * (5 - bar_length)
            if random.randint(0, 1):
                line = bar + zeros

            else:
                line = zeros + bar

            self.map.append(line)
            self.map.append([0, 0, 0, 0, 0])
            self.map.append([0, 0, 0, 0, 0])

    def levelup(self):
        if self.tick % LEVEL_INCREMENT == 0:
            self.difficulty -= 1

            if self.difficulty == 0:
                self.difficulty = 1

    def draw(self):
        for x in range(5):
            for y in range(5):
                display.set_pixel(x, y, self.map[x][y] * 7)

        display.set_pixel(0, self.y, 9)


    def game_over(self):
        return self.map[0][self.y]

# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.DUCK)
    wait_for_button()

    game.reset() # Reset the game state.
    while not game.game_over():
        # We move on button press.

        game.handle_input()
        game.update_position()

        game.maybe_add_bar()
        game.draw()

        game.levelup()

        sleep(250)

    display.show(Image.ANGRY)
    sleep(1000)
    display.scroll(game.score)