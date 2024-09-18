import pygame
import random
import math

def display_buildings(screen, board):
    for building in board.obstacles:
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                building.position[0],
                building.position[1],
                building.position[2] - building.position[0],
                building.position[3] - building.position[1],
            ),
        )

def display_teams(screen, alliances, board):
    font = pygame.font.Font(None, 24)
    for alliance in alliances:
        alliance_health = alliance.get_health()
        for team in alliance.teams:
            team_health = team.get_health()
            if team.zone == "top-left":
                text = font.render(
                    f"{team.name} - Team HP: {team_health}",
                    True,
                    team.color,
                )
                screen.blit(text, (10, 10 + alliance.teams.index(team) * 30))
                text = font.render(
                    f"    {alliance.name} - Alliance HP: {alliance_health}",
                    True,
                    alliance.color,
                )
                screen.blit(text, (10, 10 + alliance.teams.index(team) * 30 + 20))
            elif team.zone == "top-right":
                text = font.render(
                    f"{team.name} - Team HP: {team_health}",
                    True,
                    team.color,
                )
                screen.blit(text, (10, board.height - 100 + alliance.teams.index(team) * 30))
                text = font.render(
                    f"    {alliance.name} - Alliance HP: {alliance_health}",
                    True,
                    alliance.color,
                )
                screen.blit(text, (10, board.height - 100 + alliance.teams.index(team) * 30 + 20))
            elif team.zone == "bottom-left":
                text = font.render(
                    f"{team.name} - Team HP: {team_health}",
                    True,
                    team.color,
                )
                screen.blit(text, (board.width - 300, 10 + alliance.teams.index(team) * 30))
                text = font.render(
                    f"    {alliance.name} - Alliance HP: {alliance_health}",
                    True,
                    alliance.color,
                )
                screen.blit(text, (board.width - 300, 10 + alliance.teams.index(team) * 30 + 20))
            elif team.zone == "bottom-right":
                text = font.render(
                    f"{team.name} - Team HP: {team_health}",
                    True,
                    team.color,
                )
                screen.blit(text, (board.width - 300, board.height - 100 + alliance.teams.index(team) * 30))
                text = font.render(
                    f"    {alliance.name} - Alliance HP: {alliance_health}",
                    True,
                    alliance.color,
                )
                screen.blit(text, (board.width - 300, board.height - 100 + alliance.teams.index(team) * 30 + 20))

def display_units(screen, alliances):
    for alliance in alliances:
        for team in alliance.teams:
            for unit in team.units:
                if unit.is_alive():
                    pygame.draw.circle(
                        screen, 'black', (unit.position[0], unit.position[1]), 8
                    )
                    pygame.draw.circle(
                        screen, alliance.color, (unit.position[0], unit.position[1]), 7
                    )

                    pygame.draw.circle(
                        screen, team.color, (unit.position[0], unit.position[1]), 5
                    )

                    pygame.draw.line(
                        screen,
                        'black',
                        (unit.position[0] + 5, unit.position[1] - 5),
                        (unit.position[0] - 5, unit.position[1] + 5),
                        2
                    )

                    pygame.draw.line(
                        screen,
                        'black',
                        (unit.position[0] - 5, unit.position[1] - 5),
                        (unit.position[0] + 5, unit.position[1] + 5),
                        2
                    )

                    orientation_vector = (
                        math.cos(math.radians(unit.orientation)) * 10,
                        math.sin(math.radians(unit.orientation)) * 10
                    )
                    if unit.status == "moving":
                        pygame.draw.line(
                            screen,
                            (0, 0, 0),
                            unit.position,
                            (
                                unit.position[0] + orientation_vector[0],
                                unit.position[1] + orientation_vector[1],
                            ),
                            2
                        )
                    elif unit.status == "attacking":
                        if random.random() > 0.5:
                            pygame.draw.line(
                                screen,
                                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                unit.position,
                                (
                                    unit.position[0] + 5 * orientation_vector[0],
                                    unit.position[1] + 5 * orientation_vector[1],
                                ),
                                1
                            )

                        pygame.draw.line(
                            screen,
                            alliance.color,
                            unit.position,
                            (
                                unit.position[0] + orientation_vector[0],
                                unit.position[1] + orientation_vector[1],
                            ),
                            2
                        )
                    pygame.draw.line(
                        screen,
                        (0, 0, 0),
                        unit.position,
                        (
                            unit.position[0] + orientation_vector[0],
                            unit.position[1] + orientation_vector[1],
                        ),
                        4
                    )

                    pygame.draw.rect(
                        screen,
                        (255, 0, 0),
                        (unit.position[0] - 10, unit.position[1] - 15, 20, 3),
                    )
                    pygame.draw.rect(
                        screen,
                        (0, 0, 0),
                        (unit.position[0] - 10, unit.position[1] - 15, 20 * (unit.hp / unit.hp_max), 3),
                    )

def display_board(screen, board, alliances):
    screen.fill((255, 255, 255))
    display_buildings(screen, board)
    display_teams(screen, alliances, board)
    display_units(screen, alliances)
    pygame.display.flip()
