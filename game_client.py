import itertools
import random

from nicegui import ui
from nicegui.binding import bindings

from game_core import Pairs


class GameClient:
    def __init__(self):
        ### Style initialization
        ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
        with ui.element('div').style('width: 100%; '
                                     'height: 100%; '
                                     'position: absolute; '
                                     'margin: 0;'
                                     ):
            with ui.column(align_items='center').style('width: 50%; '
                                                       'height: 100%; '
                                                       'position: absolute; '
                                                       'margin: 0;'
                                                       ):
                ui.button('START GAME', on_click=lambda: ui.navigate.to('/start_game')).style('width: 10%; '
                                              'background-color: #000000; '
                                              'color: #FFFFFF; '
                                              'top: 50%; '
                                              'left: 50%;'
                                              'transform: translate(-50%, -50%);'
                                              )
                ui.button('OPTIONS', on_click=lambda: ui.navigate.to('/options_menu')).style('width: 10%; '
                                           'background-color: #000000; '
                                           'color: #FFFFFF; '
                                           'top: 50%; '
                                           'left: 50%;'
                                           'transform: translate(-50%, -50%);'
                                           )


@ui.page('/start_game')
def start_game():
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    with ui.element('div').style('width: 100%; '
                                 'height: 100%; '
                                 'position: absolute; '
                                 'margin: 0;'
                                 ):
        with ui.column(align_items='center').style('width: 50%; '
                                                   'height: 100%; '
                                                   'position: absolute; '
                                                   'margin: 0;'
                                                   ):
            ui.button('BLACKJACK',
                      on_click=lambda: ui.navigate.to('/blackjack')).style('width: 10%; '
                                                                          'background-color: #000000; '
                                                                          'color: #FFFFFF; '
                                                                          'top: 50%; '
                                                                          'left: 50%;'
                                                                          'transform: translate(-50%, -50%);'
                                                                          )
            ui.button('PAIRS',
                      on_click=lambda: ui.navigate.to('/pairs')).style('width: 10%; '
                                                                       'background-color: #000000; '
                                                                       'color: #FFFFFF; '
                                                                       'top: 50%; '
                                                                       'left: 50%;'
                                                                       'transform: translate(-50%, -50%);'
                                                                       )

@ui.page('/options_menu')
def options_menu():
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Options - Coming Soon').style('color: #FFFFFF;')

@ui.page('/blackjack')
def blackjack():
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Blackjack - Coming Soon').style('color: #FFFFFF;')

@ui.page('/pairs')
def pairs():
    card_image = "C:\\dev\\python\\pyCasino\\img\\back@2x.png"
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Pairs - Coming Soon').style('color: #FFFFFF;')
    pairs_game = Pairs()
    selected_cards = pairs_game.selected_cards
    print(selected_cards)
    random.shuffle(selected_cards)

    print("SLC: " + str(selected_cards))
    with ui.grid(columns=3, rows=4).style(f'height: 25%; width: 25%;').classes('absolute-center, '):
        for card in selected_cards:
            with ui.card().tight():
                img = ui.image(card_image)
                img.on('click', switch_image(card_image, card, img))

def switch_image(card_image, card, img):
    if "back" in card_image:
        card_image = str(card[2])
        img.set_source(card_image)
        ui.update()
    else:
        card_image = "C:\\dev\\python\\pyCasino\\img\\back@2x.png"
        img.set_source(card_image)
        ui.update()

game_client = GameClient()
ui.run()