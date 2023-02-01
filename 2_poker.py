###########################################################
# 
#    $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
#    $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
#    $$ |  $$ |$$ /  $$ |$$ |$$  / $$ |      $$ |  $$ |
#    $$$$$$$  |$$ |  $$ |$$$$$  /  $$$$$\    $$$$$$$  |
#    $$  ____/ $$ |  $$ |$$  $$<   $$  __|   $$  __$$< 
#    $$ |      $$ |  $$ |$$ |\$$\  $$ |      $$ |  $$ |
#    $$ |       $$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
#    \__|       \______/ \__|  \__|\________|\__|  \__|#
#
# Hands are as follows (in order of winningness):
#   - Royal flush (All cards have the same suit, A, K, Q, J, 10)
#   - Straight flush
#   - four of a kind
#   - full house
#   - flush
#   - straight
#   - three of a kind
#   - two pairs
#   - pair
#   - high card
#
###########################################################

from random import shuffle 

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

cards = []
for value in values:
    for suit in suits:
        cards.append((value, suit))

straightCombos = []
for i in range(9):
    combo = values[i:i+5]
    combo = ''.join(combo)
    straightCombos.append(combo)

straightCombos.append('A2345')

for combo in straightCombos:
    print(combo)



shuffle(cards)


def deal(cards):
    hand = cards[0:5]
    cards = cards[5:]
    return hand, cards


hand, cards = deal(cards)

def getCounts(hand):
    counts = {}
    for card in hand:
        if card[0] not in counts:
            counts[card[0]] = 0
        counts[card[0]] += 1
    return counts

def pair(hand):
    counts = getCounts(hand)
    for count in counts.values():
        if count == 2:
            return True
    return False

def threeOfAKind(hand):
    counts = getCounts(hand)
    for count in counts.values():
        if count == 3:
            return True
    return False

def fourOfAKind(hand):
    counts = getCounts(hand)
    for count in counts.values():
        if count == 4:
            return True
    return False

def fullHouse(hand):
    return pair(hand) and threeOfAKind(hand)

def flush(hand):
    suits = set()
    for card in hand:
        suits.add(card[1])
    return len(suits) == 1

def cardValue(card):
    return values.index(card[0])

def straight(hand):
    hand.sort(key=cardValue, reverse=False)
    handVals = ''.join([card[0] for card in hand])
    print(handVals)
    return handVals in straightCombos

def straightFlush(hand):
    return straight(hand) and flush(hand)

def royalFlush(hand):
    hand.sort(key=cardValue, reverse=False)
    handVals = ''.join([card[0] for card in hand])
    return handVals == '10JQKA' and flush(hand)

def twoPair(hand):
    counts = getCounts(hand)
    return sorted(counts.values()) == [1, 2, 2]

hand = [('9', 'Spades'), ('9', 'Spades'), ('9', 'Spades'), ('Q', 'Spades'), ('Q', 'Spades')]


hand2 = [('2', 'Spades'), ('2', 'Spades'), ('2', 'Spades'), ('A', 'Spades'), ('A', 'Spades')]


#   - Royal flush (All cards have the same suit, A, K, Q, J, 10)
#   - Straight flush
#   - four of a kind
#   - full house
#   - flush
#   - straight
#   - three of a kind
#   - two pairs
#   - pair
#   - high card

# How do you actually return card values, sorted in the correct order, so that they can be compared
# against another hand?
def getScoresByType(hand):
    if royalFlush(hand):
        return 9
    if straightFlush(hand):
        return 8
    if fourOfAKind(hand):
        return 7
    if fullHouse(hand):
        return 6 #+ [card[0] for card in hand]
    if flush(hand):
        return 5
    if straight(hand):
        return 4
    if threeOfAKind(hand):
        return 3
    if twoPair(hand):
        return 2
    if pair(hand):
        return 1
    return 0 #+ hand.sort(key=cardValue, reverse=True)

