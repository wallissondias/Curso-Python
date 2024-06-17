import pygame
pygame.init()
pygame.mixer.music.load('music.mp3') #carregar arquivo
pygame.mixer.music.play() #reproduzir audio
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
