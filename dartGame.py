import audioManager

current_points = 0


def startGame(start_points):
    current_points = start_points
    darts_used = 0
    score = 0
    score_prev = 0
    print("Started game")
    while current_points>0:
        audio_input = audioManager.get_audio_input()
        score = audio_input[0]
        if audio_input[1]:
            current_points = current_points - score + score_prev
            audioManager.speak("Corrected score")
        else:
            current_points -= score
            score_prev = score
            darts_used += 3
        print("Score: {}; RemainingPoints: {}; DartsUsed: {}".format(score, current_points, darts_used))
        print("correction: {}".format(audio_input[1]))

    audioManager.speak("How many darts")
    audio_input = audioManager.get_audio_input()
    darts_used = darts_used - 3 + audio_input[0]

    print("You've finished the game using {} darts".format(darts_used))
    audioManager.speak("Youve finished the game using {} darts".format(darts_used))


startGame(301)