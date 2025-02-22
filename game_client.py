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

class Pairs_Card_Toggle(ui.button):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._state = False
        self.on('click', self.toggle)

    def toggle(self) -> None:
        self._state = not self._state
        self.update()

    def update(self) -> None:
        self.props(f'icon={"/assets/img/back@2x.png" if self._state else "card_image"}')
        super().update()


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

    card_image = "/assets/img/back@2x.png"

    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Pairs - Coming Soon').style('color: #FFFFFF;')
    pairs_game = Pairs()
    selected_cards = pairs_game.selected_cards
    print(selected_cards)
    random.shuffle(selected_cards)

    print("SLC: " + str(selected_cards))

    def switch_image(c_button, image, c):
        if image == "/assets/img/back@2x.png":
            c_button.set_source(c[2])
            print(c[2])
        else:
            c_button.set_source("/assets/img/back@2x.png")
        ui.update(c_button)
    with ui.grid(columns=3, rows=4).style(f'height: 25%; width: 25%; column-gap: 10px; row-gap: 10px; ').classes('col-gap-10, row-gap-10;'):
        for card in selected_cards:
            with ui.button().classes('row-span-1, h-[272px] ;'):
                img = ui.image(card_image)
                img.on('click', lambda ui_img=img, image=card_image, c=card: switch_image(ui_img, image, c))







game_client = GameClient()
app.add_static_files('/assets/img', 'C:\\dev\\python\\pyCasino\\assets\\img')
ui.run()