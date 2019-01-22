# A project to process some data from friends playing Scrabble.
# This project is to practice the use of dictionaries.
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# lower case letter handling:
letters += [
  letter.lower() 
  for letter 
  in letters
]
points *= 2

# A dictionary that maps letters to their point values
letter_to_points = {
  key:value 
  for key, value 
  in zip(letters, points)
}

# adding a key, value pair for a blank tile
letter_to_points[" "] = 0

# This function takes in a word and returns how many points it's worth
def score_words(word):
  point_total = 0
  for w in word:
    if w in letter_to_points:
      point_total += letter_to_points[w]
  return point_total
    
# Test the score_word function
brownie_points = score_words("BROWNIE")
print(brownie_points)

### Scoring a game ###

# This dictionary maps players to a list of words they have played
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

# Function to calculate how many points each player earned
# dictionary is declared outside function to have larger scope
player_to_points = {}
def update_point_total():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_words(word)
    player_to_points[player] = player_points

# A function that adds a word to the list of words a player has 
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_total()





