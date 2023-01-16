import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol , count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)
    columns =[]
    for col in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)            
        columns.append(column)            
    return columns

def print_slot_machine(columns):
    #this is known as transposing
    
    print("------------")
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=' | ')
            else:
                print(column[row])            
    print("------------")
    
def check_winning(columns,lines,bet,values):
    winnings =0
    winning_line =[]
    for line in range(lines):
        symbol = columns[0][line]
        for i in columns:
            symbol_to_check = i[line]
            if symbol!= symbol_to_check:
                break
        else:
            winnings +=values[symbol]*bet
            winning_line.append(line+1)
    
    return winnings,winning_line

def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("please enter number more than 0")
        else:
            print("!! enter a valid amount !!")
    return amount

def get_bet():
    while True:
        bet = input(f"Enter the number of Amount to bet on( {MIN_BET} - {MAX_BET} ) ?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:  # if you want to check if a value is in between 2 values 
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Please enter the number")
    return bet

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on( 1-"+str(MAX_LINES)+") ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # if you want to check if a value is in between 2 values 
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter the number")
    return lines

def game(amount):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet >amount:
            print(f'You dont have enough amount to bet , your balance is ${amount}')
            answer = input("Do you want to add more Press[Y] or continue with the amount Press[N] ?")
            if answer=='Y'or answer=='y':
                main()
        else:
            break
    print("----------------------------------------------------------")
    print(f"You are betting ${bet} on {lines} Lines. Total bet ${total_bet}")
    result = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(result)
    winning,winning_line=check_winning(result,lines,bet,symbol_value)
    if winning !=0:
        print(f"You have won ${winning} in Lines:",*winning_line)
        return amount+winning
    else:
        print("Better Luck next time!!")
    print(winning,total_bet)
    return amount-total_bet
def main():
    amount = deposit() 
    while True:
        print(f"current balance ${amount}")
        answer = input("Press enter to play ( q to Quit)")
        if answer == 'q' or answer=="Q":
            break
        amount = game(amount)
    print(f"You have ${amount} left")
    
main()