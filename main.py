from game import Game
from gui import GUI
from turtle import Screen
from player import Player
from fleet import Fleet
from car import Car
from scoreboard import Scoreboard


if __name__ == "__main__":
    game = Game(
        GUI(Screen()),
        Player,
        Fleet(8, Car),
        Scoreboard()
    )

    game.play()
