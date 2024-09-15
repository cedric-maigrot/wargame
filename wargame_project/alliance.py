class Alliance:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self, team):
        self.teams.remove(team)

    def get_teams(self):
        return self.teams
    
    def is_alive(self):
        return any(team.is_alive() for team in self.teams)