class BadmintonGame:
    def __init__(self):
        self.score_a = 0
        self.score_b = 0
        self.games_won_a = 0
        self.games_won_b = 0
        self.current_game = 1
        self.max_games = 3

    def add_point(self, player):
        if player == "A":
            self.score_a += 1
        elif player == "B":
            self.score_b += 1

        if self._game_over():
            self._end_game()

    def _game_over(self):
        if (self.score_a >= 21 or self.score_b >= 21) and abs(self.score_a - self.score_b) >= 2:
            return True
        if self.score_a == 30 or self.score_b == 30:
            return True
        return False

    def _end_game(self):
        if self.score_a > self.score_b:
            self.games_won_a += 1
        else:
            self.games_won_b += 1
        self.score_a = 0
        self.score_b = 0
        self.current_game += 1

    def match_winner(self):
        if self.games_won_a == 2:
            return "Player A"
        elif self.games_won_b == 2:
            return "Player B"
        return None
