import audioManager
from tkinter import *

def start_game(player_names, start_points):
    #setup gui
    p1['text']=player_names[1]
    p0['text']=player_names[0]
    pointsP0['text']=start_points
    pointsP1['text'] = start_points
    p0.config(bg="green")
    p1.config(bg="white")
    root.update_idletasks()

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
                updatePoints(player_details[i]['current_points'], player_details, player_details[i][
                    'name'], score)
                # pointsP1['text'] = score
                # root.update_idletasks()
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
                    updatePoints(player_details[j]['current_points'], player_details,
                                 player_details[j]['name'], score)
                    print("Corrected score for {}, RemainingPoints: {}".
                          format(player_details[j]['name'], player_details[j]['current_points']))
                    audioManager.speak("Corrected score")
                    audio_input = audioManager.get_audio_input()
                    score = audio_input[0]
                    if not (audio_input[1]):
                        player_details[i]['current_points'] -= score
                        player_details[i]['score_prev'] = score
                        player_details[i]['darts_used'] += 3
                        updatePoints(player_details[i]['current_points'], player_details,
                                     player_details[i]['name'], score)

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


def updatePoints(new_points, player_details, current_player, score):
    print(player_details[0]['name']+", "+current_player)
    if(player_details[0]['name']==current_player):
        pointsP0['text']=new_points
        score0['text']=score
        p1.config(bg="green")
        p0.config(bg="white")
    else:
        pointsP1['text']=new_points
        score1['text'] = score
        p0.config(bg="green")
        p1.config(bg="white")
    root.update_idletasks()

root = Tk()

def initGame(event):
    print("starting Game....")
    start_game(["Niko", "Mareike"], 301)

pointsP1 = Label(root, text="000",width=5, font=("Courier", 250))
pointsP0 = Label(root, text="000", width=5, font=("Courier", 250))
score0 = Label(root, text="sc0", width=5, font=("Courier", 150), bg="grey")
score1 = Label(root, text="sc1", width=5, font=("Courier", 150), bg="grey")
p1 = Label(root, text="P1", width=5, font=("Courier", 100))
p0 = Label(root, text="P0", width=5, font=("Courier", 100))
startButton = Button(root, text="Start Game", fg="red", width=30, font=("Courier", 100))

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

pointsP1.grid(row=1, column=1, sticky=N+S+E+W)
pointsP0.grid(row=1, column=0, sticky=N+S+E+W)
p1.grid(row=0, column=1, sticky=N+S+E+W)
p0.grid(row=0, column=0, sticky=N+S+E+W)
score0.grid(row=2, column=0, sticky=N+S+E+W)
score1.grid(row=2, column=1, sticky=N+S+E+W)
startButton.grid(row=3, columnspan=2, sticky=N+S+E+W)

startButton.bind("<Button-1>", initGame)

root.mainloop()

start_game(["Niko", "Mareike"], 301)

# start_game(["niko", "Mareike"], 301)