class Implementation:
    """
    A class that represents an implementation of the Elo Rating System
    """

    def __init__(self, base_rating=1000):
        """
        Runs at initialization of class object.
        @param base_rating - The rating a new player would have
        """
        self.base_rating = base_rating
        self.players = []

    #get player list
    def get_player_list(self):
        return self.players

    #get specific player
    def get_player(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
   
    #addplayer
    def add_player(self, name):
        self.players.append(player(name))


    #remove player
    #record match
    #def record_match(self, player1, player2, result):
    #get player rating
    #get rating list
    