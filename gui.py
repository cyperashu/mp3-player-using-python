import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Clone")
        self.root.geometry("400x300")
        self.root.configure(bg="#121212")

        # Song Path
        self.song_path = None

        # Progress Bar
        self.progress = tk.Scale(root, from_=0, to=100, orient="horizontal", length=350, bg="#333", fg="white")
        self.progress.pack(pady=10)

        # Button Frame
        button_frame = tk.Frame(root, bg="#121212")
        button_frame.pack()

        # Buttons (Play, Pause, Resume, Stop)
        self.play_button = tk.Button(button_frame, text="▶️", command=self.play_music, width=6)
        self.pause_button = tk.Button(button_frame, text="⏸️", command=self.pause_music, width=6)
        self.resume_button = tk.Button(button_frame, text="⏯️", command=self.resume_music, width=6)
        self.stop_button = tk.Button(button_frame, text="⏹️", command=self.stop_music, width=6)

        # Arrange Buttons in One Line
        self.play_button.grid(row=0, column=0, padx=5, pady=10)
        self.pause_button.grid(row=0, column=1, padx=5, pady=10)
        self.resume_button.grid(row=0, column=2, padx=5, pady=10)
        self.stop_button.grid(row=0, column=3, padx=5, pady=10)

        # Open File Button
        self.open_file_button = tk.Button(root, text="📂 Open Music File", command=self.load_song)
        self.open_file_button.pack(pady=10)

        # Song Label
        self.song_label = tk.Label(root, text="No song selected", fg="white", bg="#121212")
        self.song_label.pack()

    def load_song(self):
        self.song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if self.song_path:
            self.song_label.config(text=self.song_path.split("/")[-1])

    def play_music(self):
        if self.song_path:
            pygame.mixer.music.load(self.song_path)
            pygame.mixer.music.play()
            self.update_progress()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.progress.set(0)

    def update_progress(self):
        if pygame.mixer.music.get_busy():
            self.progress.set(self.progress.get() + 1)
            self.root.after(1000, self.update_progress)  # Update every second

# Run the Application
root = tk.Tk()
app = MusicApp(root)
root.mainloop()
