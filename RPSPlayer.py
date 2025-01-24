class RPSPlayer:
    def __init__(self, name, plays):
        self.name = name
        self.plays = plays
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.series_wins = 0

    def calculate_score(self):
        return self.wins + (0.5 * self.ties)

    def __str__(self):
        return f"{self.name}: plays: {self.plays} wins: {self.wins} losses: {self.losses} ties: {self.ties} score: {self.calculate_score()} series_wins: {self.series_wins}"
