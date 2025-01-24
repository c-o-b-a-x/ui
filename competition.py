from tkinter import *
from tkinter import filedialog
from time import sleep
import open_file as of
from RPSPlayer import RPSPlayer

class RPSTournament:
    def __init__(self):
        self.players = []
        self.output_text = None
        self.root = Tk()
        self.add_images()
        self.add_info()
        self.setup_ui()

    def add_images(self):
        self.images = {
            "rock": PhotoImage(file="resources/rock100.png"),
            "paper": PhotoImage(file="resources/paper100.png"),
            "scissors": PhotoImage(file="resources/scissors100.png"),
            "question": PhotoImage(file="resources/tbd100.png")
        }
        self.player1_img_label = Label(self.root, image=self.images["question"])
        self.vs_label = Label(self.root, text="VS")
        self.player2_img_label = Label(self.root, image=self.images["question"])
        
        self.player1_img_label.grid(row=0, column=0)
        self.vs_label.grid(row=0, column=1)
        self.player2_img_label.grid(row=0, column=2)

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
            print(player)
            self.output_text.insert(END, str(player) + '\n')

        self.output_text.config(state=DISABLED)

    def run_tournament(self):
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]
                self.competitors_label.config(text=f"{player1.name} vs {player2.name}")
                print(f"{player1.name} vs {player2.name}")
                self.root.update()
                sleep(self.speed_scale.get())
                self.player1_img_label.config(image=self.images["question"])
                self.player2_img_label.config(image=self.images["question"])

if __name__ == "__main__":
    tournament = RPSTournament()
    tournament.root.mainloop()