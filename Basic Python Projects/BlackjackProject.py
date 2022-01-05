  import random
  import os
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10]

  def deck_card():
      '''Returns random card from deck'''
      #For jack/king/queen-->10 points
      #For Ace -->11 or 1
      card=random.choice(cards)
      cards.remove(card)
    return card
def calculate_score(cardlist):
    ''''Take a list of cards and return the score calculated from cards'''
    score=sum(cardlist)
    if sum(cardlist)==21 and len(cardlist)==2:
        score=0
    elif 11 in cardlist and sum(cardlist)>21:
        score=sum(cardlist)-10
    return score    
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def playgame():     
    user_card=[]
    computer_card=[]
    print("Hi, i am your opponent Robo :-)")
    username=input("What's your good name?")
    for i in range(2):
        #new_card=deck_card()
        user_card.append(deck_card())
        computer_card.append(deck_card())
    user_score=calculate_score(user_card)
    computer_score=calculate_score(computer_card)
    is_game_over=False
    while not(is_game_over):
        print(f"Hi,{username}..your cards:{user_card}")
        print(f"Robo card:{computer_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            choice=input("Do you want to take more cards? (Y/N)").lower()
            if choice=='y':
                user_card.append(deck_card())
            else:
                user_score= calculate_score(user_card)  
                is_game_over=True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deck_card())
        computer_score = calculate_score(computer_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score)) 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    playgame()