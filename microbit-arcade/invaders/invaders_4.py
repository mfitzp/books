from microbit import *

MIN_COORD = 0
MAX_COORD = 4


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


# tag::reset[]
class Game:

    def reset(self):
        # Initial values
        self.x = 2

        self.missiles = []  # list of missile positions

    # end::reset[]

    # tag::handle_input[]
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

    # end::handle_input[]

    # tag::draw[]
    def draw(self):
        display.clear()

        # Draw the missile positions.
        for pos in self.missiles:
            display.set_pixel(pos[0], pos[1], 5)

        display.set_pixel(self.x, 4, 9)
    # end::draw[]

    def game_over(self):
        return False


display.show(Image.TARGET)
wait_for_button()

game = Game() # Create our game object.
game.reset() # Reset the game state.


while not game.game_over():
    game.handle_input()
    game.draw()
    sleep(150)


