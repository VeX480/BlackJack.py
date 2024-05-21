import random
import sys

deck = [
    
    2, 3, 4, 5, 6, 7, 9, 10, 2, 3, 4, 5, 6, 7, 9, 10, 2, 3, 4, 5, 6, 7, 9, 10,
    2, 3, 4, 5, 6, 7, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    'A', 'A', 'A', 'A'
]
playerhand = []
dealerhand = []
hidedealerhand = []
hidedealertotal = 0
playertotal = 0
dealertotal = "?"

def play():
    playertotal = 0
    dealertotal = 0
    playerhand = []
    dealerhand = []
    hidedealerhand = []
    hidedealertotal = "?"
    deck = [

        2, 3, 4, 5, 6, 7, 9, 10, 2, 3, 4, 5, 6, 7, 9, 10, 2, 3, 4, 5, 6, 7, 9, 10,
        2, 3, 4, 5, 6, 7, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
        'A', 'A', 'A', 'A'
    ]

    def pdealcards():
        card = random.choice(deck)
        playertotal = sum(playerhand)
        if card == 'A':
            card = 1 if playertotal + 11 > 21 else 11
            playerhand.append(card)
            deck.remove('A')
        else:
            playerhand.append(card)
            deck.remove(card)

        if playertotal > 21 and 11 in playerhand:
            playerhand.remove(11)
            playerhand.append(1)
            

    def ddealcards():
        card = random.choice(deck)
        dealertotal = sum(dealerhand)
        if card == 'A':
            if hidedealerhand == []:
                hidedealerhand.append(card) 
                hidedealerhand.append("?")
            card = 1 if dealertotal + 11 > 21 else 11
            dealerhand.append(card)
            deck.remove('A')
        else:
            if hidedealerhand == []:
                hidedealerhand.append(card) 
                hidedealerhand.append("?")
            dealerhand.append(card)
            deck.remove(card)
        if dealertotal > 21 and 11 in dealerhand:
            playerhand.remove(11)
            playerhand.append(1)

    pdealcards()
    pdealcards()
    ddealcards()
    ddealcards()

    playertotal = sum(playerhand)
    print("")
    print("-------------------------------------")
    print(f'Your hand: {playerhand}')
    print(f'Total: {playertotal}')

    dealertotal = sum(dealerhand)
    print("")
    print(f"Dealer's hand: {hidedealerhand}")
    print(f'Total: {hidedealertotal}')

    if dealertotal == 21:
        print("")
        print("-------------------------------------")
        print(f"Dealer's hand: {dealerhand}")
        print(f"Dealer's Total: {dealertotal}")
        print("Dealer Blackjack!! You lose")
        startmenu()
    if playertotal == 21:
        print("")
        print("-------------------------------------")
        print("Blackjack!! You win")
        startmenu()

    def move():
        print("")
        print("-------------------------------------")
        print("What's your move?")
        print("1 - Hit")
        print("2 - Stand")

        def choice():
            choice = input('1/2: ')
            if choice == '1':
                pdealcards()
                playertotal = sum(playerhand)
                if playertotal > 21 and 11 in playerhand:
                    playerhand.remove(11)
                    playerhand.append(1)
                    playertotal = sum(playerhand)
                    print("")
                    print("-------------------------------------")
                    print(f'Your hand: {playerhand}')
                    print(f'Total: {playertotal}')
                    print("")
                    print(f"Dealer's hand: {hidedealerhand}")
                    print(f'Total: {hidedealertotal}')
                    move()
                if playertotal < 21:
                    print("")
                    print("-------------------------------------")
                    print(f'Your hand: {playerhand}')
                    print(f'Total: {playertotal}')
                    print("")
                    print(f"Dealer's hand: {hidedealerhand}")
                    print(f'Total: {hidedealertotal}')
                    move()
                elif playertotal > 21:
                    print("")
                    print("-------------------------------------")
                    print(f'Your hand: {playerhand}')
                    print(f'Total: {playertotal}')
                    print("")
                    print('You Lose!!')
                    startmenu()
                elif playertotal == 21:
                    print("")
                    print("-------------------------------------")
                    print(f'Your hand: {playerhand}')
                    print(f'Total: {playertotal}')
                    print("")
                    print("Blackjack!! You win")
                    startmenu()
            if choice == "2":


                def stand():
                    playertotal = sum(playerhand)
                    dealertotal = sum(dealerhand)
                    if dealertotal > 21 and 11 in dealerhand:
                        dealerhand.remove(11)
                        dealerhand.append(1)
                    if dealertotal <= 17:
                        ddealcards()
                        stand()

                    elif dealertotal > 21:
                        print("")
                        print("-------------------------------------")
                        print(f'Your hand: {playerhand}')
                        print(f'Your Total: {playertotal}')
                        print("")
                        print(f"Dealer's hand: {dealerhand}")
                        print(f"Dealer's Total: {dealertotal}")
                        print("")
                        print('Dealer Bust!! You win!!')

                        

                        startmenu()
                    elif dealertotal >= 18 and dealertotal < playertotal:
                        print("")
                        print("-------------------------------------")
                        print(f'Your hand: {playerhand}')
                        print(f'Your Total: {playertotal}')
                        print("")
                        print(f"Dealer's hand: {dealerhand}")
                        print(f"Dealer's Total: {dealertotal}")
                        print("")
                        print('You Win!!')

                     

                        startmenu()
                    elif dealertotal >= 18 and dealertotal > playertotal:
                        print("")
                        print("-------------------------------------")
                        print(f'Your hand: {playerhand}')
                        print(f'Your Total: {playertotal}')
                        print("")
                        print(f"Dealer's hand: {dealerhand}")
                        print(f"Dealer's Total: {dealertotal}")
                        print("")
                        print('You Lose!!')

                        

                        startmenu()
                    elif dealertotal == playertotal and dealertotal >= 18:
                        print("")
                        print("-------------------------------------")
                        print(f'Your hand: {playerhand}')
                        print(f'Your Total: {playertotal}')
                        print("")
                        print(f"Dealer's hand: {dealerhand}")
                        print(f"Dealer's Total: {dealertotal}")
                        print("")
                        print('Draw!!')

                        

                        startmenu()
                    elif dealertotal == 21:
                        print("")
                        print("-------------------------------------")
                        print(f'Your hand: {playerhand}')
                        print(f'Your Total: {playertotal}')
                        print("")
                        print(f"Dealer's hand: {dealerhand}")
                        print(f"Dealer's Total: {dealertotal}")
                        print("")
                        print("Dealer Blackjack!! You lose")
                        if dealertotal > 21 and 11 in dealerhand:
                            dealerhand.remove(11)
                            dealerhand.append(1)
                            move()
                        
                    

                        startmenu()
                    else:
                        print("")
                        print("-------------------------------------")
                        print(f'Your hand: {playerhand}')
                        print(f'Your Total: {playertotal}')
                        print("")
                        print(f"Dealer's hand: {dealerhand}")
                        print(f"Dealer's Total: {dealertotal}")

                
                stand()
        choice()
    move()
      
def startmenu():
    print("-------------------------------------")
    print('Do you want to play? ')

    enter = input('1/2 ')

    if enter == '1':
        play()

    elif enter == '2':
        print('Okay, Goodbye!')
        sys.exit(0)
        
    else:
        startmenu()

startmenu()