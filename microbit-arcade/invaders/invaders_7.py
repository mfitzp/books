from microbit import *

MIN_COORD = 0
MAX_COORD = 4


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

def move(sprite, x, y):
    # Simple helper function to increment x & y values in tuples (x, y),
    # returning the new values as a tuple.
    return (sprite[0] + x, sprite[1] + y)

def in_bounds(pos):
    if pos[0] < MIN_COORD or pos[0] > MAX_COORD:
        return False
    if pos[1] < MIN_COORD or pos[1] > MAX_COORD:
        return False
    return True

 # tag::reset[]
class Game:

    def reset(self):
        # Initial values
        self.x = 2

        self.missiles = []
        self.aliens = []  # List of alien positions.
        # end::reset[]

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

    # tag::add_aliens[]
    def add_aliens(self):
        self.aliens = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1)]
    # end::add_aliens[]

    def move_missiles(self):
        # Advance positions of missiles (upwards).
        self.missiles = [move(missile, 0, -1) for missile in self.missiles]
        # Remove missiles that have moved out of bounds (off top of screen).
        self.missiles = [missile for missile in self.missiles if in_bounds(missile)]

    # tag::draw[]
    def draw(self):
        display.clear()

        # Draw the alien positions.
        for pos in self.aliens:
            display.set_pixel(pos[0], pos[1], 9)

        # Draw the missile positions.
        for pos in self.missiles:
            display.set_pixel(pos[0], pos[1], 5)

        display.set_pixel(self.x, 4, 9)
    # end::draw[]

    def game_over(self):
        return False


display.show(Image.TARGET)
wait_for_button()

# tag::main_loop[]
game = Game() # Create our game object.
game.reset() # Reset the game state.
game.add_aliens()

while not game.game_over():
    game.handle_input()
    game.move_missiles()
    game.draw()
    sleep(150)
# end::main_loop[]
