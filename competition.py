from tkinter import *
import open_file as of


class RPSPlayer:
    def __init__(self, data):
        self.name = data['name']
        self.wins = data['wins']
        self.losses = data['losses']

    def __str__(self):
        return f"{self.name} - Wins: {self.wins}, Losses: {self.losses}"

class RPSTournament:
    def __init__(self):
        self.players = []
        self.output_text = None

    def open_window(self):
        window = Tk()
        window.title("RPS Tournament")

        img = PhotoImage(file="resources/bgbgbg.png")
        background_label = Label(window, image=img)
        background_label.place(relwidth=1, relheight=1)

        top_frame = Frame(window, bd=2, relief=SOLID, bg='grey')
        top_frame.pack(padx=20, pady=10, fill=X)

        Button(top_frame, text="Select Folder", command=self.browse_directory).pack(padx=5, pady=5)
        Button(top_frame, text="Select File", command=self.browse_file).pack(padx=5, pady=5)
        Label(top_frame, text="Speed").pack(padx=5, pady=5)
        Scale(top_frame, from_=0, to=1, resolution=0.05, orient=HORIZONTAL).pack(padx=5, pady=5)
        Button(top_frame, text="Run Tournament", command=self.run_tournament).pack(padx=5, pady=5)

        self.output_text = Text(window, height=20, wrap=WORD, width=60, state=DISABLED)
        self.output_text.pack(padx=20, pady=20, expand=True, fill=BOTH) 

        scrollbar = Scrollbar(window, command=self.output_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.output_text.config(yscrollcommand=scrollbar.set)

        background_label.image = img

        window.mainloop()

    def browse_file(self):
        file_paths = of.File(self.output_text).browse_files()
        self.load_players_from_files(file_paths)
    def browse_directory(self):
        file_paths = of.File(self.output_text).browse_directory()
        self.load_players_from_files(file_paths)

    def load_players_from_files(self, files):
        self.players.clear()

        for file in files:
            player_data = self.load_player_data_from_file(file)
            new_player = RPSPlayer(player_data)
            self.players.append(new_player)

        self.print_all_players()

    def load_player_data_from_file(self, file):
        return {'name': 'Player Name', 'wins': 0, 'losses': 0}

    def print_all_players(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)

        for player in self.players:
            print(player)
            self.output_text.insert(END, str(player) + '\n')

        self.output_text.config(state=DISABLED)

    def run_tournament(self):
        pass

if __name__ == "__main__":
    tournament = RPSTournament()
    tournament.open_window()
