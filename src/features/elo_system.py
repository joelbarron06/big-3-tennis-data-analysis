import pandas as pd

class EloSystem:
    def __init__(self, k_factor=32, initial_rating=1500):
        self.ratings = {}
        self.grass_ratings = {}
        self.clay_ratings = {}
        self.hard_ratings = {}
        self.carpet_ratings = {}
        self.k_factor = k_factor
        self.initial_rating = initial_rating

    def get_rating(self, player, surface=None): # returns overall and surface specific rating if surface is provided
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
        
    def expected_score(self, r_w, r_l): # expected score of winner
        return 1 / (1 + 10**((r_l - r_w) / 400))

    def update_rating(self, winner, loser, surface=None):
        surfaces = ['Grass', 'Clay', 'Hard', 'Carpet']
        k = self.k_factor

        if surface in surfaces:
            r_w, r_w_surface = self.get_rating(winner, surface)
            r_l, r_l_surface = self.get_rating(loser, surface)
        else:
            r_w = self.get_rating(winner)
            r_l = self.get_rating(loser)

        # calculate winner's overall rating
        e_w = self.expected_score(r_w, r_l)
        e_l = 1 - e_w

        r_w_new = r_w + k * (1 - e_w)  
        r_l_new = r_l + k * (0 - e_l)

        # calculate winner's surface specific rating
        if surface in surfaces:
            e_w_surface = self.expected_score(r_w_surface, r_l_surface)
            e_l_surface = 1 - e_w_surface

            r_w_new_surface = r_w_surface + k * (1 - e_w_surface)
            r_l_new_surface = r_l_surface + k * (0 - e_l_surface)

        # update ratings
        self.ratings[winner] = r_w_new
        self.ratings[loser] = r_l_new

        if surface in surfaces:
            if surface == 'Grass':
                self.grass_ratings[winner] = r_w_new_surface
                self.grass_ratings[loser] = r_l_new_surface
            elif surface == 'Clay':
                self.clay_ratings[winner] = r_w_new_surface
                self.clay_ratings[loser] = r_l_new_surface
            elif surface == 'Hard':
                self.hard_ratings[winner] = r_w_new_surface
                self.hard_ratings[loser] = r_l_new_surface
            elif surface == 'Carpet':
                self.carpet_ratings[winner] = r_w_new_surface
                self.carpet_ratings[loser] = r_l_new_surface

        return 

    def process_match_df(self, df):
        elo_df = df.copy()
        for row in elo_df:
            self.update_rating(row['winner_name'], row['loser_name'], row['surface'])
            row['winner_elo'] = self.get_rating(row['winner_name'])[0]
            row['loser_elo'] = self.get_rating(row['loser_name'])[0]
            row['winner_elo_surface'] = self.get_rating(row['winner_name'], row['surface'])[1]
            row['loser_elo_surface'] = self.get_rating(row['loser_name'], row['surface'])[1]
        return elo_df
    
    def create_time_series_df(self, df):
        ...

