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

# above ^ can also be solved with:
#def has_player(self, player_name):
    #return self.players.count(player) >0
# (there are multiple ways of solving these problems)
#orx
#return player in self.players

    def play_game(self, win):
        if win:
            self.points += 3



    


