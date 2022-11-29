class Team:
    def __init__(self, player_name, list_of_players, coach):
        self.name = player_name
        self.players = list_of_players
        self.coach = coach
        self.points = 0

    def add_player(self, name):
        self.players.append(name)

    def has_player(self, player_name):
        for player in self.players:
            if player_name == player:
                return True
        else:
            return False

    def play_game(self, win_or_lose):
        if win_or_lose == "win":
            self.points += 3
        
            

            

