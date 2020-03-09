# Black Jack Game!
# Black Jack is a game with 52 cards in a deck
import random
# What will we need
# Something to represent the Cards
# Make it printable/ visable
# represent the suits and ranks/ Card and value of that card


class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '[ ' + self.rank + ' of ' + self.suit + ' ]'

# Test below
# x = Card('Diamond','10')
# print(x)

    # Something to represent the Deck
        # 52 cards in the deck
        # Dealing cards
        # Subtracting the card once dealt
        # Shuffle the 52 cards so its random/Random module


class Deck:

    def __init__(self):
        self.deck = [Card(suits, ranks).__str__() for suits in ['Clubs', 'Spades', 'Hearts', 'Diamonds']
                     for ranks in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

# Test
# x = Deck()
# x.shuffle()
# print(x.deal())

    # Something to represent the Hand/the actual players cards not just the deck
        # Needs to have a value/something to check the value of the cards in the hand
        # Needs t


class Hand:

    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def hit(self, card):
        self.cards.append(card)

    def calc_hand(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            x = card.split(' ')
            if x[1].isnumeric():
                self.value += int(x[1])
            else:
                if x[1] == 'A':
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10  # This is for JQK
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):  # Method to keep it nice and neat, making a self.calc_hand() to run a method through another method and give the output
        self.calc_hand()
        return self.value

    def display(self):
        if self.dealer:
            print('Dealers :', '[?]', self.cards[1])
            print('')

        else:
            print('Players :', self.cards)
            print("Value:", self.get_value())
            print('')

    def full_display(self):
        if self.dealer:
            print('Dealers :', self.cards)
            print('Value :', self.get_value())
            print('')

        else:
            print('Players :', self.cards)
            print('Value :', self.get_value())
            print('')


class Bank:  # allowing for the player to place a bet
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def make_bet(self):
        self.bet = 0#Setting the self.bet to 0 everytime this method is called so that your bet does't keep adding on top of each other over and over again 
        try:
            bet1 = int(input('How much do you want to bet? '))

            while bet1 > self.total:
                bet1 = int(input(f"You only have {self.total} amount"))

            self.bet += bet1

        except:
            # This will loop back to the method calling upon itself, so that no str to int errors occur :D
            return self.make_bet()

    def bet_win(self):
        self.total += self.bet

    def bet_lose(self):
        self.total -= self.bet


# Bank Check!
# player_bank = Bank()
# player_bank.make_bet()
# player_bank.bet_win()
# print('Your total: ', player_bank.total)
# print('Your bet: ', player_bank.bet)


class Game:

    def __init__(self):
        pass

    def play(self):

        playing = True
        self.player_bank = Bank()  # Moved it here so that it won't constantly reset its bank value once the game starts, so the player can keep betting more and more till they run out of money, aka you win more you bet more
        while playing:

            self.deck = Deck()  # Creating the deck
            self.deck.shuffle()  # shuffling the deck

            self.player1 = Hand()

            # initiates the hidding of the hand
            self.dealer1 = Hand(dealer=True)

            self.dealer1.hit(self.deck.deal())
            self.player1.hit(self.deck.deal())
            self.dealer1.hit(self.deck.deal())
            self.player1.hit(self.deck.deal())

            choice = input('Do you want to play? y or n').lower()

            if choice == 'y':
                game_on = True

            else:
                break

            while game_on:

                name = input('What is your name?')
                self.player_bank.make_bet()

                print('\n'*100)
                print(f"{name}'s Hand: ")
                self.player1.display()
                self.dealer1.display()

                hit_or_stand = 0

                while self.player1.value < 21:
                    hit_or_stand = input(
                        'Do you want to hit or stand h or s').lower()
                    print('\n'*100)
                    if hit_or_stand == 'h':
                        print('\n'*100)
                        self.player1.hit(self.deck.deal())
                        print(f"{name}'s Hand: ")
                        self.player1.full_display()
                        self.dealer1.display()
                        print('')

                    while hit_or_stand not in ['h', 's', 'hit', 'stand']:
                        hit_or_stand = input(
                            'Do you want to hit or stand h or s').lower()
                        print('')

                    if hit_or_stand == 's' and self.dealer1.value < 17:
                        print('\n'*100)
                        self.dealer1.hit(self.deck.deal())
                        self.dealer1.display()
                        print('')
                        break

            # Checking to see who won?
                if self.player1.value > 21:
                    print('\n'*100)
                    print(f'{name} has busted!')
                    self.player1.full_display()
                    self.dealer1.full_display()
                    self.player_bank.bet_lose()
                    print(f'Your bet : {self.player_bank.bet}')
                    print('Your total: ', self.player_bank.total)
                    print('\n')
                    game_on = False

                if self.dealer1.value > 21:
                    print('\n'*100)
                    print(f'Dealer has busted! {name} has won!')
                    self.player1.full_display()
                    self.dealer1.full_display()
                    self.player_bank.bet_win()
                    print(f'Your bet : {self.player_bank.bet}')
                    print('Your total: ', self.player_bank.total)
                    print('\n')
                    game_on = False

                if self.player1.value == 21:
                    print('\n'*100)
                    print(f'Black Jack {name} win!')
                    self.player1.full_display()
                    self.dealer1.full_display()
                    self.player_bank.bet_win()
                    print(f'Your bet : {self.player_bank.bet}')
                    print('Your total: ', self.player_bank.total)
                    print('\n')
                    game_on = False

                if self.dealer1.value == 21:
                    print('\n'*100)
                    print(f'Dealer has Black Jack! {name} lose!')
                    self.player1.full_display()
                    self.dealer1.full_display()
                    self.player_bank.bet_lose()
                    print(f'Your bet : {self.player_bank.bet}')
                    print('Your total: ', self.player_bank.total)
                    print('\n')
                    game_on = False

                # Error occured when dealer was 21 and it said that player had won, the self.dealer1.value < 21 makes sure that it doesn't happen has been FIXED! by changing some values in the class
                if self.player1.value > self.dealer1.value and self.player1.value < 21 and self.dealer1.value < 21:
                    print('\n'*100)
                    print(f'{name} has won! Great Job!')
                    self.player1.full_display()
                    self.dealer1.full_display()
                    self.player_bank.bet_win()
                    print(f'Your bet : {self.player_bank.bet}')
                    print('Your total: ', self.player_bank.total)
                    print('\n')
                    game_on = False

                if self.dealer1.value > self.player1.value and self.dealer1.value < 21 and self.player1.value < 21:  # Error occured when player was 21
                    print('\n'*100)
                    print(f'Dealer has won! {name} lose!')
                    self.player1.full_display()
                    self.dealer1.full_display()
                    self.player_bank.bet_lose()
                    print(f'Your bet : {self.player_bank.bet}')
                    print('Your total: ', self.player_bank.total)
                    print('\n')
                    game_on = False


if __name__ == '__main__':
    g = Game()  # initiates the game
    g.play()  # starts the game!
