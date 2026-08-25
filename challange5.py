# The high score Tracker Game 
while True:
    game_score = input("Guess a random game score? ").lower()
    if game_score == "stop":
        print("Game session ended!")
        break 

    elif int(game_score) > 100: # casting to int
       print("Wow! That's a new high score !")
    else : 
      print("Good try, keep playing " )