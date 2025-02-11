import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()  # Initialize the mixer
        self.playing = False
        self.current_track = None

    def load_music(self, file_path):
        """Loads an MP3 file."""
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            self.current_track = file_path

    def play_music(self):
        """Plays the loaded music."""
        if self.current_track:
            pygame.mixer.music.play()
            self.playing = True

    def pause_music(self):
        """Pauses the current song."""
        pygame.mixer.music.pause()
        self.playing = False

    def resume_music(self):
        """Resumes the paused song."""
        pygame.mixer.music.unpause()
        self.playing = True

    def stop_music(self):
        """Stops the current song."""
        pygame.mixer.music.stop()
        self.playing = False
