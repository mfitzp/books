from microbit import *

MIN_COORD = 0
MAX_COORD = 4


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

# tag::move[]
def move(sprite, x, y):
    # Simple helper function to increment x & y values in tuples (x, y),
    # returning the new values as a tuple.
    return (sprite[0] + x, sprite[1] + y)
# end::move[]


class Game:

    def reset(self):
        # Initial values
        self.x = 2

        self.missiles = []  # list of missile positions

    def handle_input(self):
        acc_x = accelerometer.get_x()

        if acc_x < -0:
            self.x -= 1
        if acc_x > 0:
            self.x += 1

        # Constrain to width of the display.
        if self.x > MAX_COORD:
            self.x = MAX_COORD

        if self.x < MIN_COORD:
            self.x = MIN_COORD

        if button_a.was_pressed():
            # Add missile at our current position.
            self.missiles.append((self.x, 4))

    # tag::move_missiles[]
    def move_missiles(self):
        # Advance positions of missiles (upwards)
        self.missiles = [move(missile, 0, -1) for missile in self.missiles]
    # end::move_missiles[]

    def draw(self):
        display.clear()

        # Draw the missile positions.
        for pos in self.missiles:
            display.set_pixel(pos[0], pos[1], 5)

        display.set_pixel(self.x, 4, 9)

    def game_over(self):
        return False


display.show(Image.TARGET)
wait_for_button()

game = Game() # Create our game object.
game.reset() # Reset the game state.

# tag::main_loop[]
while not game.game_over():
    game.handle_input()
    game.move_missiles()
    game.draw()
    sleep(150)
# end::main_loop[]
