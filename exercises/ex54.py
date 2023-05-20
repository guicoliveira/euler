from enum import Enum
from typing import Optional


class HandScore(Enum):
	HighCard = 0
	OnePair = 1
	TwoPairs = 2
	ThreeOfAKind = 3
	Straight = 4
	Flush = 5
	FullHouse = 6
	FourOfAKind = 7
	StraightFlush = 8
	RoyalFlush = 9

class Score:
	def __init__(self, hand_score: HandScore, data: Optional[dict]):
		self.hand_score = hand_score
		self.data = data
class Card:
	value: int = 0
	suit: str = ""

	def __str__(self):
		return f"{self.value} - {self.suit}"

class Game:
	def __init__(self):
		self.player1: list[Card] = []
		self.player2: list[Card] = []

	def __str__(self):
		s = "\nPlayer 1: "
		for card in self.player1:
			s += f"[{str(card)}] "
		s += "\nPlayer 2: "
		for card in self.player2:
			s += f"[{str(card)}] "
		return s


def exercise54():
	total_p1_hands = 0
	file = open("aux_files\\poker_hands.txt", "r")
	i = 0
	for line in file.readlines():
		i += 1
		if i < 0:
			continue
		if i > 200:
			break
		parsed_hand = parse_hand(line)
		if is_p1_winner(parsed_hand):
			total_p1_hands += 1

	print(f"Result: {total_p1_hands}")


def is_p1_winner(hands: Game) -> bool:
	p1_score = calculate_hand_value(hands.player1)
	p2_score = calculate_hand_value(hands.player2)

	if p1_score.hand_score == p2_score.hand_score:
		tiebreak(p1_score, p2_score, hands)

	print(hands)

	print(f"Player 1 score: {p1_score}")
	print(f"Player 2 score: {p2_score}")

	return True

def tiebreak(p1: Score, p2: Score) -> bool:
	scores_easy_handled = [HandScore.HighCard, HandScore.Flush, HandScore.StraightFlush, HandScore.Straight]

	if p1.hand_score in scores_easy_handled:
		return True if p1.data["value"] >= p2.data["value"] else False




def calculate_hand_value(cards: list[Card]) -> Score:
	values = [x.value for x in cards]
	values.sort()
	flush = is_flush(cards)
	straight = 	is_straight(values)

	if flush and straight:
		return Score(HandScore.RoyalFlush, None) if is_royal_flush(values) \
			else Score(HandScore.StraightFlush, {"value": values[4]})
	elif flush:
		return Score(HandScore.Flush, {"value": values[4]})
	elif straight:
		return Score(HandScore.Straight, {"value": values[4]})

	four_of_a_kind = is_four_of_a_kind(values)
	if four_of_a_kind is not None:
		return Score(HandScore.FourOfAKind, {"value": four_of_a_kind})

	three_of_a_kind = is_three_of_a_kind(values)
	if three_of_a_kind is not None:
		return three_of_a_kind

	pair = is_pair(values)
	if pair is not None:
		return pair

	return Score(HandScore.HighCard, {"value": values[4]})

def is_flush(cards: list[Card]) -> bool:
	for i in range(1, 5):
		if cards[i].suit != cards[0].suit:
			return False
	return True

def is_straight(values: list[int]) -> bool:
	for i in range(1, 5):
		if values[i] != values[0] + i:
			return False
	return True

def is_royal_flush(values):
	if 14 in values and 13 in values and 12 in values and 11 in values and 10 in values:
		return 1

def is_four_of_a_kind(values: list[int]) -> bool:
	for i in range(2):
		total = 0
		for j in range(1 + i, 4 + i):
			if values[j] == values[i]:
				total += 1

		if total == 3:
			return True

	return False

def is_three_of_a_kind(values: list[int]) -> Score or None:
	for i in range(3):
		total = 0
		for j in range(1 + i, 3 + i):
			if values[j] == values[i]:
				total += 1

		if total == 2:
			if i == 0 and values[3] == values[4]:
				return Score(HandScore.FullHouse, {"trio": values[i], "pair": values[3]})
			elif i == 2 and values[0] == values[1]:
				return Score(HandScore.FullHouse, {"trio": values[i], "pair": values[0]})
			else:
				return Score(HandScore.ThreeOfAKind, {"trio": values[i]})

	return None

def is_pair(values: list[int]) -> HandScore or None:
	pair_number = 0
	data = {}
	for i in range(4):
		if values[i] == values[i + 1]:
			pair_number += 1
			if pair_number == 1:
				data["pair"] = values[i]
			if pair_number == 2:
				data["pair2"] = values[i]

	if pair_number == 1:
		return Score(HandScore.OnePair, data)
	if pair_number == 2:
		return Score(HandScore.TwoPairs, data)

	return None

def parse_hand(line: str) -> Game:
	game = Game()
	cards = line.split(" ")
	for i in range(10):
		card = parse_card(cards[i])
		if i < 5:
			game.player1.append(card)
		else:
			game.player2.append(card)

	return game

def parse_card(card_data: str) -> Card:
	card = Card()

	try:
		card.value = int(card_data[0])
	except ValueError:
		if card_data[0] == "T":
			card.value = 10
		if card_data[0] == "J":
			card.value = 11
		if card_data[0] == "Q":
			card.value = 12
		if card_data[0] == "K":
			card.value = 13
		if card_data[0] == "A":
			card.value = 14
	card.suit = card_data[1]
	return card
