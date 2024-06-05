import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital bheem Music Player")
        self.root.geometry("300x300")
        
        self.filename = MusicPlayer

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)
        
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)
        
        self.open_button = tk.Button(self.root, text="Open", command=self.open_file)
        self.open_button.pack(pady=10)

    def play_music(self):
        if self.filename:
            pygame.mixer.music.unpause()
        else:
            messagebox.showerror("Error", "No file selected")

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()
    
    def open_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3")])
        if self.filename:
            pygame.mixer.music.load(self.filename)
            pygame.mixer.music.play(-1)

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
