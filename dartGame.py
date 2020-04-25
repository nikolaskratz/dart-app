import audioManager

current_points = 0


def startGame(start_points):
    current_points = start_points
    darts_used = 0
    score = 0
    print("Started game")
    while current_points>0:
        score = audioManager.listen_for_int()
        current_points -= score
        print("Score: {}; RemainingPoints: {}; DartsUsed: {}".format(score, current_points, darts_used))
        darts_used += 3

    print("You've finished the game using {} darts".format(darts_used))
    audioManager.speak("Youve finished the game using {} darts".format(darts_used))


startGame(301)