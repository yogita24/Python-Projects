import random
wordlist=['science','nature','study']
logo='''
      __                                      
     /  \                   
     |  |                                      
     |  |                                      
     |  |____  ____   ____                     
     |   __  \/ __  \/ __  \
     |  /  \ | |  | | |  | |  
     |  |  | | |__| | |__| |  
     |__|  |_|______||_____|
                       /  |
                      / _ |
                     |_|_||'''
                     
chosen_word=random.choice(wordlist)
x=chosen_word
result=['_ ']*len(x)
turn=len(x)
lives=6

                                              

hangman=['''        
   |__
   |  |
   |  O
___| /|\ 
[___  /\         
   |______________


   ''','''
   |__
   |  |
   |  O
___| /|\ 
[___  /                  
   |______________


   ''','''
   |__
   |  |
   |  O
___| /|\ 
[___                       
   |______________


   ''','''
   |__
   |  |
   |  O
___| /|            
[___         
   |______________


   ''','''
   |__
   |  |
   |  O
___|  |                
[___         
   |______________


   ''','''
   |__
   |  |
   |  O
___| 
[___         
   |______________


   ''']

print("Play"+hangman[0])
print(f"Guess the word and save the man")
endgame=False
print(''.join(result))
while not endgame:
      guess=input("Guess a letter").lower()
      for position in range(turn):
          #print(chosen_word[position]==guess)
          if guess==chosen_word[position]:
              result[position]=guess
    
      if guess not in chosen_word:
           lives-=1
           if lives>0:
               print(f"Ops..One life lost.Total lives:{lives}")
               print(hangman[lives])
           else:
               print("You lost")
               print(hangman[lives])
               endgame=True
      print(f"{''.join(result)}")     
      if "_ " not in result:
          endgame=True
          print("You won!!")
          break
           
              
