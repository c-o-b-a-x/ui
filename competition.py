from tkinter import *
from tkinter import filedialog
from time import sleep
import open_file as of
from RPSPlayer import RPSPlayer
import utilities as utils

class RPSTournament:
    def __init__(self):
        self.players = []
        self.output_text = None
        self.root = Tk()
        self.root.title("RPS Tournament")
        self.images = {}
        self.player1_img_label = None
        self.player2_img_label = None
        self.add_images()
        self.add_info()
        self.setup_ui()

    def add_images(self):
        try:
            self.images["rock"] = PhotoImage(file="resources/rock100.png")
            self.images["paper"] = PhotoImage(file="resources/paper100.png")
            self.images["scissors"] = PhotoImage(file="resources/scissors100.png")
            self.images["question"] = PhotoImage(file="resources/tbd100.png")

            self.player1_img_label = Label(self.root, image=self.images["question"])
            self.vs_label = Label(self.root, text="VS")
            self.player2_img_label = Label(self.root, image=self.images["question"])

            self.player1_img_label.grid(row=0, column=0)
            self.vs_label.grid(row=0, column=1)
            self.player2_img_label.grid(row=0, column=2)
        except Exception as e:
            pass

    def add_info(self):
        self.info_frame = Frame(self.root)
        self.info_frame.grid(row=1, columnspan=3)

        self.competitors_label = Label(self.info_frame, text="")
        self.competitors_label.pack()

        self.outcome_label = Label(self.info_frame, text="")
        self.outcome_label.pack()

    def setup_ui(self):
        select_file_button = Button(self.root, text="Select File", command=self.browse_file)
        select_file_button.grid(row=2, column=0)

        run_tournament_button = Button(self.root, text="Run Tournament", command=self.run_tournament)
        run_tournament_button.grid(row=2, column=2)

        Label(self.root, text="Speed").grid(row=2, column=1)
        self.speed_scale = Scale(self.root, from_=0, to=1, resolution=0.05, orient=HORIZONTAL)
        self.speed_scale.grid(row=2, column=1)

        self.output_text = Text(self.root, height=20, wrap=WORD, width=60, state=DISABLED)
        self.output_text.grid(row=3, columnspan=3, padx=20, pady=20, sticky="nsew")

        scrollbar = Scrollbar(self.root, command=self.output_text.yview)
        scrollbar.grid(row=3, column=3, sticky='ns')
        self.output_text.config(yscrollcommand=scrollbar.set)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("multi rock, paper, scissors", "*.mrps")])
        if file_path:
            self.load_players_from_file(file_path)

    def load_players_from_file(self, file_path):
        self.players.clear()
        with open(file_path, 'r') as file:
            for line in file:
                name, *plays = line.strip().split(',')
                player = RPSPlayer(name, plays)
                self.players.append(player)
        self.print_all_players()

    def print_all_players(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)

        for player in self.players:
            self.output_text.insert(END, str(player) + '\n')

        self.output_text.config(state=DISABLED)

    def determine_winner(self, play1, play2):
        return utils.determine_winner(play1, play2)

    def update_images(self, play1, play2):
        play_mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        try:
            if self.player1_img_label and self.player2_img_label:
                self.player1_img_label.config(image=self.images[play_mapping[play1]])
                self.player2_img_label.config(image=self.images[play_mapping[play2]])
                self.root.update()
        except KeyError as e:
            print(f"Error updating images: {e}")
        except AttributeError as e:
            print(f"Error: {e}")

    def run_tournament(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]
                matchup_text = f"{player1.name} vs {player2.name}"

                self.competitors_label.config(text=matchup_text)
                self.output_text.insert(END, matchup_text + '\n')
                self.root.update()

                player1_series_wins = 0
                player2_series_wins = 0

                for round_num in range(len(player1.plays)):
                    play1 = player1.plays[round_num]
                    play2 = player2.plays[round_num]
                    result = self.determine_winner(play1, play2)

                    if result == "win":
                        player1.wins += 1
                        player2.losses += 1
                        player1_series_wins += 1
                        round_outcome = f"Round {round_num + 1}: {player1.name} ({play1}) vs {player2.name} ({play2}) - Winner: {player1.name}"
                    elif result == "lose":
                        player2.wins += 1
                        player1.losses += 1
                        player2_series_wins += 1
                        round_outcome = f"Round {round_num + 1}: {player1.name} ({play1}) vs {player2.name} ({play2}) - Winner: {player2.name}"
                    else:
                        player1.ties += 1
                        player2.ties += 1
                        round_outcome = f"Round {round_num + 1}: {player1.name} ({play1}) vs {player2.name} ({play2}) - Tie"

                    self.update_images(play1, play2)
                    self.outcome_label.config(text=round_outcome)
                    self.output_text.insert(END, round_outcome + '\n')
                    self.root.update()
                    sleep(1 - self.speed_scale.get())

                if player1_series_wins > player2_series_wins:
                    player1.series_wins += 1
                elif player2_series_wins > player1_series_wins:
                    player2.series_wins += 1

        self.print_final_results()

    def print_final_results(self):
        self.output_text.insert(END, "\nFinal Results:\n")
        for player in self.players:
            self.output_text.insert(END, str(player) + '\n')

        max_wins = max(player.wins for player in self.players)
        max_scores = max(player.wins + player.series_wins for player in self.players)
        max_series_wins = max(player.series_wins for player in self.players)

        top_winners = [player.name for player in self.players if player.wins == max_wins]
        top_scorers = [player.name for player in self.players if player.wins + player.series_wins == max_scores]
        top_series_winners = [player.name for player in self.players if player.series_wins == max_series_wins]

        self.output_text.insert(END, f"\nMost Wins: {', '.join(top_winners)}\n")
        self.output_text.insert(END, f"Highest Scores: {', '.join(top_scorers)}\n")
        self.output_text.insert(END, f"Most Series Wins: {', '.join(top_series_winners)}\n")
        self.output_text.config(state=DISABLED)

if __name__ == "__main__":
    tournament = RPSTournament()
    tournament.root.mainloop()