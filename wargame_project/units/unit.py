import random
import math

class Unit:
    def __init__(self, name, hp, damage, board, zone):
        """
        Initialize a unit with a name, health points, damage, and position.
        The position is randomly generated within the board boundaries.
        """
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.damage = damage
        self.generate_valid_position(board, zone)
        
        self.orientation = random.randint(0, 360)
        self.speed = 1
        self.status = "idle"

    def generate_valid_position(self,board, zone):
        # Generate a random position within the board boundaries
        # While the unit spawn in a building, generate a new position
        while True:
            self.position = self.generate_random_position(board, zone)
            building_collision = False
            for building in board.obstacles:
                if (
                    self.position[0] >= building.building_x_min
                    and self.position[0] <= building.building_x_max
                    and self.position[1] >= building.building_y_min
                    and self.position[1] <= building.building_y_max
                ):
                    building_collision = True
                    break
            if not building_collision:
                break
        

    def generate_random_position(self, board, zone):
        """
        Generate a random position within the board boundaries.
        """
        zone_parts = zone.split("-")
        top_bottom = zone_parts[0]
        left_right = zone_parts[1]

        board_dimensions = board.get_dimensions()
        if top_bottom == "top":
            top = 0
            bottom = board_dimensions[0] // 2
        elif top_bottom == "bottom":
            top = board_dimensions[0] // 2 + 1
            bottom = board_dimensions[0]
        else:
            raise ValueError("Invalid top/bottom value in zone")

        if left_right == "left":
            left = 0
            right = board_dimensions[1] // 2
        elif left_right == "right":
            left = board_dimensions[1] // 2 + 1
            right = board_dimensions[1]
        else:
            raise ValueError("Invalid left/right value in zone")

        return (random.randint(top, bottom), random.randint(left, right))

    def update(self, board, own_alliance, alliances):
        """
        Update the unit's position based on the game logic.
        """
        visible_enemies = []
        if self.is_alive():
            for alliance in alliances:
                if alliance != own_alliance:
                    for team in alliance.teams:
                        for unit in team.units:
                            if unit.is_alive():
                                distance = self.calculate_distance(self.position, unit.position)
                                if distance < 50 and self.is_in_field_of_view(unit.position):
                                    visible_enemies.append(unit)

        if visible_enemies:
            # If there are visible enemies, attack the first one
            enemy = visible_enemies[0]
            self.attack(enemy)
            self.status = "attacking"
        else:
            # If no enemies are visible, move forward
            self.move_forward(board)
            self.status = "moving"

    def attack(self, enemy):
        """
        Attack the enemy unit and reduce its health points.
        """
        enemy.hp -= self.damage
        print(f"{self.name} attacked {enemy.name} for {self.damage} damage.")
        # Unit turn to face the enemy
        self.orientation = self.calculate_angle(self.position, enemy.position)
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated.")

    def move_forward(self, board):
        """
        Move the unit forward by a fixed distance.
        """
        x, y = self.position
        angle = random.uniform(-5, 5) + self.orientation
        x += self.speed * math.cos(math.radians(angle))
        y += self.speed * math.sin(math.radians(angle))

        # Verify if the unit after the mouvement will not be in a building
        # If it is the case, the unit will not move
        for building in board.obstacles:
            if (
                x >= building.building_x_min
                and x <= building.building_x_max
                and y >= building.building_y_min
                and y <= building.building_y_max
            ):
                # Turn the unit in order to avoid the building
                self.orientation = (self.orientation + 5) % 360
                return

        self.position = (x, y)

        # If the unit is now outside the board boundaries, move it back inside
        spacing = 5
        if x < spacing:
            x = spacing
            self.orientation = (self.orientation + 5) % 360
        if x >= board.width - spacing:
            x = board.width - spacing
            self.orientation = (self.orientation + 5) % 360
        if y < spacing:
            y = spacing
            self.orientation = (self.orientation + 5) % 360
        if y >= board.height - spacing:
            y = board.height - spacing
            self.orientation = (self.orientation + 5) % 360

    def calculate_distance(self, position1, position2):
        """
        Calculate the distance between two positions using Euclidean distance formula.
        """
        x1, y1 = position1
        x2, y2 = position2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def is_in_field_of_view(self, position):
        """
        Check if a position is within the unit's field of view.
        The field of view is defined as a 45 degree angle in front of the unit.
        """
        # Calculate the angle between the unit's position and the target position
        angle = self.calculate_angle(self.position, position)

        # Check if the angle is within the field of view range
        return angle <= 45

    def calculate_angle(self, position1, position2):
        """
        Calculate the angle between two positions.
        """
        x1, y1 = position1
        x2, y2 = position2
        dx = x2 - x1
        dy = y2 - y1
        angle = math.degrees(math.atan2(dy, dx))
        return angle

    def is_alive(self):
        """
        Check if the unit is alive based on its health points.
        """
        return self.hp > 0