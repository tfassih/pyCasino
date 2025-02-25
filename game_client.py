import random
from nicegui import ui, app
from game_core import Pairs, Blackjack


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

###PAIRS GAME###

card_pair = []
matches = 0
m_list = []
counter = [0]
timer = {'value': 5}
wc = None
tc = None

@ui.page('/pairs')
def pairs():
    global matches
    global card_pair
    global timer
    global counter
    global wc
    global tc
    counter = [0]
    timer = {'value': 5}
    card_image = "/assets/img/back@2x.png"
    images = []
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Pairs').style('color: #FFFFFF; font-size: 20px;').classes('absolute-center;')
    matches_label = (ui.label(f'Matches: {matches}').style('color: #FFFFFF; font-size: 16px;')
                     .classes('absolute-center;'))
    timer_label = (ui.label().style('color: #FFFFFF; font-size: 16px;')
                   .bind_text_from(timer, 'value', lambda value: f'Time: {timer['value']}')
                   .classes('absolute-center;'))
    pairs_game = Pairs()
    selected_cards = pairs_game.selected_cards
    random.shuffle(selected_cards)

    def switch_image(card_button, card_img, c):
        global counter
        global card_pair
        global timer

        if counter[0] < 3:
            new_img = c[2] if card_img == "/assets/img/back@2x.png" else "/assets/img/back@2x.png"
            card_button.set_source(new_img)

            counter[0] += 1
            card_pair.append(c)
            if counter[0] > 1 and len(card_pair) > 1:
                check_pair_vals(card_pair[0], card_pair[1], matches_label)
                card_pair = []
            if counter[0] == 3:
                for img_btn in images:
                    img_btn.set_source("/assets/img/back@2x.png")
                card_pair = []
                counter[0] = 0

    tc = app.timer(1.0, lambda: timer.update(value=timer['value'] - 1))
    wc = app.timer(0.5, lambda: check_win_condition())

    with (ui.grid(columns=3, rows=4).style(f'height: 25%; width: 25%; column-gap: 10px; row-gap: 10px; ')
                                    .classes('col-gap-10, row-gap-10;')):
        for card in selected_cards:
            with ui.button().classes('row-span-1, h-[272px] ;'):
                img = ui.image(card_image)
                images.append(img)
                img.on('click', lambda ui_img=img, image=card_image, c=card: switch_image(ui_img, image, c))
                ui.update(img)

    def check_pair_vals(card1, card2, ml):
        global matches
        global m_list

        if card1 == card2 and [card1, card2] not in m_list:
            matches += 1
            m_list.append([card1, card2])
            ml.set_text(f'Matches: {matches}')
            check_win_condition()

def check_win_condition():
    global matches
    global timer
    if matches == 6 and timer['value'] > 0:
        for client in app.clients('/pairs'):
            with client:
                ui.navigate.to('/win_condition')
    elif timer['value'] < 1:
        for client in app.clients('/pairs'):
            with client:
                ui.navigate.to('/game_over')

@ui.page('/game_over')
def game_over():
    global wc
    global tc
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Game Over').style('color: #FFFFFF; font-size: 20px;').classes('absolute-center;')
    app.timer.cancel(wc)
    app.timer.cancel(tc)
    (ui.button('Restart', on_click=lambda: ui.navigate.to('/pairs')).style('font-size: 16px;')
                                                                         .classes('absolute-center;'))
    (ui.button('Main Menu', on_click=lambda: ui.navigate.to('/start_game'))
                                                             .style('font-size: 16px;')
                                                             .classes('absolute-center;'))

@ui.page('/win_condition')
def win_condition():
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('You Win!').style('color: #FFFFFF; font-size: 20px;').classes('absolute-center;')
    app.timer.cancel(wc)
    app.timer.cancel(tc)
    (ui.button('Restart', on_click=lambda: ui.navigate.to('/pairs')).style('font-size: 16px;')
                                                                         .classes('absolute-center;'))
    (ui.button('Main Menu', on_click=lambda: ui.navigate.to('/start_game')).style('font-size: 16px;')
                                                                                 .classes('absolute-center;'))

###OPTIONS MENU###

@ui.page('/options_menu')
def options_menu():
    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Options - Coming Soon - Currently Non-functional').style('color: #FFFFFF; font-size: 24px;')
    ui.separator().style('color: #FFFFFF; background-color: #FFFFFF').classes('absolute-center;')
    ui.label('Pairs Configuration').style('color: #FFFFFF; font-size: 20px;')
    with (ui.grid(columns=2).classes('absolute-center; items-start;')):
        ui.label('Number of cards').style('color: #FFFFFF; font-size: 16px;')
        ui.toggle([12, 16, 20, 24], value=16).style('color: #000000; background-color: #F0F0F0; width: 190px')

        ui.label('Timer Duration').style('color: #FFFFFF; font-size: 16px;')
        ui.toggle([15, 20, 25, 30, 35, 40, 45, 50, "Disabled"], value=40
                  ).style('color: #000000; background-color: #F0F0F0;')
    ui.separator().style('color: #FFFFFF; background-color: #FFFFFF').classes('absolute-center;')
    ui.label('Blackjack Configuration').style('color: #FFFFFF; font-size: 20px;')

###BLACKJACK###

@ui.page('/blackjack')
def blackjack():
    blackjack_game = Blackjack()
    player_score = blackjack_game.player_score
    dealer_score = blackjack_game.dealer_score
    bet = blackjack_game.bet
    blackjack_game.start_game()

    ui.query('body').style(f'background-color: #000000; min-height: 1200px;')
    ui.label('Blackjack - Coming Soon').style('color: #FFFFFF; font-size: 24px;').classes('absolute-center;')
    ui.separator().style('color: #FFFFFF; background-color: #FFFFFF').classes('absolute-center;')

    (ui.label(f'Player Score: {player_score}')
     .style('color: #FFFFFF; font-size: 20px;')
     .classes('absolute-center;')
     .bind_text_from(blackjack_game,
                    'player_score',
                     lambda value: f'Player Score: {value}'))

    (ui.label(f'Dealer Score: {dealer_score}').style('color: #FFFFFF; font-size: 20px;')
                                            .classes('absolute-center;')
                                            .bind_text_from(blackjack_game,
                                                            'dealer_score',
                                                            lambda value: f'Dealer Score: {value}'))

    (ui.label(f'Current Bet: $ {bet}').style('color: #FFFFFF; font-size: 20px;')
                    .bind_text_from(blackjack_game,
                                    'bet',
                                    lambda value: f'Bet: {value}'))

    with ui.row():
        for card in blackjack_game.player_hand:
            ui.image(card[2]).style('top:75; left:25; position:start;').classes('h-[323px], w-[272px];')

    def handle_hit():
        blackjack_game.player_hit = True
        blackjack_game.hit()
        ui.image(blackjack_game.player_hand[-1][2]).style('top:75; left:25; position:start;').classes('h-[323px], w-[272px];')
        blackjack_game.dealer_logic()

    with ui.column(wrap=False, align_items='center').style('width:15%; height:100%; position:end; left:95; top:20'):
        ui.button('Hit', on_click=lambda: handle_hit()).style('font-size: 16px;').classes('align-left;')
        ui.button('Stand', on_click=lambda: blackjack_game.stand()).style('font-size: 16px;').classes('align-left;').disable()
        ui.button("Restart", on_click=lambda: blackjack_game.reset_game()).style('font-size: 16px;').classes('align-left;').disable()
        ui.button("Main Menu", on_click=lambda: ui.navigate.to('/start_game')).style('font-size: 16px;').classes('align-left;')


    @ui.page('/blackjack_game_over')
    def blackjack_game_over():
        ui.query('body').style(f'background-color: #000000; min-height: 1200px;').classes('flex-start')
        (ui.label(f'Player Score: {blackjack_game.player_score}')
         .style('color: #FFFFFF; font-size: 20px;')
         .classes('absolute-center, flex-start;'))

        (ui.label(f'Dealer Score: {blackjack_game.dealer_score}').style('color: #FFFFFF; font-size: 20px;')
         .classes('absolute-center, flex-start;'))

        ui.label('BLACKJACK GAME OVER').style('color: #FFFFFF; font-size: 20px;').classes('absolute-center, flex-end;')
        blackjack_game.reset_game()
        ui.button("Main Menu", on_click=lambda: ui.navigate.to('/start_game')).style('font-size: 16px;').classes('align-left;')

    @ui.page('/blackjack_victory')
    def blackjack_victory():
        ui.query('body').style(f'background-color: #000000; min-height: 1200px;').classes('flex-start')
        (ui.label(f'Player Score: {blackjack_game.player_score}')
         .style('color: #FFFFFF; font-size: 20px;')
         .classes('absolute-center, flex-start;'))

        (ui.label(f'Dealer Score: {blackjack_game.dealer_score}').style('color: #FFFFFF; font-size: 20px;')
         .classes('absolute-center, flex-start;'))

        ui.label('BLACKJACK VICTORY').style('color: #FFFFFF; font-size: 20px;').classes('absolute-center, flex-end;')
        blackjack_game.reset_game()
        ui.button("Main Menu", on_click=lambda: ui.navigate.to('/start_game')).style('font-size: 16px;').classes('align-left;')

game_client = GameClient()
app.add_static_files('/assets/img', 'C:\\dev\\python\\pyCasino\\assets\\img')

ui.run()
