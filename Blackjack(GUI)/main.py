import pygame
import random
from logo import logo

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)
white = (255, 255, 255)

window = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont('Comic Sans', 20)


clock = pygame.time.Clock()
is_running = True


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card = random.choice(cards)
    return card

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def winner(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "You have busted, you loose!"

    if player_score == dealer_score:
        return "That's a draw!"

    elif dealer_score == 0:
        return "You lost, opponent has Blackjack!"

    elif player_score == 0:
        return "You got Blackjack, you win!"

    elif player_score > 21:
        return "You bust, you loose."

    elif dealer_score > 21:
        return "Dealer has busted, you win!"

    elif player_score > dealer_score:
        return "You have a higher score, you win!"

    else:
        return "Dealer has a higher score, you loose!"


def blackjack():
    text_surface = font.render(logo, True, white)

    player_cards = []
    dealer_cards = []

    for card in range(2):

        player_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    while True:

        player_score = score(player_cards)
        dealer_score = score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True

        else:
            hit_hold = input("Type 'y' to get another card, type 'n' to pass: ")

            if hit_hold == 'y':
                player_cards.append(deal_cards())

        while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(deal_cards())
            dealer_score = score(dealer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Dealer's final hand {dealer_cards}, final score: {dealer_score}")

        print(winner(player_score, dealer_score))


while is_running:

    for event in pygame.event.get():        # Event handling
        if event.type == pygame.QUIT:
            is_running = False

    test_surface = font.render('Would you like to play a game of blackjack? Press y or n', True, (255, 255, 255))
    window.blit(test_surface, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                blackjack()

    pygame.display.update()


