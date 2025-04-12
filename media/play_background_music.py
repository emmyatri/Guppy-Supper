import pygame
def play_background_music():
    music_file = os.path.join("assets", "sounds", "Beach Party.mp3")
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)