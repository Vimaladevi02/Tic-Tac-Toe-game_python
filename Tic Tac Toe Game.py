board= ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])   
def check_winner():
    winning_combinations=[
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combination in winning_combinations:
        if (board[combination[0]] == board[combination[1]] and
            board[combination[1]] == board[combination[2]]):
            return True
    return False
player="X"
for turn in range(9):
    display_board()
    position=int(input("Player " + player + ", enter position (1-9): "))
    if board[position- 1] in ["X", "O"]:
        print("Position already taken. Try again.")
        continue
    board[position- 1]=player
    if check_winner():
        display_board()
        print("Player", player, "wins!")
        break
    if player=="X":
        player="O"
    else:
        player="X"
else:
    display_board()
    print("It's a draw!")
