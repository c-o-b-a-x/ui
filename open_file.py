import os
import tkinter as tk
from tkinter import filedialog

class File:
    def __init__(self, output_text_widget):
        self.output_text = output_text_widget

    def browse_directory(self):
        path = filedialog.askdirectory(title="Select Folder with .rps files")
        
        self.output_text.config(state=tk.NORMAL)  

        self.output_text.delete(1.0, tk.END) 

        if os.path.isdir(path):
            self.output_text.insert(tk.END, "Processing files...\n")
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name)
                if os.path.isfile(file_path) and file_name.lower().endswith('.rps'):
                    self.output_text.insert(tk.END, f"File: {file_name}\n")

                    with open(file_path, "r") as file:
                        file_contents = file.read()
                        self.output_text.insert(tk.END, f"Contents:\n{file_contents}\n")
                        self.output_text.insert(tk.END, "=" * 40 + "\n")  



            with open("rps.log", "a") as log_file:
                log_file.write(self.output_text.get(1.0, tk.END))  

        else:
            self.output_text.insert(tk.END, f"The provided path is not a valid directory: {path}\n")

        self.output_text.config(state=tk.DISABLED)  


    def browse_files(self):
            file_path = filedialog.askopenfilename(
                title="Select  File",
                filetypes=[("Multi Rock, Paper, Scissors (.mrps)", "*.mrps"),("Rock Paper Scisorrs (.RPS)","*.rps")]
            )
    
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete(1.0, tk.END)
    
            if file_path and os.path.isfile(file_path) and file_path.lower().endswith('.mrps'):
                self.output_text.insert(tk.END, "Processing file...\n")
                self.output_text.insert(tk.END, f"File: {os.path.basename(file_path)}\n")
    
                with open(file_path, "r") as file:
                    file_contents = file.read()
                    self.output_text.insert(tk.END, f"Contents:\n{file_contents}\n")
    
                players = file_contents.splitlines()
                self.output_text.insert(tk.END, "\nPlayers List:\n")
                for player in players:
                    self.output_text.insert(tk.END, f"{player}\n")
                self.output_text.insert(tk.END, "=" * 40 + "\n")
    
                with open("rps.log", "a") as log_file:
                    log_file.write(self.output_text.get(1.0, tk.END))
    
            self.output_text.config(state=tk.DISABLED)