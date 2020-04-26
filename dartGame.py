import audioManager


def start_game(player_names, start_points):
    player_details = []
    game_running = True
    for player in player_names:
        player_details.append(
            {'name': player, 'current_points': start_points, 'darts_used': 0, 'score_prev': 0})
    while game_running:
        for i in range(0, len(player_details)):
            if(not(game_running)):
                break
            print("{}s turn".format(player_details[i]['name']))
            audio_input = audioManager.get_audio_input()
            score = audio_input[0]
            if not (audio_input[1]):
                player_details[i]['current_points'] -= score
                player_details[i]['score_prev'] = score
                player_details[i]['darts_used'] += 3
                print("NORMAL")
            else:
                while audio_input[1]:
                    print("CORRECTION")
                    if i == 0:
                        j = len(player_details) - 1
                    else:
                        j = i - 1
                    player_details[j]['current_points'] = \
                        player_details[j]['current_points'] - score + player_details[j]['score_prev']
                    print("Corrected score for {}, RemainingPoints: {}".
                          format(player_details[j]['name'], player_details[j]['current_points']))
                    audioManager.speak("Corrected score")
                    audio_input = audioManager.get_audio_input()
                    score = audio_input[0]
                    if not (audio_input[1]):
                        player_details[i]['current_points'] -= score
                        player_details[i]['score_prev'] = score
                        player_details[i]['darts_used'] += 3

            print("{} scored {} Points; RemainingPoints: {}; DartsUsed: {}".format(player_details[i][
                                                                                       'name'], score,
                                                                                   player_details[i][
                                                                                       'current_points'],
                                                                                   player_details[i][
                                                                                       'darts_used']))
            print("correction: {}".format(audio_input[1]))
            if player_details[i]['current_points'] == 0:
                game_running = False
                audioManager.speak("How many darts")
                audio_input = audioManager.get_audio_input()
                player_details[i]['darts_used'] = player_details[i]['darts_used'] - 3 + audio_input[0]
                print("{} won the game using {} darts".format(player_details[i]['name'], player_details[i][
                    'darts_used']))
                audioManager.speak("{} won the game using {} darts".format(player_details[i]['name'],
                                                                           player_details[i]['darts_used']))

    for p2 in player_details:
        if p2['current_points']>0:
            print("{} has {} Points remaining".format(p2['name'], p2['current_points']))
            audioManager.speak("{} has {} Points remaining".format(p2['name'], p2['current_points']))


start_game(["Niko", "Mareike"], 301)
