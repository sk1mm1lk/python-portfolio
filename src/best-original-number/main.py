#!/usr/bin/env python

# Author: David Dudov <github.com/sk1mm1lk>
# Date: 18-04-2023

import sys
import random
import csv

class Player():
    def __init__(self, player_id):
        self.player_id = player_id
        self.chosen_number = 0

    def pick_number(self, lower_bound, upper_bound):
        self.chosen_number = random.randint(lower_bound, upper_bound)

    def is_odd(self):
        return (self.chosen_number % 2 == 1)
    
    def to_string(self):
        return "P[{}] C[{}]".format(self.player_id, self.chosen_number)

def get_original_players(players):
    original_players = []
    is_original = True

    for i in range(len(players)):
        is_original = True

        for j in range(len(players)):
            if(i == j):
                continue
            if(players[i].chosen_number == players[j].chosen_number):
                is_original = False

        if is_original:
            original_players.append(players[i])

    return original_players

def get_max(players):
    max_value = 0
    max_player = None

    for player in players:
        if player.chosen_number > max_value:
            max_value = player.chosen_number
            max_player = player

    return max_player

def main():
    try:
        n_players = int(sys.argv[1])
    except Exception as e:
        raise e

    players = []
    odd_players = []
    even_players = []

    for i in range(n_players):
        current_player = Player(i + 1)
        current_player.pick_number(1, n_players * 3)
        print(current_player.to_string())

        players.append(current_player)
        if current_player.is_odd():
            odd_players.append(current_player)
        else:
            even_players.append(current_player)
    
    if len(odd_players) > len(even_players):
        original_players = get_original_players(even_players)
    elif len(odd_players) < len(even_players):
        original_players = get_original_players(odd_players)
    else:
        original_players = get_original_players(players)

    winner = get_max(original_players)
    print("The winner is:")
    print(winner.to_string())

    with open("game_results.csv", 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(['Player', 'Choice'])
        for player in players:
            csv_writer.writerow([player.player_id, player.chosen_number])
        csv_writer.writerow(['Winner','Choice'])
        csv_writer.writerow([winner.player_id, winner.chosen_number])

if __name__ == "__main__":
    main()
