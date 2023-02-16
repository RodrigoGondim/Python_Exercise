'''Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3'''

# Coloque o 'Arquivo.mp3' na mesma pasta do seu projeto
import pygame

pygame.init()
pygame.mixer.music.load('Arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()

