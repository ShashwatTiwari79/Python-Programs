import random
# calculating number of wins , loss and number of bets and then printing them
def gambler_play(stake,goal,trials):
    wins = 0
    num_bets = 0
    loss = 0
    for i in range(trials):
        amt = stake
        bets = 0
        while amt>0 and amt<goal:
            bets = bets+1
            if random.random()>0.5:
                amt = amt+1
            else:
                amt = amt-1
        num_bets = num_bets+bets
        if amt==goal:
            wins = wins+1
        else:
            loss = loss+1
    print(f"\nNumber of bets = {num_bets/trials}")
    print(f"Number of wins = {wins}")
    print(f"number of loss={loss}")
    print(f"percentage of win = {(wins/trials)*100}")
    print(f"percentage of loss = {(loss/trials)*100}")

stake = int(input("Enter the value in the stake:-"))
goal = int(input("Enter the goal:-"))
trials = int(input("Enter the number of trials:-"))
gambler_play(stake,goal,trials)

