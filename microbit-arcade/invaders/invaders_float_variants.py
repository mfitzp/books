from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
DIFFICULTY_INCREASE = 0.25
BOMB_HIT_CHANCE = 3

ALIEN_START_POSITIONS = [
    [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1)],
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (2, 1)],
    [(1, 0), (2, 0), (3, 0), (0, 1), (2, 1), (4, 1)],
    [(1, 0), (2, 0), (3, 0), (1, 1), (3, 1), (2, 2)],
]

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


class Game:

    def reset(self):
        # Initial values
        self.x = 2
        self.xf = 2.0 # sensitivity.

        self.missiles = []
        self.aliens = []
        self.alien_velocity_x = 1

        self.bombs = 3
        self.active_bomb = 0

        self.score = 0

        self.tick = 0
        self.level = 0
        self.difficulty = 20 # Is in reverse, decrement to increase.


    def handle_input(self):
        acc_x = accelerometer.get_x()

        if acc_x < 0:
            self.xf += acc_x / 512
        if acc_x > 0:
            self.xf += acc_x / 512

        if self.xf > MAX_COORD:
            self.xf = MAX_COORD

        if self.xf < MIN_COORD:
            self.xf = MIN_COORD

        self.x = int(self.xf)

        if button_a.was_pressed():
            # Add missile.
            self.missiles.append((self.x, 4))

        if button_b.was_pressed() and self.bombs:
            # Fire bomb. Flash + remove 1/BOMB_HIT_CHANCE of the aliens.
            self.aliens = [alien for alien in self.aliens if random.randint(0, BOMB_HIT_CHANCE)]
            self.active_bomb = 3 # Reduces 1 per tick. Screen at 3 * bright.
            self.bombs -= 1

    def add_aliens(self):
        # We need to copy, or we'll me modifying the original lists.
        alien_position = self.level % len(ALIEN_START_POSITIONS)
        self.aliens = ALIEN_START_POSITIONS[alien_position].copy()
        self.tick = 0

    def advance_aliens(self):
        for x, y in self.aliens:
            if (
                (self.alien_velocity_x == -1 and x == MIN_COORD) or
                (self.alien_velocity_x == +1 and x == MAX_COORD)
            ):
                # If any aliens are at the far edge, increment y, and reverse.
                self.alien_velocity_x = -self.alien_velocity_x
                self.aliens = [move(alien, 0, 1) for alien in self.aliens]
                # This can happen if detached alien slips past bottom.
                self.aliens = [alien for alien in self.aliens if in_bounds(alien)]
                return True # No other move this time.

    def aliens_can_move(self):
        self.tick += 1
        if self.tick > self.difficulty:
            self.tick = 0
            return True

    def move_aliens(self):
        self.aliens = [move(alien, self.alien_velocity_x, 0) for alien in self.aliens]

    def move_missiles(self):
        # Advance positions of missiles (upwards)
        self.missiles = [move(missile, 0, -1) for missile in self.missiles]
        self.missiles = [missile for missile in self.missiles if in_bounds(missile)]

    def check_collisions(self):
        for missile in self.missiles[:]:  # Iterate a copy.
            if missile in self.aliens:
                # Since we store by coordinates, we can remove using the missile coords.
                self.aliens.remove(missile)
                self.missiles.remove(missile)
                self.score += 1

        if not self.aliens:
            self.difficulty -= DIFFICULTY_INCREASE
            self.level += 1
            self.bombs += 1
            self.add_aliens()

    def draw(self):
        display.clear()

        if self.active_bomb:
            for dx in range(MAX_COORD + 1):
                for dy in range(MAX_COORD + 1):
                    display.set_pixel(dx, dy, self.active_bomb * 3)
            self.active_bomb -= 1


        for pos in self.aliens:
            display.set_pixel(pos[0], pos[1], 9)

        for pos in self.missiles:
            display.set_pixel(pos[0], pos[1], 5)

        display.set_pixel(self.x, 4, 9)

    def game_over(self):
        return (self.x, 4) in self.aliens

# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.TARGET)
    wait_for_button()


    game.reset() # Reset the game state.
    game.add_aliens()
    while not game.game_over():
        game.handle_input()
        if game.aliens_can_move():
            if not game.advance_aliens():
                game.move_aliens()
        game.move_missiles()
        game.draw()
        game.check_collisions()

        sleep(100)

    display.show(Image.ANGRY)
    sleep(1000)
    display.scroll(game.score)