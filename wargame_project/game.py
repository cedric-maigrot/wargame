from .board import Board
from .team import Team
from .alliance import Alliance
from .drawing import display_board
import pygame
import math

class Game:
    def __init__(self):
        self.board = Board(width=800, height=700)
        self.alliances = []
        alliance1 = Alliance(
            "Alliance 1", color=(0, 157, 220)
        )  # Blue color for Alliance 1
        alliance1.add_team(
            Team("Team 1", color=(0, 104, 143), board=self.board, zone="top-left")
        )  # Dark blue color for Team 1
        alliance1.add_team(
            Team("Team 2", color=(107, 201, 238), board=self.board, zone="top-right")
        )  # Light blue color for Team 2
        self.alliances.append(alliance1)

        alliance2 = Alliance(
            "Alliance 2", color=(246, 130, 31)
        )  # Orange color for Alliance 2
        alliance2.add_team(
            Team("Team 3", color=(160, 79, 10), board=self.board, zone="bottom-left")
        )  # Dark orange color for Team 3
        alliance2.add_team(
            Team("Team 4", color=(251, 186, 130), board=self.board, zone="bottom-right")
        )  # Light orange color for Team 4
        self.alliances.append(alliance2)

    def start(self):
        # Start the game logic here
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode(self.board.get_dimensions())
        pygame.display.set_caption("Game Board")
        clock = pygame.time.Clock()
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            display_board(self.screen, self.board, self.alliances)
            self.play_turn()
            winner = self.check_winner()
            if winner:
                running = False
                self.end(winner)

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

    def end(self, winner):
        print(f"The winner is: {winner.name}")
        pygame.quit()
        exit()

    def play_turn(self):
        for alliance in self.alliances:
            for team in alliance.teams:
                for unit in team.units:
                    unit.update(self.board, alliance, self.alliances)

    


    def check_winner(self):
        # Implement the logic to check for a winner here
        alive_alliances = [
            alliance for alliance in self.alliances if alliance.is_alive()
        ]
        if len(alive_alliances) == 1:
            return alive_alliances[0]
        else:
            return None


# Create an instance of the Game class and start the game
game = Game()