from distributed_poker.base import Card
import numpy

class Deck(object):
    def __init__(self):
        self.cards = []
        self.cardsInGame = []
        self.Shuffle()

    def Shuffle(self):
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        hearts = [Card('hearts', value) for value in values]
        spades = [Card('spades', value) for value in values]
        clubs = [Card('clubs', value) for value in values]
        dimonds = [Card('dimonds', value) for value in values]

        self.cards = hearts + spades + clubs + dimonds
        self.cardsInGame = []
        numpy.random.shuffle(self.cards)

    def draw(self, numberOfDraws=1):
        draws = []
        for drawNumber in range(numberOfDraws):
            drawedCard = self.cards.pop()
            draws.append(drawedCard)
            self.cardsInGame.append(drawedCard)

        return draws

    def isEmpty(self):
        return len(self.cards) == 0
