# Fifth class 02/21/2023

from flask import Flask, request
import poker
import json 
import uuid

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Everyone!'


@app.route('/hand')
def deal_hand():
    deck = poker.Deck()

    return {
        'hand': str(deck.deal())
    }
@app.route('/hands')
def deal_hands():
    num_hands = request.args.get('hands')
    num_hands = int(num_hands)
    deck = poker.Deck()
    hands = []
    for _ in range(num_hands):
        hands.append(str(deck.deal()))
    
    return {
        'hands': hands
    }

@app.route('/determine', methods=['POST'])
def determine():
    hands = json.loads(request.data)
    print(hands['hand1'])
    print(hands['hand2'])
    hand1 = poker.Hand.fromString(hands['hand1'])
    hand2 = poker.Hand.fromString(hands['hand2'])
    return {
        'winner': poker.determineWinner(hand1, hand2)
    }

videoPokerSessions = {}

@app.route('/videoPoker', methods=['POST', 'GET'])
def videoPoker():
    deck = poker.Deck()

    if request.method == 'GET':
        session = str(uuid.uuid1())
        hand = deck.deal()
        videoPokerSessions[session] = {
            'hand': hand,
            'deck': deck
        }

        return {
            'hand': str(hand),
            'session': session
        }
    
    if request.method == 'POST':
        data = json.loads(request.data)
        if data.get('session', None) not in videoPokerSessions:
            return {'error': 'Session not found!'}
        
        session = data['session']
        game = videoPokerSessions[session]
        holds = data.get('holds', [])
        cards = [game['hand'].cards[i] for i in holds]
        if len(cards) < 5:
            # get some new cards! Add them to the held cards
            new_cards = deck.deal(num=5-len(cards)).cards
            hand = poker.Hand(cards + new_cards)
        else:
            hand = game['hand']
        del videoPokerSessions[session]
        return {
            'hand': str(hand),
            'score': hand.getScore()
        }
