class Building:
    def __init__(self, position, board_width, board_height):
        self.position = position
        self.check_building_position(board_width, board_height)

    def check_building_position(self, board_width, board_height):
        # Get the position of the building
        building_x, building_y = position

        # Get the width and height of the building
        building_width = 3  # Replace with the actual width of the building
        building_height = 3  # Replace with the actual height of the building

        # Check if the building is within the board boundaries
        if (
            building_x < 0
            or building_x + building_width > board_width
            or building_y < 0
            or building_y + building_height > board_height
        ):
            raise ValueError("Building is not fully within the board")


class Board:
    def __init__(self, width, height):
        self.obstacles = []
        self.width = width
        self.height = height

    def get_dimensions(self):
        return (self.width, self.height)

    def add_building(self, position):
        building = Building(position)
        self.obstacles.append(building)

    def remove_building(self, position):
        for building in self.obstacles:
            if building.position == position:
                self.obstacles.remove(building)
                break
