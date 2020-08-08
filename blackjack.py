
import random
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]
#new list to show which cards dealt
dealt=[]
#dealt values
d_values=[]
#comupter values/lsits
c_dealt=[]
c_values=[]

#validation loop for bank
while True:
    try:
        bank=float(input("Enter how much money you have: "))
        break
    except:
        print("Invalid input, try again.")
#if they have no money
if bank<=0:
    print("You do not have enough money to play.")
    quit
#if they have
else:
    #while they have enough money
    while bank > 0:
        #ask if they want to play
        prompt=input("Would you like to play? y or n: ")
        while True:
            if prompt=="y":
                break
            elif prompt=="n":
                quit()
            else:
                print("Invalid input, try again.")
        #Enter how much money you would like to bed
        while True:
            try:
                while True:
                    bet=float(input("Enter how much money you would like to bet: "))
                    if bet>bank:
                        print("You do not have enough money")
                    elif bet>0:
                        break
                    else:
                        print("Invalid bet, try again.")
                    
                break
            except:
                print("Invalid input, try again.")



            
        #deal two cards
        card_1=random.choice(cards)
        location=cards.index(card_1)
        dealt+=[card_1]
        #if the card is an ace ask for user input
        if values[location]==[1,11]:
            print("You have drawn an Ace as your first card!")
            print("Would you like for it to count as 1 or 11 points?")
            ask=input("Enter either 1 or 11: ")
            while True:
                if ask=="1":
                    d_values+=[1]
                    break
                elif ask=="11":
                    d_values+=[11]
                    break
                else:
                    print("Invalid input, try again.")
        #add to the list the values ofthe card
        else:               
            d_values+=[values[location]]
        #remove the cards after they've been dealt
        del cards[location]
        del values[location]

        card_2=random.choice(cards)
        location=cards.index(card_2)

        if values[location]==[1,11]:
            print("You have drawn an Ace as your second card!")
            print("Your first card is as follows:", dealt)
            print("It is worth:", d_values)
            print("Would you like for it to count as 1 or 11 points?")
            ask=input("Enter either 1 or 11: ")
            while True:
                if ask=="1":
                    d_values+=[1]
                    break
                elif ask=="11":
                    d_values+=[11]
                    break
                else:
                    print("Invalid input, try again.")
        else:
            d_values+=[values[location]]
        dealt+=[card_2]
        del cards[location]
        del values[location]
        #print player hand
        print("Player hand:", dealt, "is worth", sum(d_values))
        #if they reach 21
        if sum(d_values)==21:
            print("Player wins! Blackjack!")
            bank += bet*2
            print("You have", bank, "dollars in your bank")
        elif sum(d_values)>21:
            print("Bust!")
            print("Computer wins!")
            bank -= bet
            print("You have", bank, "dollars in your bank")
        else:
            #if they continue to play the game
            while True:
                h_s=input("(h)it or (s)tand? ")
                #hit
                if h_s=="h":
                    card=random.choice(cards)
                    location=cards.index(card)
                    dealt+=[card]
                    if values[location]==[1,11]:
                        print("You have drawn an Ace as your card!")
                        print("The cards in your hand are as follows:", dealt)
                        print("They are worth:", d_values)
                        print("Would you like for it to count as 1 or 11 points?")
                        ask=input("Enter either 1 or 11: ")
                        while True:
                            if ask=="1":
                                d_values+=[1]
                                break
                            elif ask=="11":
                                d_values+=[11]
                                break
                            else:
                                print("Invalid input, try again.")
                    else:
                        d_values+=[values[location]]
                    del cards[location]
                    del values[location]
                    print("You drew", card)
                    print("Player hand:", dealt, "is worth", sum(d_values))
                    if sum(d_values)==21:
                        print("Player wins! Blackjack!")
                        bank += bet*2
                        print("You have", bank, "dollars in your bank")
                        break
                    elif sum(d_values)>21:
                        print("Bust!")
                        print("Computer wins!")
                        bank -= bet
                        print("You have", bank, "dollars in your bank")
                        break
                    else:
                        continue
                #computer
                elif h_s=="s":
                    card_1=random.choice(cards)
                    location=cards.index(card_1)
                    c_dealt+=[card_1]
                    #random to determine card
                    if values[location]==[1,11]:
                        ask=random.randint(1,2)
                        while True:
                            if ask==1:
                                c_values+=[1]
                                break
                            else:
                                c_values+=[11]
                                break
                    else:        
                        c_values+=[values[location]]
                    del cards[location]
                    del values[location]

                    card_2=random.choice(cards)
                    location=cards.index(card_2)
                    c_dealt+=[card_2]
                    if values[location]==[1,11]:
                        ask=random.randint(1,2)
                        while True:
                            if ask==1:
                                c_values+=[1]
                                break
                            else:
                                c_values+=[11]
                                break
                    else:
                        c_values+=[values[location]]
                    del cards[location]
                    del values[location]
                    print("Computer hand:", dealt, "is worth", sum(c_values))
                    hit=True
                    #continue to hit until they have reached the cocnclusions at the bottom
                    while hit:
                        card=random.choice(cards)
                        location=cards.index(card)
                        
                        if values[location]==[1,11]:
                            #if card is ace, randomly choose which value it takes
                            ask=random.randint(1,2)
                            while True:
                                if ask==1:
                                    c_values+=[1]
                                    break
                                elif ask==2:
                                    c_values+=[11]
                                    break
                                else:
                                    print("Invalid input, try again.")
                        else:
                            c_values+=[values[location]]
                        c_dealt+=[card]
                        del cards[location]
                        del values[location]
                        print("Computer drew", card)
                        print("Computer hand:", c_dealt, "is worth", sum(c_values))
                        if sum(c_values)==21:
                            print("Computer got 21!  Blackjack!")
                            print("Computer wins!")
                            bank -= bet
                            print("You have", bank, "dollars in your bank")
                            break
                        elif sum(c_values)>21:
                            print("Bust!")
                            print("Player wins.")
                            bank += bet*2
                            print("You have", bank, "dollars in your bank")
                            break
                        elif sum(c_values)>sum(d_values):
                            print("Computer wins")
                            bank += bet*2
                            print("You have", bank, "dollars in your bank")
                            break
                        elif sum(c_values)<sum(d_values):
                            print("Player wins")
                            bank += bet*2
                            print("You have", bank, "dollars in your bank")
                            break
                        else:
                            continue
                    break
                else:
                    print("Invalid input, try again.")

