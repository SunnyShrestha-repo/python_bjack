"""
This is a simple program that simulates the BlackJack just for the dealer
and calculates the probability of dealer getting cards which total up to 21
"""

import random

def atHand(cards):
    return(cards[0]+cards[1])


def stoppingReached(aTuple):
        total = atHand(aTuple) + 10
        if total>=17 and total<=21:
            print("Stopping total ",total," reached!")
            
#main function that simulates the card dealing for total number of runs given
def BlackJack(runs):
    hasAce = False 
    busted = 0 
    totalGames = 0 
    dealer = (random.randint(1,10), random.randint(1,10))
    #Random cards drawn    
    if 1 in dealer:
            hasAce = True 

    while totalGames < runs:
        if hasAce:
            stoppingReached(dealer)#breaks the while loop when ace is detected
        else:
            newDraw = random.randint(1,10) #new card is drawn
            newTotal = atHand(dealer)+newDraw
            if newTotal>=21: 
                busted += 1                
        totalGames += 1
    print("The probability of dealer getting busted: ", busted,"/",totalGames)

        

if __name__ == "__main__":
    programRun = int(input("Enter how many games you want dealer to play: "))
    BlackJack(programRun)
