# Best Original Number Game Simulation

## Description
This is an example normal form game that was part of an assignment of mine for and Artificial Intelligence paper

## Game Rules
- The game is intended to be a normal form game that is to be played by 3 or more players.
- The results of the game are impacted by the choices of all players together as opposed to individually
- Each player must pick a number between 1 and 3 times the number of players
- The players are then split into two groups: those with an odd number choice and those with an even number choice
- The group with the least number of players is taken, and if the group sizes are the same, then take everyone
- And the winner is taken from the chosen group based on the highest number chosen, that isn't chosen by anyone else

## Example:
| Player | Choice |
|--------|--------|
| 1      | 12     |
| 2      | 11     |
| 3      | 10     |
| 4      | 12     |
| 5      | 9      |
| 6      | 7      |
| 7      | 9      |

- So in the above scenario, there are 3 even number choices and 4 odd number choices
- So the even number group then get selected
- The highest number in the even group is 12, but since there are duplicates, that number is skipped
- Thus player 3 wins by choosing 10

## Usage
1. Run the python script with a commandline argument for the number of players to be simulated for the game.
2. The player IDs and their choices will be displayed on the screen as well as the winner of the game
3. See the new file `game_results.csv` made for csv format of the results
