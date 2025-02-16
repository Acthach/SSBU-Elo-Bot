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
    """
    Calculates and updates the ratings of two players after a match
    Add a decay factor that adjust elo given and taken from players based on how much they have played against each other before
        In order to do this there needs to be a check for how many matches have been played between the two players

    """
    #get player rating
    #get rating list
    """ Display all players and their ratings and put them in a tier list"""
    # manually change player rating
    
