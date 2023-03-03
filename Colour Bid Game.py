import random

# Define the available colors and their winning probability
COLORS = {'red': 0.45, 'green': 0.55}

# Define the minimum and maximum bid amounts
MIN_BID = 1
MAX_BID = 1000

# Define the number of players and their initial balance
NUM_PLAYERS = 10
INITIAL_BALANCE = 1000

# Initialize the players' balances
player_balances = [INITIAL_BALANCE] * NUM_PLAYERS

# Game loop
while True:
    # Display each player's current balance
    print('Current balances:')
    for i, balance in enumerate(player_balances):
        print(f'Player {i+1}: ${balance}')

    # Get each player's bid for this round
    bids = []
    for i in range(NUM_PLAYERS):
        while True:
            bid = input(f'Player {i+1}, choose a color (red or green) and place a bid (between ${MIN_BID} and ${MAX_BID}): ')
            color, amount = bid.split()
            amount = int(amount)
            if color not in COLORS or amount < MIN_BID or amount > MAX_BID or amount > player_balances[i]:
                print('Invalid bid. Please try again.')
            else:
                bids.append((color, amount))
                player_balances[i] -= amount
                break

    # Determine the winning color for this round
    winning_color = random.choices(list(COLORS.keys()), list(COLORS.values()))[0]

    # Display the winning color for this round
    print(f'The winning color is {winning_color}!')

    # Calculate the total amount bid on the winning color
    total_winning_bids = sum(amount for color, amount in bids if color == winning_color)

    # Calculate the payout for the winning player
    for i, (color, amount) in enumerate(bids):
        if color == winning_color:
            payout = amount * 0.7
            player_balances[i] += payout + total_winning_bids - payout
            print(f'Player {i+1} won ${payout}!')
    
    # Check if any player has run out of money
    if min(player_balances) == 0:
        print('Game over!')
        break
