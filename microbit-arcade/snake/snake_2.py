from microbit import *


def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)

# tag::handle_input[]
class Game:

    def handle_input(self):
        acc_x = accelerometer.get_x()
        acc_y = accelerometer.get_y()

        if abs(acc_x) > abs(acc_y):
            if acc_x < -100:  # <1>
                self.x -= 1
            if acc_x > 100:
                self.x += 1

        else:
            if acc_y < -100:
                self.y -= 1
            if acc_y > 100:
                self.y += 1
# end::handle_input[]

    def reset(self):
        # Initial values
        self.x = 2
        self.y = 2

    def draw(self):
        display.clear()
        display.set_pixel(self.x, self.y, 9)


    def game_over(self):
        return False


game = Game() # Create our game object.
game.reset() # Reset the game state.

display.show(Image.SNAKE)
wait_for_button()

while not game.game_over():
    game.handle_input()
    game.draw()
    sleep(250)
