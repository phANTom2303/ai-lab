import heapq

goal_state = [1,2,3,4,5,6,7,8,0]
moves = {'U': -3, 'D': 3, 'L': -1, 'R': 1}

class PuzzleState:
    def __init__(self, board, parent, move, depth, total_cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.total_cost = total_cost
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost


def heuristic(board):
    wrong_tiles = 0
    for i in range(9):
        if board[i] != 0 and board[i] != goal_state[i]:
            wrong_tiles += 1
    return wrong_tiles 


def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + moves[move]

    new_board[blank_pos] = new_board[new_blank_pos]
    new_board[new_blank_pos] = 0
    
    return new_board


def print_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print("------")


def print_solution(solution):
    path = []
    current = solution

    while current:
        path.append(current)
        current = current.parent

    path.reverse()

    step_num = 0
    for state in path:
        print("Step", step_num, "- Move:", state.move)
        print_board(state.board)
        step_num += 1


def a_star(start_board):
    open_list = []
    close_list = set()

    start_cost = heuristic(start_board)
    heapq.heappush(open_list, PuzzleState(start_board, None, "", 0, start_cost))

    while open_list:
        current = heapq.heappop(open_list)

        if current.board == goal_state:
            return current  

        close_list.add(tuple(current.board)) 

        blank_pos = current.board.index(0)

        for move_name in ['U', 'D', 'L', 'R']:

            # Skip invalid moves
            if move_name == 'U' and blank_pos < 3:
                continue
            if move_name == 'D' and blank_pos > 5:
                continue
            if move_name == 'L' and blank_pos % 3 == 0:
                continue
            if move_name == 'R' and blank_pos % 3 == 2:
                continue

            new_board = move_tile(current.board, move_name, blank_pos)

            if tuple(new_board) in close_list:
                continue

            new_depth = current.depth + 1
            new_h = heuristic(new_board)
            new_total_cost = new_depth + new_h

            new_state = PuzzleState(new_board, current, move_name, new_depth, new_total_cost)
            heapq.heappush(open_list, new_state)

    return None


initial_state = [1,2,3,4,0,5,6,7,8]

print("Starting puzzle:")
print_board(initial_state)

solution = a_star(initial_state)

if solution:
    print("SOLVED in", solution.depth, "moves!")
    print_solution(solution)
else:
    print("Cannot solve this puzzle")