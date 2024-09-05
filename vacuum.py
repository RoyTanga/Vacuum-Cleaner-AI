import random
import time

# Define the room size
ROOM_SIZE = 10

# Define the possible actions the vacuum can take
ACTIONS = ['move_forward', 'turn_left', 'turn_right', 'clean']

# Define the vacuum's initial position and orientation
class VacuumRobot:
    def __init__(self):
        self.x = random.randint(0, ROOM_SIZE - 1)
        self.y = random.randint(0, ROOM_SIZE - 1)
        self.orientation = random.choice(['north', 'south', 'east', 'west'])
        self.dirt_level = 0

    def move_forward(self):
        if self.orientation == 'north':
            self.y = max(self.y - 1, 0)
        elif self.orientation == 'south':
            self.y = min(self.y + 1, ROOM_SIZE - 1)
        elif self.orientation == 'east':
            self.x = min(self.x + 1, ROOM_SIZE - 1)
        else:
            self.x = max(self.x - 1, 0)

    def turn_left(self):
        directions = ['north', 'west', 'south', 'east']
        current_index = directions.index(self.orientation)
        self.orientation = directions[(current_index - 1) % len(directions)]

    def turn_right(self):
        directions = ['north', 'east', 'south', 'west']
        current_index = directions.index(self.orientation)
        self.orientation = directions[(current_index + 1) % len(directions)]

    def clean(self):
        self.dirt_level = 0

    def get_sensor_data(self):
        # Simulate sensor data
        return {
            'dirt_level': self.dirt_level,
            'position': (self.x, self.y),
            'orientation': self.orientation
        }

# Define the AI-powered cleaning algorithm
def clean_room(vacuum):
    while True:
        sensor_data = vacuum.get_sensor_data()
        dirt_level = sensor_data['dirt_level']

        if dirt_level > 0:
            print(f"Cleaning at ({sensor_data['position'][0]}, {sensor_data['position'][1]}) with dirt level {dirt_level}")
            vacuum.clean()
        else:
            print(f"No dirt detected at ({sensor_data['position'][0]}, {sensor_data['position'][1]})")
            action = random.choice(ACTIONS)
            if action == 'move_forward':
                vacuum.move_forward()
            elif action == 'turn_left':
                vacuum.turn_left()
            elif action == 'turn_right':
                vacuum.turn_right()
            else:
                vacuum.clean()

        time.sleep(1)  # Pause for 1 second

# Create and run the vacuum robot
vacuum = VacuumRobot()
clean_room(vacuum)