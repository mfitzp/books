from microbit import *
import random

MIN_COORD = 0
MAX_COORD = 4
MIN_VEHICLES = 3
VEHICLE_LENGTH = 3
VEHICLE_MIN_SPEED = 3

def wait_for_button():
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


def in_bounds(x, y):
    if x < MIN_COORD or x > MAX_COORD:
        return False
    if y < MIN_COORD or y > MAX_COORD:
        return False
    return True



class Game:

    def reset(self):
        # Initial values, player at middle-bottom of screen.
        self.x = 2
        self.y = 4

        self.n_vehicles = MIN_VEHICLES
        self.vehicles = []
        self.level = 1
        self.tick = 0

        self.lane_speeds = [random.randint(1, VEHICLE_MIN_SPEED) for _ in range(5)]


    def handle_input(self):
        self.tick += 1
        acc_x = accelerometer.get_x()

        if acc_x < -256:
            self.x = self.x - 1
        if acc_x > 256:
            self.x = self.x + 1

        if self.x > MAX_COORD:
            self.x = MAX_COORD

        if self.x < MIN_COORD:
            self.x = MIN_COORD


        if button_b.was_pressed():
            # Jump up the screen.
            self.y = self.y - 1

        if button_a.was_pressed():
            # Jump back.
            self.y = self.y + 1
            if self.y > 4:
                self.y = 4


    def level_up(self):
        if self.y == -1:
            # Clear board.
            self.vehicles = []
            self.y = 4
            self.n_vehicles += 1
            self.level += 1
            self.lane_speeds = [random.randint(1, VEHICLE_MIN_SPEED) for _ in range(5)]
            display.scroll(game.level)



    def add_vehicles(self):
        # Each vehicle is actually added as a series of indivudal pixels.
        # they are moved independently for simplicity.
        if len(self.vehicles) < self.n_vehicles:
            # Generate a random vehicle.
            vehicle_length = random.randint(1, VEHICLE_LENGTH)
            vehicle_lane = random.randint(0, 3)
            for n in range(vehicle_length):
                if vehicle_lane % 2:
                    x = -1 - n
                else:
                    x = 5 + n
                self.vehicles.append((x, vehicle_lane))

    def draw(self):
        display.clear()

        for x, y in self.vehicles:
            if in_bounds(x, y):
                display.set_pixel(x, y, 7)

        display.set_pixel(self.x, self.y, 9)



    def lane_speed(self, y):
        # Lane speed is set on init.
        if self.tick % self.lane_speeds[y]:
            return 0

        # Half lanes have positive speed, half negative.
        if y % 2 == 0:
            return -1
        return 1

    def move_vehicles(self):

        # Movement is determined by the row of the vehicle.
        vehicles = []
        for x, y in self.vehicles:
            lane_x_delta = self.lane_speed(y)
            if not lane_x_delta:
                vehicles.append((x, y))
                continue # No update this time.

            new_x = x+lane_x_delta
            # Update if we're still in bounds.
            if (
                (lane_x_delta > 0 and new_x <= MAX_COORD) or
                (lane_x_delta < 0 and new_x >= MIN_COORD)
            ):
                vehicles.append((new_x, y))

        self.vehicles = vehicles

    def game_over(self):
        return (self.x, self.y) in self.vehicles

# Main loop

game = Game() # Create our game object.

while True:

    display.show(Image.RABBIT)
    wait_for_button()

    display.scroll(1)
    game.reset() # Reset the game state.
    while not game.game_over():
        game.handle_input()
        game.level_up()
        game.move_vehicles()
        game.add_vehicles()
        game.draw()

        sleep(250)

    display.show(Image.ANGRY)
    sleep(1000)