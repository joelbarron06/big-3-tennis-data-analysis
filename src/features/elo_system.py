class EloSystem:
    def __init__(self, k_factor=32, initial_rating=1500):
        self.ratings = {}
        self.grass_ratings = {}
        self.clay_ratings = {}
        self.hard_ratings = {}
        self.carpet_ratings = {}
        self.k_factor = k_factor
        self.initial_rating = initial_rating

    def get_rating(self, player, surface=None):
        if player not in self.ratings:
            self.ratings[player] = self.initial_rating
            self.grass_ratings[player] = self.initial_rating
            self.clay_ratings[player] = self.initial_rating
            self.hard_ratings[player] = self.initial_rating
            self.carpet_ratings[player] = self.initial_rating
        if surface == 'Grass':
            return self.ratings[player], self.grass_ratings[player]
        elif surface == 'Clay':
            return self.ratings[player], self.clay_ratings[player]
        elif surface == 'Hard':
            return self.ratings[player], self.hard_ratings[player]
        elif surface == 'Carpet':
            return self.ratings[player], self.carpet_ratings[player]
        else:
            return self.ratings[player]
        
    def expected_score(self, r_a, r_b):
        return 1 / (1 + 10**((r_b - r_a) / 400))
    
    def update_rating(self, player_a, player_b, result, surface=None):
        ...