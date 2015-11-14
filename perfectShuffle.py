import random

deck = []
for i in range (1, 53):
	deck.append(i)

print(deck)
def perfShuffle(deck):
	newDeck = []
	for i in range(0, 52):
		rand = random.sample(deck, 1)[0]
		deck.remove(rand)
		newDeck.append(rand)
	return newDeck
print perfShuffle(deck)
