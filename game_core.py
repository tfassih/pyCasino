import itertools
import tkinter as tk
from tkinter import ttk
import random
import numpy as np
import time


# class pyCasino:
#     def __init__(self, root : tk.Tk):
#         self.suites = ["Diamonds", "Hearts", "Spades", "Clubs"]
#         self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#         self.deck = list(itertools.product(self.suites, self.values))
#         self.win = False
#         self.timer = 40
#         self.restart = False
#         self.root = root
#
#         self.root.title("pyCasino")
#         self.root.geometry("1000x1200")
#         self.root.configure(background="green")
#
#         self.mainWindow = ttk.Frame(self.root, padding="10")
#         self.mainWindow.grid(row=0, column=0, sticky="nsew")
#
#         self.player_win_status_var = tk.StringVar()
#         self.timer_var = tk.StringVar()
#
#         self.player_win_status_var.set("WIN STATUS: " + str(self.win))
#         self.timer_var.set(str(self.timer))
#
#         self.player_win_label = tk.Label(self.mainWindow,
#                                          textvariable=self.player_win_status_var,
#                                          bg="green",
#                                          fg="white")
#         self.player_win_label.grid(row=2, column=4)
#
#         self.timer_label = tk.Label(self.mainWindow, textvariable=self.timer_var, bg="green", fg="white")
#         self.timer_label.grid(row=2, column=6)
#
#         self.start_game_button = tk.Button(self.mainWindow, text="START GAME", command = self.update_game_loop)
#         self.start_game_button.grid(row=2, column=8)
#
#         self.restart_game_button = tk.Button(self.mainWindow, text="RESTART GAME", command = self.restart_game)
#         self.restart_game_button.grid(row=2, column=10)
#
#     def update_game_loop(self):
#         if self.timer == "40" and self.restart_game_button.cget("state") == "disabled":
#             self.restart = False
#         if not self.restart:
#             self.restart = False
#             self.start_game_button.configure(state="disabled")
#             self.restart_game_button.configure(state="normal")
#             self.timer -= 1
#             self.timer_var.set(str(self.timer))
#             if self.restart_game_button.cget("state") == "normal":
#                 self.root.after_cancel(self.root.after(1000, self.update_game_loop))
#             else:
#                 self.timer_var.set("40")
#
#     def restart_game(self):
#         self.restart = True
#         self.start_game_button.configure(state="normal")
#         self.win = False
#         self.timer = 40
#         self.restart_game_button.configure(state="disabled")
#         self.player_win_status_var.set("WIN STATUS: " + str(self.win))
#         self.timer_var.set(str(self.timer))
#
#
# def start_core():
#     root = tk.Tk()
#     app = pyCasino(root)
#     root.mainloop()
#
#
#
# if __name__ == "__main__":
#     start_core()
class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.card_image = f"C:\\dev\\python\\pyCasino\\assets\\img\\{value}_of_{suite}.png"

    def get_suite(self):
        return self.suite

    def get_value(self):
        return self.value

    def get_card_image(self):
        return self.card_image


class Deck:
    def __init__(self):
        self.selected_cards = []
        self.suites = ["Diamonds", "Hearts", "Spades", "Clubs"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.card_images = [
            ###DIAMONDS###
            "C:\\dev\\python\\pyCasino\\assets\\img\\2_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\3_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\4_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\5_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\6_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\7_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\8_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\9_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\10_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\jack_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\queen_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\king_of_diamonds.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\ace_of_diamonds.png",
            ###HEARTS###
            "C:\\dev\\python\\pyCasino\\assets\\img\\2_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\3_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\4_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\5_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\6_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\7_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\8_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\9_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\10_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\jack_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\queen_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\king_of_hearts.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\ace_of_hearts.png",
            ###SPADES###
            "C:\\dev\\python\\pyCasino\\assets\\img\\2_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\3_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\4_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\5_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\6_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\7_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\8_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\9_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\10_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\jack_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\queen_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\king_of_spades.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\ace_of_spades.png",
            ###CLUBS###
            "C:\\dev\\python\\pyCasino\\assets\\img\\2_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\3_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\4_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\5_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\6_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\7_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\8_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\9_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\10_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\jack_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\queen_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\king_of_clubs.png",
            "C:\\dev\\python\\pyCasino\\assets\\img\\ace_of_clubs.png",
        ]
        self.deck = []
        for suite in self.suites:
            for value in self.values:
                card = Card(suite, value)
                self.deck.append([card.suite, card.value, card.card_image])
        random.shuffle(self.deck)

    def reset_deck(self):
        self.deck = []
        for suite in self.suites:
            for value in self.values:
                card = Card(suite, value)
                self.deck.append([card.suite, card.value, card.card_image])
        self.shuffle_deck()
        return self.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)
        print(list(self.deck))

    def deal_cards(self):
        card_list = []
        counter = 0
        num_cards = 0
        matches = 0
        matching_card_index = 0
        match_list = []

        for i in range(len(self.deck) - 1):
            if matches == 6:
                break
            for j in range(i+1, len(self.deck) - 1):
                if self.deck[i][1] == self.deck[j][1]:
                    for x in match_list:
                        if str(self.deck[i][1]) == str(x[1]):
                            return
                    match_list.append([self.deck[i][0], self.deck[i][1], self.deck[i][2]])
                    match_list.append([self.deck[j][0], self.deck[j][1], self.deck[j][2]])
                    num_cards += 2
                    matches += 1
                    if matches == 6:
                        break
                    print(len(self.deck))
                    for k in range(len(self.deck) - 1):
                        if k + 1 > len(self.deck):
                            break
                        print(k)
                        if self.deck[k][1] == self.deck[i][1] and len(self.deck) - k > 0:
                            self.deck.pop(self.deck.index(self.deck[k]))
                    break
        checker = 0
        for i in range(len(match_list) - 1):
            for j in range(i + 1, len(match_list) - 1):
                if match_list[i][1] == match_list[j][1]:
                    checker += 1
                if checker > 2:
                    break
        if checker > 2:
            self.deck = self.reset_deck()
            self.deal_cards()
        return match_list

class Pairs:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.selected_cards = self.deck.selected_cards
