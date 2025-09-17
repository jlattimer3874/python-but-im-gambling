import random
import time
import sys
# setting vars
#card = random.randint(1,11)
hand = random.randint(2,21)
dealerhand = random.randint(2,21)
playerwins = 0
dealerwins = 0
ties = 0
hands = 0
closeProgram = False
#this is for if i don't catch anything, and something isn't attributed properly
whoopsies = 0

#Asks whether or not you want to start
start = input("Welcome to Blackjack! I'm going to assume you know how to play. If you don't, type 'instructions'. " \
"\nIMPORTANT: Unfortunately I haven't been able to code aces yet. " \
"\nImagine, if you will, Aces are worth 1 and there are 4 jokers worth 11. Thank you! " \
"\nNow, would you like to play?  ")

while start not in ["yes","no","instructions"]:
    if start == "no":
        print("Then why'd you even open the program?")
        closeProgram = True ## i'm only leaving this comment here instead of the others so i don't have to re-write it, but any sort of quit or even raising the SystemExit will only kill the current thread
        
        


    elif start == "instructions":
        print("In Blackjack, everyone plays against the dealer. Players receive all cards face up, and the dealer’s first card is face up and the second is face down. " \
        "\nThe object of the game is to get closer to 21 than the dealer without going over 21. If a hand goes over 21, it is called a “bust” or “break,” and the" \
        "\nwager is lost. In 21, Jacks, Queens, Kings, and 10s count as 10. An Ace may be played as a one or an 11. All other cards are played at face value." \
        "\nWhen you receive your first two cards, you may either “stand” or “hit.” When you “stand,” it means you feel you are close enough to 21 and no longer" \
        "\nwish any additional cards, indicated by waving off with your hand. If you wish to receive another card or “hit,” tap or scratch the table behind your" \
        "\nwager with your finger.  In either situation, you will never touch the cards; everything is communicated using hand signals. You may draw as many" \
        "\ncards as you want until you are close to 21 or until you “bust.”" \
        "\nIf you are closer to 21 than the dealer, you win and are paid an amount equal to your original wager. If your hand is less than the dealer’s, you lose. If" \
        "\nthe dealer’s hand “busts” or “breaks,” you win as well. Ties are a standoff or “push,” and your bet remains on the table." \
        "\nIf your initial two cards total 21, any Ace with a 10, Jack, Queen, or King, you have a Blackjack. Blackjack is paid either 6 to 5 or 3 to 2, depending on" \
        "\nthe type of Blackjack you are playing." \
        "\n these instructions were sourced from : https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-blackjack.html")
        instructYorN = input("Alright then. Would you like to get started?")
        while instructYorN not in ["yes","no"]:
            if instructYorN == "yes":
                print("Good.")
            elif instructYorN == "no":
                print("God*#%@it")
                
            else:
                print("'K man, I'm asking you a question. could you answer me please?")       
    elif start == "yes":
        print("Alright, let's get started.")
    else:
         print("Dude, c'mon, just pick one please")    

## this is for closing the program, since i can't close it from within a thread, all it does is check for the closeProgram boolean and if true, ACTUALLY quits the damn thing. what the fuck, why can't i terminate the whole thing 
## from within a thread??? fucking coding languages making me pissed off. GRAHHHH i'm so mad



##startup process
print("Dealing hands...")
time.sleep(2.5)
print("Your hand is: {}".format(hand))
while hand < 21 and dealerhand < 21:
    hitorstand = input("That's your hand. Would you like to hit or stand?")
    while hitorstand not in ["hit","stand"]:
        if hitorstand == "hit":
            print("You hit.")
            hand += random.randint(1,11)

        elif hitorstand == "stand":
            print("You stand.")

        else:
            print("Hit. Or. Stand.")

    if hand > 21: 
        print("Sorry man. Your hand busted by ", hand - 21)
        playerwins = playerwins +1
    
    if dealerhand > 21:
        print("Congradulations, the dealer busted by", dealerhand - 21)
        dealerwins = dealerwins +1
        






    


##print("The total number of dealer wins was {}. The total number of player wins was {}. The total number of ties was {}.".format(dealerwins,playerwins,ties))
##print("you made {} whoopsies".format(whoopsies))