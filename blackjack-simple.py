import random
import time
import sys
import os
# setting vars
card = random.randint(1,11)
hand = random.randint(2,21)
dealerhand = random.randint(2,21)
playerwins = 0
dealerwins = 0
ties = 0
hands = 0
closeProgram = False
answersWrong = 0
start = 0
hitorstand = 0
# defining functions time!
def notInAnswerList():

    global answersWrong
    if answersWrong == 0:
        print("That's not what I asked, try again!")
        answersWrong += 1

    elif answersWrong == 1:
        print("That's still not what I asked, try again please!")
        answersWrong += 1
    
    elif answersWrong == 2:
        print("That's STILL not what I'm asking. Please, try again.")
        answersWrong += 1
    
    elif answersWrong == 3:
        print("Ok, still not what I'm asking. It can't be THAT hard, can it? Please, just pick one. I'm tired.")
        answersWrong += 1
    
    elif answersWrong == 4:
        print("Alright. I'm giving you ONE more chance. Either pick a goddamn answer, or I'll quit() myself. I'm not playing, alright?")
        answersWrong += 1
    
    elif answersWrong == 5:
        print("NOPE! THAT'S IT! I gave you FIVE chances, and you BLEW it. I'm done with this garbage, so help me God.")
        quit()
def gameplay():
    global hitorstand
    while hand < 21 and dealerhand < 21:
        hitorstand = input("Hit or stand?")
        while hitorstand not in ["hit","stand"]:
            notInAnswerList()
            hitorstand = input("Hit. Or. Stand. ")

        while hitorstand in ["hit","stand"]:
            if hitorstand == "hit":
                print("You hit.")
                hand += random.randint(1,11)
                break

            elif hitorstand == "stand":
                print("You stand.")
                break

    if hand > 21: 
     print("Sorry man. Your hand busted by ", hand - 21)
     playerwins = playerwins +1
    
    elif dealerhand > 21:
     print("Congradulations, the dealer busted by", dealerhand - 21)
     dealerwins = dealerwins +1


#Asks whether or not you want to start
start = input("Welcome to Blackjack! I'm going to assume you know how to play. If you don't, type 'instructions'. " \
"\nIMPORTANT: Unfortunately I haven't been able to code aces yet. " \
"\nImagine, if you will, Aces are worth 1 and there are 4 jokers worth 11. Thank you! " \
"\nNow, would you like to play? ")

while start not in ["yes","no","instructions"]:
    notInAnswerList()
    start = input("Would you like to start?")

while start in ["yes","no","instructions"]:
    if start == "no":
        print("Then why'd you even open the program?")
        quit()

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
        instructYorN = input("Alright then. Would you like to get started? ")

        while instructYorN not in ["yes,","no"]:
            notInAnswerList()
            instructYorN = input("Yes or no? ")

        while instructYorN in ["yes","no"]:
            if instructYorN == "yes":
                print("Good.")
                break
            elif instructYorN == "no":
                print("God*#%@it")
                time.sleep(1)
                print("Screw you, man.")
                quit()
                  
            break

    elif start == "yes":
        print("Alright, let's get started.")
        break
      





##startup process
print("Dealing hands...")
time.sleep(1.5)
print("Your hand is: {}".format(hand))
gameplay()
