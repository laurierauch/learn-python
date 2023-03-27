letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# add lower case letters and the corresponding points
letters += [
  letter.lower()
  for letter in letters
]
points *= 2 

letter_to_points = {key:value for key, value in zip(letters, points)}

# add an empty tile
letter_to_points[" "] = 0

print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"Player1":["BLUE", "TENNIS", "EXIT"], "WordNerd": ["EARTH", "EYES", "MACHINE"], "LexiCon": ["ERASER", "BELLY", "HUSKY"], "ProfReader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)


def play_word(player, word):
  player_to_words[player].append(word)

play_word("WordNerd", "FLIBBERTIGIBBET")
print(player_to_words)

def update_point_totals(): 
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)

play_word("ProfReader", "QUESTION")
print(player_to_words)
update_point_totals()






