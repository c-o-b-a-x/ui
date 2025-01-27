from tkinter import *
import random
from utilities import determine_winner, convert_to_play
import open_file as of
from competition import RPSTournament

def tourny():
    tournament = RPSTournament()
    tournament.root.mainloop()

def play_game():
    global player_choice
    
    if player_choice is None:
        error_label.config(text="Please select Rock, Paper, or Scissors!")
        return
    error_label.config(text="")
    
    computer_choice = random.choice(["r", "p", "s"])
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == "win":
        score["Wins"] += 1
    elif result == "lose":
        score["Losses"] += 1
    else:
        score["Ties"] += 1

    update_score_display()

def update_score_display():
    wins_label.config(text=f"Wins: {score['Wins']}")
    losses_label.config(text=f"Losses: {score['Losses']}")
    ties_label.config(text=f"Ties: {score['Ties']}")

def reset_game():
    global player_choice
    player_choice = None

    score["Wins"] = 0
    score["Losses"] = 0
    score["Ties"] = 0
    
    computer_img = PhotoImage(file="Resources/tbd100.png")
    computer_label.config(image=computer_img)
    computer_label.image = computer_img
    player_label.config(image=computer_img)
    player_label.image = computer_img
    
    player_choice_var.set(None)
    
    update_score_display()

def update_player_choice():
    global player_choice
    if player_choice_var.get() == 1:
        player_choice = "r"
    elif player_choice_var.get() == 2:
        player_choice = "p"
    elif player_choice_var.get() == 3:
        player_choice = "s"

window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")

top_level_menubar = Menu(window)
window.config(menu=top_level_menubar)

options_menu = Menu(top_level_menubar, tearoff=0)
top_level_menubar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Tournament Mode", command=tourny)

frame = Frame(window)
frame.grid(row=0, column=0)

player_choice_var = IntVar()

rock_button = Radiobutton(frame, text="Rock", variable=player_choice_var, value=1, command=update_player_choice)
rock_button.grid(row=0, column=0)

paper_button = Radiobutton(frame, text="Paper", variable=player_choice_var, value=2, command=update_player_choice)
paper_button.grid(row=0, column=1)

scissors_button = Radiobutton(frame, text="Scissors", variable=player_choice_var, value=3, command=update_player_choice)
scissors_button.grid(row=0, column=2)

player_img = PhotoImage(file="Resources/tbd100.png")
player_label = Label(frame, image=player_img)
player_label.grid(row=1, column=0)
player_label.image = player_img  # Prevent garbage collection

Label(frame, text="VS").grid(row=1, column=1)

computer_img = PhotoImage(file="Resources/tbd100.png")
computer_label = Label(frame, image=computer_img)
computer_label.grid(row=1, column=2)
computer_label.image = computer_img  # Prevent garbage collection

error_label = Label(window, text="", fg="red")
error_label.grid(row=1, column=0, columnspan=3)

Label(window, text="MAKE YOUR MOVE").grid(row=2, column=0, columnspan=3)

play_button = Button(window, text="Play", command=play_game)
play_button.grid(row=3, column=0)

score = {"Wins": 0, "Losses": 0, "Ties": 0}

frame_score = Frame(window)
frame_score.grid(row=4, column=0, columnspan=3)

wins_label = Label(frame_score, text="Wins: 0")
wins_label.grid(row=4, column=0)

losses_label = Label(frame_score, text="Losses: 0")
losses_label.grid(row=4, column=1)

ties_label = Label(frame_score, text="Ties: 0")
ties_label.grid(row=4, column=2)

reset_button = Button(window, text="Reset Scores", command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3)

player_choice = None

window.mainloop()