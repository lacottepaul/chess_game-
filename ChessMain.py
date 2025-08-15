"""
Main file, this handles the interaction with user and the dfisplay of the game 'GameState'. 
"""
import pygame as p 
from Chess import ChessEngine 

WIDTH = HEIGHT = 512 #size of pieces on the board 
DIMENSION = 8 #of the board 
SQ_SIZE = HEIGHT // DIMENSION 
MAX_FPS = 15 
IMAGES = {}

''' 
loading images
'''

def loadImages():
    pieces = ["bR","bN","bB","bQ","bK","wR","wN","ww","wQ","wK","wp","bp"]
    for piece in pieces: 
         IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+"wp.png"),(SQ_SIZE,SQ_SIZE))