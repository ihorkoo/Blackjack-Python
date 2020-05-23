import random

class Players:
    def __init__(self):
        self.name = self._input_name()
        self.score = 0

    def _input_name(self):
        name = input("Введіть ім'я гравця:")
        return name

    def reset_player(self):
        self.score = 0



class Cards:
    """Клас реалізує колоду карт"""

    def __init__(self):
        self.cards = self._create_cards()


    def _create_cards(self):
        """Створення колоди кард
        :return: dict, де key - назва карти, value - кількість очок"""

        cards = {'6' : 6, '7' : 7, '8' : 7, '9' : 9, '10' : 10,
                 'J' : 2, 'D' : 3, 'K' : 4, 'A' : 11}
        suit = ['♠' ,'♣', '♥ ', '♦']

        dict_with_all_cards = {}

        for k,v in cards.items():
            for i in suit:
                dict_with_all_cards[k+i] = v

        return dict_with_all_cards


    def reset_cards(self):
        """Обновити колоду карт"""
        self.cards = self._create_cards()


    def take_card(self):
        """Вибрати випадкову карту та забрати її з колоди.
        :return: tupl:
                :random_card - назва карти
                :point - кількість очок карти
        """
        random_card = random.choice(list(self.cards))
        point = self.cards[random_card]
        del self.cards[random_card]
        return (random_card, point)



class Game:
    """Клас, що відповідає за весь механізм гри"""

    def __init__(self, player1, player2, cards):
        """players - словник із гравцями
        Значення в словнику 1 означає, що гравець активний, тобто готовий брати нові карти
        Значення 0 - гравець завершив хід та очікує інших гравців"""

        self.cards = cards
        self.players = {player1 : 1, player2 : 1}


    def active_players(self):
        """Список гравців, що продовують грати (активні)"""

        active = [k  for k, v in self.players.items() if v == 1]
        return active


    def move(self, player):
        """Хід гравця.
        Гравець витягує нову карту або відмовляється продовжувати хід"""

        print(f"{player.name} - твій хід")
        print(f"У тебе {player.score}")
        q = input('Будеш брати карту? (y/n)')
        if q == 'y':
            card, point = self.cards.take_card()
            print(f"Ти витягнув карту {card}")
            player.score += point

        else:
            self.players[player] = 0

        print("-------******-------")
        print()


    def _reset_round(self):
        """Обновляємо колоду та видаляємо результати гравців"""

        self.cards.reset_cards()
        for player in self.players:
            player.reset_player()


    def win(self):
        """Визначаємо переможця у грі """

        player1, player2 = self.players.keys()

        if player1.score == player2.score:
            print("Нічия")
        elif  player1.score > 21 and  player2.score <= 21:
            print(f"Переміг гравець {player2.name} {player2.score}")
        elif player2.score > 21 and  player1.score <= 21:
            print(f"Переміг гравець {player1.name} {player1.score}")
        elif player2.score < player1.score <= 21:
            print(f"Переміг гравець {player1.name} {player1.score}")
        elif player1.score < player2.score <= 21:
            print(f"Переміг гравець {player2.name} {player2.score}")

        self._reset_round()


    def round_game(self):
        """Запуск одного раунда гри"""

        while self.active_players():
            for player in self.active_players():
                self.move(player)
        self.win()


if __name__ == "__main__":
    pl1 = Players()
    pl2 = Players()
    cards = Cards()
    game = Game(pl1, pl2, cards)
    game.round_game()
