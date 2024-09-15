import random
from .units.unit import Unit


class Team:
    def __init__(self, name, color, board, zone):
        self.name = name
        self.color = color
        self.units = [Unit(f"Unit {x}", 100, 1, board, zone) for x in range(10)]

    def move(self, x, y):
        self.position = (x, y)

    def attack(self, target):
        # Implement the logic for attacking a target here
        pass

    def is_alive(self):
        return any(unit.is_alive() for unit in self.units) 