import itertools
import random

from nicegui import ui, app
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
card_pair = []
matches = 0
counter = [0]
@ui.page('/pairs')
def pairs():
    global matches
    global card_pair
    card_image = "/assets/img/back@2x.png"
    images = []
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Pairs - Coming Soon').style('color: #FFFFFF;')
    matches_label = ui.label(f'Matches: {matches}').style('color: #FFFFFF;')
    pairs_game = Pairs()
    selected_cards = pairs_game.selected_cards
    print(selected_cards)
    random.shuffle(selected_cards)
    global counter
    print("SLC: " + str(selected_cards))

    def switch_image(card_button, card_img, c):
        global counter
        global card_pair
        if counter[0] < 3:
            new_img = c[2] if card_img == "/assets/img/back@2x.png" else "/assets/img/back@2x.png"
            card_button.set_source(new_img)

            counter[0] += 1
            card_pair.append(c)
            if counter[0] > 1 and len(card_pair) > 1:
                print("check")
                check_pair_vals(card_pair[0], card_pair[1], matches_label)
                card_pair = []
            if counter[0] == 3:
                for img_btn in images:
                    img_btn.set_source("/assets/img/back@2x.png")
                card_pair = []
                counter[0] = 0

    with ui.grid(columns=3, rows=4).style(f'height: 25%; width: 25%; column-gap: 10px; row-gap: 10px; ').classes('col-gap-10, row-gap-10;'):
        for card in selected_cards:
            with ui.button().classes('row-span-1, h-[272px] ;'):
                img = ui.image(card_image)
                images.append(img)
                img.on('click', lambda ui_img=img, image=card_image, c=card: switch_image(ui_img, image, c))
                ui.update(img)

def check_pair_vals(card1, card2, ml):
    global matches
    print(card1)
    print(card2)
    if card1 == card2:
        matches += 1
        ml.set_text(f'Matches: {matches}')
        print("MATCHES: " + str(matches))








game_client = GameClient()
app.add_static_files('/assets/img', 'C:\\dev\\python\\pyCasino\\assets\\img')
ui.run()