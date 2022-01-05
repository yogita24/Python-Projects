character_list=['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','1','2','3','4','5','6','7','8','9','&','^']
#choice=input("Type encode to encrypt and decode to decrypt")

def caeser_cipher(true_text,choice,shift):
    new_word=""
    if choice=="decode":
        shift*=-1
        print(shift)
    elif choice=="encode":
        shift*=1
    for char in true_text:
        if char in character_list:
            position=character_list.index(char)
            new_position=(position+shift)%len(character_list)
            print(new_position)
            new_word+=character_list[new_position]
        else:
            new_word+=char
    return new_word
            
            
            
stay_connected="Yes"
while stay_connected=="Yes":
      print("\n")
      choice=input("Type encode to encrypt and decode to decrypt").lower()
      if choice not in ["encode","decode"]:
          print("Please type: encode/decode only for further go :-)")
          stay_connected=input("Do you want to continue (Yes/No)").title()
          
      else:
          original_text=input(f"\nEnter the word you want to {choice}").lower()
          shift_1=int(input("By now many steps you want to shift"))
          shift=shift_1%26
          ciphered_text=caeser_cipher(original_text,choice,shift)
          print(f"{choice} word is {ciphered_text}")
          stay_connected=input("Do you want to continue (Yes/No)").title()

