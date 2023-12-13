class Board:
    def __init__(self):
        
        # --- Initializing variables ---
        self.players = []
        self.board = [[' ' for i in range(16)] for j in range(12)]
        self.exit = None # initialized as none as the exit only holds a single coordinate value -> best practice from code examples I've seen
        self.escaped_robots = 0
        self.dead_robots = 0
        self.steps = 0
        player_rows = 0
        error_printed = False

        # --- Defining File Paths ---
        map_path = "map.txt"
        players_path = "players.txt"
        exit_path = "exit.txt"
        self.user_data_path = "USR-DATA.txt" # save file name taken from TLOU P1 lol

        # --- File Reading using with statements to handle exceptions easier ---

        # Reading MAP file and creating board using file
        try:
            with open(map_path, 'r') as file:
                for row, line in enumerate(file):
                    line = line.strip("\n")
                    for col, symbol in enumerate(line):
                        if symbol == '#':
                            self.board[row][col] = '#'
                        else:
                            self.board[row][col] = ' '
        except:
            print("Error reading map file!")

        # Reading PLAYERS file and creating player list using file
        try:
            with open(players_path, 'r') as file:
                for line in file:
                    player_rows += 1
                    line = line.strip("\n")
                    row, col = map(int, line.split(' ')) # learning all about built-in python functions lol
                    if player_rows > 4 and not error_printed: # checking if player file is in valid format
                        print("File is in invalid format")
                        error_printed = True
                    else:
                        self.players.append((row, col))
        except:
            print("Error reading players file!")

        # Reading EXIT file and creating exit coordinate using file
        try:
            with open(exit_path, 'r') as file:
                line = file.readline()
                line = line.strip("\n")
                row, col = map(int, line.split(' '))
                if row < 0 or col < 0 or col >= len(self.board[0]):
                    print("File is in invalid format")
                else:
                    self.exit = (row, col)
        except:
            print("Error reading exit file!")



    def get_board(self):
        # --- Initalizes board with players and exit placed ---
        for players in self.players:
            row, col = players # tuple unpacking
            self.board[row][col] = 'P'

        if self.exit:
            exit_row, exit_col = self.exit
            self.board[exit_row][exit_col] = 'E'

        return self.board               



    def update(self, direction):
        # --- Initializing variables ---
        before_positions = self.players.copy() # Don't know if copy is necessary but don't wanna break anything
        after_positions = []
        max_row = len(self.board) - 1
        max_col = len(self.board[0]) - 1

        # Clearing old player positions
        for player_row, player_col in before_positions:
            self.board[player_row][player_col] = ' '

        tentative_positions = [] # List to store player positions before collision check

        # --- Calculating movement ---
        for player_row, player_col in before_positions:
            if direction == "U":
                new_row, new_col = max(player_row - 1, 0), player_col
            elif direction == "D":
                new_row, new_col = min(player_row + 1, max_row), player_col
            elif direction == "L":
                new_row, new_col = player_row, max(player_col - 1, 0)
            elif direction == "R":
                new_row, new_col = player_row, min(player_col + 1, max_col)

            tentative_positions.append((new_row, new_col))  # Add to tentative positions

        # --- Check for collisions and ensure moves are valid ---
        for i, (new_row, new_col) in enumerate(tentative_positions):
            if (new_row, new_col) == self.exit:
                self.escaped_robots += 1 # increments when robot reaches exit
            elif self.board[new_row][new_col] == '#': 
                self.dead_robots += 1 # increments when robot hits wall
            elif tentative_positions.count((new_row, new_col)) > 1:
                return # if collision is detected, no movement is made
            else:
                after_positions.append((new_row, new_col))

        self.players = after_positions # final player positions per game 'tick'
        self.steps += 1


    

    def get_state(self):
        # --- Returns the current state of the game ---
        if not self.players:
            if self.escaped_robots and self.dead_robots:
                return 3  # Did some robots escape, and some died?
            elif self.escaped_robots:
                return 1  # Did all players escape?
            else:
                return 2  # Did all players die?
        return 0  # Game is still ongoing  


       
    def save_game(self):
        # --- Saves the entire current state of the game in a single file ---
        try:
            with open(self.user_data_path, 'w') as file: 
                for row in self.board:
                    file.write(''.join(row) + '\n') # writing the board to the file

                file.write(f"{self.escaped_robots} {self.dead_robots}\n") # writing the game state to the file
                file.write(f"{self.steps}") # writing the steps to the file

                print(f"Game saved successfully to {self.user_data_path}!") # log message

        except:
            print("Error saving user data!")



    def load_game(self):
        # --- Loads a previously saved state ---
        self.__init__() # Clearing the current state of the board

        try:
            with open(self.user_data_path, 'r') as file:
                lines = file.readlines()

                # Reading the board from the file
                self.board = [list(line[:16]) for line in lines[:-2]] 

                self.players = []

                for i, row in enumerate(self.board):
                    for j, cell in enumerate(row):
                        if cell == 'P':
                            self.players.append((i, j))
                        elif cell == 'E':
                            self.exit = (i, j)

                self.escaped_robots, self.dead_robots = map(int, lines[-2].strip().split()) # Reading the game state from the file

                self.steps = int(lines[-1].strip()) # Reading the steps from the file

                print(f"Game loaded successfully from {self.user_data_path}!") # log message

        except:
            print("Error loading user data!")

    def get_steps(self):
        return self.steps