class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(16)] for _ in range(12)]
        self.players = []
        self.exit = (0, 0)
        self.steps = 0

        try:
            # Read map file
            with open('map.txt', 'r') as map_file:
                for i, line in enumerate(map_file):
                    for j, symbol in enumerate(line.strip()):
                        if symbol == '#':
                            self.board[i][j] = '#'

            # Read players file
            with open('players.txt', 'r') as players_file:
                for line in players_file:
                    row, col = map(int, line.strip().split())
                    self.players.append((row, col))

            # Read exit file
            with open('exit.txt', 'r') as exit_file:
                self.exit = tuple(map(int, exit_file.readline().strip()))

        except Exception as e:
            print(f"Error reading files: {e}")

    def get_board(self):
        return self.board

    def update(self, direction):
        for i in range(len(self.players)):
            row, col = self.players[i]
            new_row, new_col = row, col

            if direction == "U" and row > 0:
                new_row = row - 1
            elif direction == "D" and row < 11:
                new_row = row + 1
            elif direction == "L" and col > 0:
                new_col = col - 1
            elif direction == "R" and col < 15:
                new_col = col + 1

            # Check for collisions and update position
            if self.board[new_row][new_col] != '#' and (new_row, new_col) not in self.players:
                self.players[i] = (new_row, new_col)

        self.steps += 1

    def get_state(self):
        escaped = all(player == self.exit for player in self.players)
        dead = any(player not in self.board[player[0]][player[1]] for player in self.players)

        if escaped and dead:
            return 3  # Some robots escaped, some died
        elif escaped:
            return 1  # All robots escaped successfully
        elif dead:
            return 2  # Some robots died
        else:
            return 0  # Game not over

    def save_game(self):
        with open('save_game.txt', 'w') as save_file:
            save_file.write(f"{self.steps}\n")
            for player in self.players:
                save_file.write(f"{player[0]} {player[1]}\n")

    def load_game(self):
        try:
            with open('save_game.txt', 'r') as save_file:
                self.steps = int(save_file.readline().strip())
                self.players = [tuple(map(int, line.strip().split())) for line in save_file]
        except Exception as e:
            print(f"Error loading game: {e}")

    def get_steps(self):
        return self.steps