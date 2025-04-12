import pygame

def load_sounds():
    sounds_dir = os.path.join("assets", "sounds")
    return {
        "turn": pygame.mixer.Sound(os.path.join(sounds_dir, "404151__lilmati__select-granted-01.wav")),
        "collect": pygame.mixer.Sound(os.path.join(sounds_dir, "124902__greencouch__beeps-231.wav")),
        "success": pygame.mixer.Sound(os.path.join(sounds_dir, "109662__grunz__success.wav")),
        "start": pygame.mixer.Sound(os.path.join(sounds_dir, "243020__plasterbrain__game-start.ogg")),
        "fail": pygame.mixer.Sound(os.path.join(sounds_dir, "253886__themusicalnomad__negative_beeps.wav")),
    }