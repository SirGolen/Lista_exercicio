#Faça um programa em python que abra e reproduza o audio de um arquivo mp3
import pygame
# Inicializa o módulo Pygame
pygame.mixer.init()
# Abre o arquivo mp3
pygame.mixer.music.load('GatoDeSchrodinger.mp3')
# Inicia a música
pygame.mixer.music.play()

while pygame .mixer.music.get_busy():
    continue

pygame.quit()
