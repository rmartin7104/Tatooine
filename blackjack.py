'''
_ _ _ _ _      __  __                        _ _        _ _                       __      __
|  _ _ _  |    |__||  |                      |   \      /   |                     |  |    |__|
|  |   |  |        |  |                      |    \    /    |                  _ _|  |_ _  
|  |___|  |     __ |  |  _ _ _ _ _       _ _ |     \  /     |  _ _ _ _   __   |_ _    _ _| __  __
|  _ _ _  |    |  ||  | /  _ _  \  \    /  / |  |\  \/  /|  | /  _ _   \|  \_ _ _ |  |    |  ||  \ _ _ _ _
|  |    \  \   |  ||  |/  /_ _\  \  \_ /  /  |  | \    / |  ||  |   |  ||   _ _  ||  |    |  ||   _ _ _   \
|  |     \  \  |  ||  ||_ _ _ _ _|\_ _   /   |  |  \__/  |  ||  |   |  ||  |   |_/|  |    |  ||  |     |  |
|  |      \  \ |  ||  || | _ _ _ _   /  /    |  |        |  ||  |_ _|  ||  |      |  |    |  ||  |     |  |
|__|       \__\|__||__|\ ________/  /  /     |__|        |__||_____/|__||__|      |__|    |__||__|     |__|
                                   /__/
This is a simple blackjack game written in Python3
'''

from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class card():
    '''This creates a single instance of a card'''
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class deck():
    '''This creates a complete deck of cards'''
    def __init__(self):
        self.all_cards = [card(rank,suit) for suit in suits for rank in ranks if True]
    def shuffle_deck(self):
        shuffle(self.all_cards)
    def remove_card(self):
        outcard = self.all_cards.pop()
        return outcard

class player():
    '''This class defines a player with a name and chip count'''
    def __init__(self,name):
        self.name = name
        self.chips = 100
        self.hand = []
        self.pile = []
    def __str__(self):
        return f'{self.name}'
    def remove_card(self):
        return self.pile.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.pile.extend(new_cards)
        else:
            self.pile.append(new_cards)

def check_bust(cards):
    if cards > 21:
        print("You went bust!")
        player1.chips -= bet_amt
        return False
    else:
        return True

def check_win(hand1,hand2):
    if hand2 > 21:
        print("Dealer Busted Player Wins!")
        player1.chips += bet_amt
        return False
    elif hand1 > hand2:
        player1.chips += bet_amt
        print("Player Wins")
        return False
    elif hand1 < hand2:
        player1.chips -= bet_amt
        print("House wins")
        return False
    else:
        print("Tie")
        return False

def deal_hand():
    handdeck = deck()
    hand1 = []
    hand2 = []
    shuffle(handdeck.all_cards)
    hand1.append(handdeck.remove_card())
    hand2.append(handdeck.remove_card())
    hand1.append(handdeck.remove_card())
    hand2.append(handdeck.remove_card()) 
    return hand1,hand2,handdeck.all_cards

def check_total(handin):
    handscore = 0
    for count,num in enumerate(handin):
        handscore += num.value
    if handscore > 21:
     for count,num in enumerate(handin):
        if num.value == 11:
            num.value = 1
            handscore = 0
            for count,num in enumerate(handin):
                handscore += num.value  
        else:
            pass
    return handscore

def check_chips(chipamt):
    if chipamt <= 0:
        print("You are out of chips, thanks for playing")
        exit()

player1 = player('Player 1')
Dealer = player("Dealer")
game_on = True

while game_on:
    check_chips(player1.chips)
    bet_amt = 9999999
    player1.hand,Dealer.hand,gamedeck = deal_hand()
    playgame = input('\nReady to play?(y/n): ')
    if playgame == 'Y' or playgame == "y":
        pass
    else:
        exit()
    turn = ''
    hand = True
    while bet_amt > player1.chips:
        bet_amt = int(input(f"Chip Total: {player1.chips}\nHow much would you like to bet: "))
    print(f'\n{player1.name} you have a {player1.hand[0]} and a {player1.hand[1]}')
    print(f'Dealer is showing a {Dealer.hand[0]}')
    handtotal = check_total(player1.hand)
    dealertotal = check_total(Dealer.hand)

    while hand:
        while turn != "H" and turn != "S":
            turn = input('\nWhat would you like to do (S or H): ')
        if turn == 'H':
            player1.hand.append(gamedeck.pop())
            print(f'\nYou got a {player1.hand[-1]}')
            handtotal = check_total(player1.hand)
            print(f"Your handtotal is {handtotal}")  
            hand = check_bust(handtotal)
            turn = ""
        elif turn == "S":
            print("Dealer Turn!")
            while dealertotal < 17:
                if dealertotal < 17:
                    Dealer.hand.append(gamedeck.pop())
                dealertotal = check_total(Dealer.hand)
            print(f"Dealer has {dealertotal}")
        
            hand = check_win(handtotal, dealertotal)
