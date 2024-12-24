# 定義遊戲棋盤
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# 顯示棋盤
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# 檢查贏家
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# 檢查是否平局
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax 演算法
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# AI 的最佳移動
def find_best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# 主遊戲循環
def main():
    board = create_board()
    print("歡迎來到圈圈叉叉遊戲！")
    print_board(board)

    while True:
        # 玩家回合
        row, col = map(int, input("輸入你的位置 (row col): ").split())
        row-=1
        col-=1
        if board[row][col] != ' ':
            print("無效的位置，請再試一次！")
            continue
        board[row][col] = 'O'
        print_board(board)

        if check_winner(board):
            print("你贏了！")
            break
        if is_draw(board):
            print("平局！")
            break

        # AI 回合
        print("AI 的回合...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        if check_winner(board):
            print("AI 贏了！")
            break
        if is_draw(board):
            print("平局！")
            break

if __name__ == "__main__":
    main()
