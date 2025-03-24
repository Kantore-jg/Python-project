from replit import clear
import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw 😂🙃"
    elif computer_score==0:
        return "Lose opponent has Blackjack 🤤"
    elif user_score==0:
        return "win with a Blackjack 😎"
    elif user_score>21:
        return "you went over. you Lose😭"
    elif computer_score>21:
        return "Opponent went over. you win 😁"
    elif user_score>computer_score:
        return "you win 😎"
    else:
        return "you lose 🙃😭"
def calculate_score(cards):
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


user_cards=[]
computer_cards=[]
for _ in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
def game():
    is_game_over=False
    while not is_game_over: 
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards: {user_cards}, current score :{user_score}")
        print(f"computer's first cards: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'Y' to get another card, type 'N' to pass: ").lower()
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score !=0 and computer_score>17:
        computer_cards.apend(deal_card())
        computer_score=calculate_score(computer_cards)
    #deal_card()
    print(f" your final hand: {user_cards}, final score: {user_score}")
    print(f" computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Type 'Y' to start the game, type 'N' to pass: ").lower() =="y":
    clear()
    game()