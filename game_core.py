import random


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
            "/assets/img/2_of_diamonds.png",
            "/assets/img/3_of_diamonds.png",
            "/assets/img/4_of_diamonds.png",
            "/assets/img/5_of_diamonds.png",
            "/assets/img/6_of_diamonds.png",
            "/assets/img/7_of_diamonds.png",
            "/assets/img/8_of_diamonds.png",
            "/assets/img/9_of_diamonds.png",
            "/assets/img/10_of_diamonds.png",
            "/assets/img/jack_of_diamonds.png",
            "/assets/img/queen_of_diamonds.png",
            "/assets/img/king_of_diamonds.png",
            "/assets/img/ace_of_diamonds.png",
            ###HEARTS###
            "/assets/img/2_of_hearts.png",
            "/assets/img/3_of_hearts.png",
            "/assets/img/4_of_hearts.png",
            "/assets/img/5_of_hearts.png",
            "/assets/img/6_of_hearts.png",
            "/assets/img/7_of_hearts.png",
            "/assets/img/8_of_hearts.png",
            "/assets/img/9_of_hearts.png",
            "/assets/img/10_of_hearts.png",
            "/assets/img/jack_of_hearts.png",
            "/assets/img/queen_of_hearts.png",
            "/assets/img/king_of_hearts.png",
            "/assets/img/ace_of_hearts.png",
            ###SPADES###
            "/assets/img/2_of_spades.png",
            "/assets/img/3_of_spades.png",
            "/assets/img/4_of_spades.png",
            "/assets/img/5_of_spades.png",
            "/assets/img/6_of_spades.png",
            "/assets/img/7_of_spades.png",
            "/assets/img/8_of_spades.png",
            "/assets/img/9_of_spades.png",
            "/assets/img/10_of_spades.png",
            "/assets/img/jack_of_spades.png",
            "/assets/img/queen_of_spades.png",
            "/assets/img/king_of_spades.png",
            "/assets/img/ace_of_spades.png",
            ###CLUBS###
            "/assets/img/2_of_clubs.png",
            "/assets/img/3_of_clubs.png",
            "/assets/img/4_of_clubs.png",
            "/assets/img/5_of_clubs.png",
            "/assets/img/6_of_clubs.png",
            "/assets/img/7_of_clubs.png",
            "/assets/img/8_of_clubs.png",
            "/assets/img/9_of_clubs.png",
            "/assets/img/10_of_clubs.png",
            "/assets/img/jack_of_clubs.png",
            "/assets/img/queen_of_clubs.png",
            "/assets/img/king_of_clubs.png",
            "/assets/img/ace_of_clubs.png",
        ]
        self.deck = []
        for suite in self.suites:
            for value in self.values:
                card = Card(suite, value)
                self.deck.append([card.suite, card.value, card.card_image])

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
        num_cards = 52
        matches = 0
        match_list = []

        for i in range(len(self.deck) - 1):
            if matches == 6:
                break

            for j in range(i+1 if i + 1 < len(self.deck) else len(self.deck)):
                if self.deck[i][1] == self.deck[j][1] and [k[1] for k in match_list].count(self.deck[i][1]) < 1 and num_cards >= 4:
                    match_list.append([self.deck[i][0], self.deck[i][1], self.deck[i][2]])
                    match_list.append([self.deck[j][0], self.deck[j][1], self.deck[j][2]])
                    matches += 1
                    for x in self.deck:
                        if x[1] == self.deck[i][1]:
                            self.deck.pop(self.deck.index(x))
                    num_cards -= 4
        print(match_list)

        self.selected_cards = match_list
        return match_list


class Pairs:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.selected_cards = self.deck.deal_cards()


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.bet = []
        self.player_score = 0
        self.dealer_score = 0
        self.player_bust = False
        self.dealer_bust = False
        self.player_blackjack = False
        self.dealer_blackjack = False
        self.player_stand = False
        self.dealer_stand = False
        self.player_hit = False
        self.dealer_hit = False
        self.player_split = False
        self.dealer_split = False
        self.player_split_hand = []
        self.dealer_split_hand = []
        self.player_split_score = 0
        self.dealer_split_score = 0
        self.player_split_bust = False
        self.dealer_split_bust = False

    def hit(self):
        if self.dealer_hit:
            pass
        if self.player_hit:
            pass

    def stand(self):
        if self.dealer_stand:
            pass
        if self.player_stand:
            pass

    def split(self):
        if self.dealer_split:
            pass
        if self.player_split:
            pass

    def update_score(self, score):
        if self.dealer_score:
            self.dealer_score += score
        if self.player_score:
            self.player_score += score

    def update_bust(self):
        if self.dealer_bust or self.dealer_split_bust:
            pass
        if self.player_bust or self.player_split_bust:
            pass

    def update_blackjack(self):
        if self.dealer_blackjack:
            pass
        if self.player_blackjack:
            pass

    def reset_game(self):
        self.player_hand = []
        self.dealer_hand = []
        self.bet = []
        self.player_score = 0
        self.dealer_score = 0
        self.player_bust = False
        self.dealer_bust = False

    def update_bet(self, bet):
        self.bet = bet

