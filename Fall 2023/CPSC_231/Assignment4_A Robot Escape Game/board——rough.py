class Board:
    def __init__(self):
        self.board = self.load_map('map.txt')
        self.players = self.load_players('players.txt')
        self.exit = self.load_exit('exit.txt')

    def load_map(self, file_path):
        try:
            with open(file_path, "r") as map_file:
                return [list(line.strip().replace('#', ' ')) for line in map_file]
        except FileNotFoundError:
            print("Map file not found")
            return []

    def load_players(self, file_path):
        try:
            with open(file_path, 'r') as players_file:
                return [tuple(map(int, line.strip().split())) for line in players_file]
        except FileNotFoundError:
            print("Players file not found")
            return []

    def load_exit(self, file_path):
        try:
            with open(file_path, 'r') as exit_file:
                return tuple(map(int, exit_file.readline().strip().split()))
        except FileNotFoundError:
            print("Exit file not found")
            return ()

    def get_board(self):
        return self.board

    def update(self, direction):
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        new_players = []
        for row, col in self.players:
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]

            if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[0]):
                if self.board[new_row][new_col] != "#":
                    new_players.append((new_row, new_col))

        self.players = new_players

    def get_state(self):
        if not self.players:
            return 1  # Win
        elif not self.players:
            return 2  # Lose (no players left)
        elif not self.players:
            return 3  # Lose (other condition)
        else:
            return 0  # Continue playing

    def save_game(self):
        try:
            with open("save_game.txt", "w") as save_file:
                self.write_section(save_file, "Board", self.board)
                self.write_section(save_file, "Players", self.players)
                self.write_section(save_file, "Exit", [self.exit])
        except Exception as e:
            print(f"Error saving game: {e}")

    def write_section(self, file, header, data):
        file.write(f"{header}:\n")
        for item in data:
            if isinstance(item, tuple):
                file.write(f"{item[0]} {item[1]}\n")
            elif isinstance(item, list):
                file.write("".join(item) + "\n")

    def load_game(self):
        try:
            with open("save_game.txt", "r") as save_file:
                self.read_section(save_file, "Board", self.load_map)
                self.read_section(save_file, "Players", self.load_players)
                self.read_section(save_file, "Exit", self.load_exit)
        except FileNotFoundError:
            print("Save game file not found")

    def read_section(self, file, header, loader):
        section = ""
        for line in file:
            if line.strip() == f"{header}:":
                section = header.lower()
            else:
                setattr(self, section, loader(line.strip()))

    def get_steps(self):
        return len(self.players)
