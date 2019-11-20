from distributed_poker.base.card import Card

class Player(object):
    def __init__(self, name, initialChips=0):
        self.name = name
        self.__chips = initialChips
        self.__chipsInThePot = 0
        self.__isDealer = False
        self.__isBigBlind = False
        self.__isSmallBlind = False
        self.isPlaying = False
        self.isOnTable = True
        self.__cardsInHand = []

    def __str__(self):
        return self.__dict__

    def __canBet(self, betSize):
        return betSize <= self.__chips

    def bet(self, betSize):
        if not self.isOnTable:
            raise ValueError(f'{self.name} isnt on the table')
        elif self.__canBet(betSize):
            self.__chips -= betSize
            self.__chipsInThePot += betSize
        else:
            raise ValueError(f'{self.name} cant bet {betSize}, he/she only has {self.__chips} chips')
        pass

    def wonPot(self, potSize):
        self.__chips += potSize
        self.__chipsInThePot = 0

    def receiveCard(self, card):
        if not self.isOnTable:
            raise ValueError(f'{self.name} isnt on the table')
        elif card is None or not isinstance(card, Card):
            raise ValueError('The card must be a "Card"')
        elif len(self.cardsInHand) == 2:
            raise ValueError(f'{self.name} already has 2 cards in hand. THIS IS TEXAS HOLDEM!')
        else:
            self.__cardsInHand.append(card)
        pass

    def fold(self):
        if not self.isOnTable:
            raise ValueError(f'{self.name} isnt on the table')
        self.isPlaying = False
        self.__cardsInHand = []
        self.__chipsInThePot = 0

    def cleanStatus(self):
        self.__isDealer = False
        self.__isBigBlind = False
        self.__isSmallBlind = False

    @property
    def isDealer(self):
        return self.__isDealer

    @isDealer.setter
    def isDealer(self, value):
        if not self.isOnTable:
            raise ValueError(f'{self.name} isnt on the table')
        elif value == True:
            if self.__isBigBlind or self.__isSmallBlind:
                raise ValueError(f'{self.name} cant be the Dealer because he/she already is Small or Big Blind')

        self.__isDealer = bool(value)

    @property
    def isBigBlind(self):
        return self.__isBigBlind

    @isBigBlind.setter
    def isBigBlind(self, value):
        if not self.isOnTable:
            raise ValueError(f'{self.name} isnt on the table')
        elif value == True:
            if self.__isDealer or self.__isSmallBlind:
                raise ValueError(f'{self.name} cant be the Big Blind because he/she already is Dealer or Small Blind')

        self.__isBigBlind = bool(value)

    @property
    def isSmallBlind(self):
        return self.__isSmallBlind

    @isSmallBlind.setter
    def isSmallBlind(self, value):
        if not self.isOnTable:
            raise ValueError(f'{self.name} isnt on the table')
        elif value == True:
            if self.__isBigBlind or self.__isDealer:
                raise ValueError(f'{self.name} cant be the Small because he/she already is Dealer or Big Blind')

        self.__isSmallBlind = bool(value)
