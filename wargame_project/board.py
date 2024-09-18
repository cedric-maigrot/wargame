class Building:
    def __init__(self, position, board_width, board_height):
        self.position = position
        self.check_building_position(board_width, board_height)

    def check_building_position(self, board_width, board_height):
        # Get the position of the building
        self.building_x_min, self.building_y_min, self.building_x_max, self.building_y_max = self.position

        # Get the width and height of the building
        self.building_width = self.building_x_max - self.building_x_min
        self.building_height = self.building_y_max - self.building_y_min

        # Check if the building is within the board boundaries
        if (
            self.building_x_min < 0
            or self.building_x_min + self.building_width > board_width
            or self.building_y_min < 0
            or self.building_y_min + self.building_height > board_height
        ):
            raise ValueError("Building is not fully within the board")


class Board:
    def __init__(self, width, height):
        self.obstacles = []
        self.width = width
        self.height = height

        # Ajoute trois building
        self.add_building((500, 500, 550, 600))
        self.add_building((600, 620, 650, 650))
        self.add_building((260, 200, 300, 300))

    def get_dimensions(self):
        return (self.width, self.height)

    def add_building(self, position):
        building = Building(position=position, board_width=self.width, board_height=self.height)
        self.obstacles.append(building)

    def remove_building(self, position):
        for building in self.obstacles:
            if building.position == position:
                self.obstacles.remove(building)
                break
