import random


def main():
    
    player_bet = 10
    dealer_bet = 10
    while player_bet > 0 and dealer_bet > 0:
        print("♦️♥️BlackJack♠️♣️")
        print("Make your choice to beat the dealer!")
        print(f"Player:{player_bet} Dealer:{dealer_bet}")
        print("")
        input("Press Enter to continue....")

        num1 = random.randint(1, 10)
        #num2 = random.randint(1, 11)
        num3 = random.randint(1, 10)
        num4 = random.randint(1, 11)
        player = num1 + num2
        dealer = num3 + num4

        print(f"Player got {num1} and {num2},total {player}.")
        print(f"Dealer got {num3} and {num4},total {dealer}")
        print("")
        print("How many do you want to bet?")
        while True:
            bet = input(f"You have {player_bet} points. ")
            try:
                bet = int(bet)
                if bet > player_bet:
                    print("You don't have that much.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter a numerical value.")

        while player <= 21:
            print("")
            choice = input("Hit or Stand? ")
            print("")
            if choice == "Hit":
                num = hit()
                player = player + num
                print(f"You got {num}.")
                print(f"Your count is {player}.")
                if player > 21:

                    print("Busted!Player lose.")
                    player_bet -= bet
                    dealer_bet += bet
                    break
                elif player == 21:

                    print("Blackjack! Player win!")
                    player_bet += bet
                    dealer_bet -= bet
                    break
            elif choice == "Stand":
                print(f"Your count is {player}.")
                break
            else:

                print("Please choose Hit or Stand.")
        while dealer < player and player != 21 and player < 21:
            num = hit()
            dealer += num
            print("")
            print(f"Dealer got {num}.")
            print(f"Dealer's count is {dealer}.")
            print("")
            if dealer > 21:
                print("Busted! Player win.")
                print("")
                player_bet += bet
                dealer_bet -= bet
                break
            elif dealer == 21:
                print("Blackjack! Player lose!")
                print("")
                player_bet -= bet
                dealer_bet += bet
                break
        if player <= 21 and dealer <= 21:
            print("")
            print(f"{player}vs{dealer}")
            if player > dealer and player != 21:
                print("Player win!")
                player_bet += bet
                dealer_bet -= bet
            elif dealer > player:
                print("Player lose!")
                player_bet -= bet
                dealer_bet += bet
            elif dealer == player:
                print("Draw!")
        input("Press to continue.....")
    if player_bet <= 0:
        print("")
        print("What a pity!")
        print("Maybe you be luckier next time!")
    else:
        print("")
        print("Well done!")
        print("You beat the dealer!")


def hit():
    num = random.randint(1, 11)
    return num


if __name__ == "__main__":
    main()
