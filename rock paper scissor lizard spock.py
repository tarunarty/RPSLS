print("Choose from (rock, paper, scissors, lizard, spock)")
print("2 points for a win")
print("1 point for a tie")
print("no points for a loss")
print("type END to stop the game")
print()
print()

p1=0
p2=0
val = ["rock","paper","lizard","scissors","spock"]
while True:

    a1=input("Player 1 plays: ").lower()
    if a1=="end":
        break
    a2=input("Player 2 plays: ").lower()
    if a2=="end":
        break
    
    if a1 not in val or a2 not in val:
        print("Incorrect values Please choose from the given list:")
        print("(rock, paper, scissors, lizard, spock)")
        print()
    else:
        if a1=="rock":
            if a2=="rock":
                p1+=1
                p2+=1
                print("Nobody wins")
            elif a2=="paper":
                p2+=2
                print("Paper covers Rock")
            elif a2=="scissors":
                p1+=2
                print("Rock crushes Scissors")
            elif a2=="lizard":
                p1+=2
                print("Rock crushes Lizard")
            else:
                p2+=2
                print("Spock vaporizes Rock")

        if a1=="paper":
            if a2=="rock":
                p1+=2
                print("Rock crushes Paper")
            elif a2=="paper":
                p1+=1
                p2+=1
                print("Nobody wins")
            elif a2=="scissors":
                p2+=2
                print("Scissors cuts Paper")
            elif a2=="lizard":
                p2+=2
                print("Lizard eats Paper")
            else:
                p1+=2
                print("Paper disproves Spock")

        if a1=="scissors":
            if a2=="rock":
                p2+=2
                print("Rock crushes Scissors")
            elif a2=="paper":
                p1+=2
                print("Scissors cuts paper")
            elif a2=="scissors":
                p1+=1
                p2+=1
                print("Nobody wins")
            elif a2=="lizard":
                p1+=2
                print("Scissors decapitates Lizard")
            else:
                p2+=2
                print("Spock smashes Scissors")

        if a1=="lizard":
            if a2=="rock":
                p2+=2
                print("Rock crushes Lizard")
            elif a2=="paper":
                p1+=2
                print("Lizard eats Paper")
            elif a2=="scissors":
                p2+=2
                print("Scissors decapitates Lizard")
            elif a2=="lizard":
                p1+=1
                p2+=1
                print("Nobody wins")
            else:
                p1+=2
                print("Lizard poisons Spock")

        if a1=="spock":
            if a2=="rock":
                p1+=2
                print("Spock vaporizes Rock")
            elif a2=="paper":
                p2+=2
                print("Paper disproves Spock")
            elif a2=="scissors":
                p1+=2
                print("Spock smashes Scissors")
            elif a2=="lizard":
                p2+=2
                print("Lizard poiosns Spock")
            else:
                p1+=1
                p2+=1
                print("Nobody wins")
                
        print("Player 1:",p1,"points | Player 2:",p2,"points")
        print()


if p1>p2:
    print("player 1 wins by",p1-p2,"points.")
elif p1<p2:
    print("player 2 wins by",p2-p1,"points.")
else:
    print("Its a tie. Everybody wins.")
        
