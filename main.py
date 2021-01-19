from game import Game
from ui import UI
from turtle import Screen
from player import Player
from fleet import Fleet
from car import Car
from scoreboard import Scoreboard


if __name__ == "__main__":
    game = Game(
        UI(Screen()),
        Player,
        Fleet(Car),
        Scoreboard()
    )

    game.play()
