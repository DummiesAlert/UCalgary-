# class Board:
    
#     def __init__(self):
        
#         try:
            
#             # Read map file
#             with open("map.txt", "r") as map_file:
                
#                 self.board = [list(line.strip()) for line in map_file]

#                 # Check if the map file has the correct size (12 rows, 16 columns)
#                 if len(self.board) != 12 or any(len(row) != 16 for row in self.board):
                    
#                     print("Invalid map file. Map must have 12 rows and 16 columns.")
                    
#                     # If the map file is invalid, create an empty grid
#                     self.board = [[" " for _ in range(16)] for _ in range(12)]

#         except FileNotFoundError:
            
#             print("Map file not found. Creating an empty grid.")
#             self.board = [[" " for _ in range(16)] for _ in range(12)]

#         try:
            
#             # Read players file
#             with open("players.txt", "r") as players_file:
                
#                 self.players = [tuple(map(int, line.strip().split())) for line in players_file]

#                 # Check the number of players
#                 if not (1 <= len(self.players) <= 4):
                    
#                     print("Invalid players file. It should contain 1 to 4 player positions.")
                    
#                     # If the players file is invalid, create an empty players list
#                     self.players = []
                    
#                 else:
                    
#                     print("Players loaded successfully.")
#                     print("Players:", self.players)
                    
#                     # Update the game grid with player positions
#                     for row, col in self.players:
#                         self.board[row][col] = "P"

#         except FileNotFoundError:
            
#             print("Players file not found. Creating an empty players list.")
            
#             self.players = []

#         try:
            
#             # Read exit file
#             with open("exit.txt", "r") as exit_file:
                
#                 exit_position = tuple(map(int, exit_file.readline().strip().split()))

#                 # Check if there is exactly one exit position
#                 if len(exit_position) != 2:
                    
#                     print("Invalid exit file. It should contain exactly 1 exit position.")
#                     # If the exit file is invalid, set the exit position to (0, 0)
                    
#                     exit_position = (0, 0)
                    
#                 else:
                    
#                     print("Exit loaded successfully.")
#                     print("Exit Position:", exit_position)
                    
#                     # Update the game grid with the exit position
#                     self.board[exit_position[0]][exit_position[1]] = "E"

#                 self.exit_position = exit_position

#         except FileNotFoundError:
            
#             print("Exit file not found. Setting the exit position to (0, 0).")
#             self.exit_position = (0, 0)

#     def get_board(self):
        
#         return self.board

#     def get_players(self):
        
#         return self.players

#     def get_exit_position(self):
        
#         return self.exit_position

#     def update(self, direction):
        
#         # Create a copy of the current game grid to avoid modifying the original list
#         new_game_grid = [list(row) for row in self.board]

#         # Define movement offsets based on the direction
#         move_offsets = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

#         players_disappeared = 0
#         players_at_exit = 0

#         for i, (row, col) in enumerate(self.players):
#             # Calculate the new position based on the direction
#             new_row = row + move_offsets[direction][0]
#             new_col = col + move_offsets[direction][1]

#             # Check if the new position is within the bounds of the board
#             if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[0]):
                
#                 # Check if the target position is an empty space, wall, or exit
#                 if self.board[new_row][new_col] == " ":
                    
#                     new_game_grid[row][col] = " "  # Clear the current position
#                     new_game_grid[new_row][new_col] = "P"  # Set the new position
                    
#                     # Update players with the new position
#                     self.players[i] = (new_row, new_col)
                    
#                 elif self.board[new_row][new_col] == "#":
                    
#                     # If the target position is a wall, the player disappears
#                     new_game_grid[row][col] = " "  # Clear the current position
                    
#                     # Update players without adding the player back to the new position
#                     self.players[i] = (-1, -1)  # Mark the player as disappeared
                
#                 elif self.board[new_row][new_col] == "E":
                    
#                     # If the target position is an exit, the player disappears
#                     new_game_grid[row][col] = " "  # Clear the current position
                    
#                     # Update players without adding the player back to the new position
#                     self.players[i] = (-1, -1)  # Mark the player as disappeared
#                     players_at_exit += 1

#         # Update the game grid with the new positions
#         self.board = new_game_grid

#     def get_state(self):
        
#         players_disappeared = 0
#         players_at_exit = 0

#         for row, col in self.players:
            
#             # Check if the player has moved into a wall
#             if self.board[row][col] == '#':
                
#                 players_disappeared += 1
                
#             # Check if the player has moved into the exit
#             elif self.board[row][col] == 'E':
                
#                 players_disappeared += 1
#                 players_at_exit += 1

#         if players_at_exit == len(self.players):
            
#             print("Debug: All robots moved into the exit.")
#             return 2  # You win!

#         if players_disappeared == len(self.players):
            
#             print("Debug: All robots hit the wall or moved into the exit.")
#             return 1  # You lost.

#         if players_at_exit > 0 and players_disappeared > 0:
            
#             print("Debug: Some robots moved into the exit, and others hit the wall.")
#             return 3  # You could do better!

#         # Game is not over yet
#         print("Debug: Game is not over yet.")
#         print('players disappeared', players_disappeared)
#         print('players at exit', players_at_exit)
#         return 0

#     def get_state(self):
        
#         players_disappeared = 0
#         players_at_exit = 0

#         for row, col in self.players:
            
#             # Check if the player has moved into a wall
#             if self.board[row][col] == '#':
                
#                 players_disappeared += 1
                
#             # Check if the player has moved into the exit
#             elif self.board[row][col] == 'E':
                
#                 players_disappeared += 1
#                 players_at_exit += 1

#         if players_at_exit == len(self.players):
            
#             print("Debug: All robots moved into the exit.")
#             return 2  # You win!

#         if players_disappeared == len(self.players):
            
#             print("Debug: All robots hit the wall or moved into the exit.")
#             return 1  # You lost.

#         if players_at_exit > 0 and players_disappeared > 0:
            
#             print("Debug: Some robots moved into the exit, and others hit the wall.")
#             return 3  # You could do better!

#         # Game is not over yet
#         print("Debug: Game is not over yet.")
#         print('players disappeared', players_disappeared)
#         print('players at exit', players_at_exit)
#         return 0

#     def save_game(self):
        
#         return

#     def load_game(self):
        
#         return

#     def get_steps(self):
        
#         return self.steps

class Board:
    def __init__(self):
        try:
            with open("map.txt", "r") as map_file:
                self.board = [list(line.strip()) for line in map_file]

                if len(self.board) != 12 or any(len(row) != 16 for row in self.board):
                    print("Invalid map file. Map must have 12 rows and 16 columns.")
                    self.board = [[" " for _ in range(16)] for _ in range(12)]
        except FileNotFoundError:
            print("Map file not found. Creating an empty grid.")
            self.board = [[" " for _ in range(16)] for _ in range(12)]

        try:
            with open("players.txt", "r") as players_file:
                self.players = [tuple(map(int, line.strip().split())) for line in players_file]

                if not (1 <= len(self.players) <= 4):
                    print("Invalid players file. It should contain 1 to 4 player positions.")
                    self.players = []
                else:
                    print("Players loaded successfully.")
                    print("Players:", self.players)

                    for row, col in self.players:
                        self.board[row][col] = "P"
        except FileNotFoundError:
            print("Players file not found. Creating an empty players list.")
            self.players = []

        try:
            with open("exit.txt", "r") as exit_file:
                exit_position = tuple(map(int, exit_file.readline().strip().split()))

                if len(exit_position) != 2:
                    print("Invalid exit file. It should contain exactly 1 exit position.")
                    exit_position = (0, 0)
                else:
                    print("Exit loaded successfully.")
                    print("Exit Position:", exit_position)

                    self.board[exit_position[0]][exit_position[1]] = "E"

                self.exit_position = exit_position
        except FileNotFoundError:
            print("Exit file not found. Setting the exit position to (0, 0).")
            self.exit_position = (0, 0)

    def get_board(self):
        return self.board

    def get_players(self):
        return self.players

    def get_exit_position(self):
        return self.exit_position

    def update(self, direction):
        new_game_grid = [list(row) for row in self.board]
        
        move_offsets = {
            
            "U": (-1, 0), 
            "D": (1, 0), 
            "L": (0, -1), 
            "R": (0, 1) }
        
        players_disappeared = 0
        players_at_exit = 0

        for i, (row, col) in enumerate(self.players):
            new_row = row + move_offsets[direction][0]
            new_col = col + move_offsets[direction][1]

            if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[0]):
                if self.board[new_row][new_col] == " ":
                    new_game_grid[row][col] = " "
                    new_game_grid[new_row][new_col] = "P"
                    self.players[i] = (new_row, new_col)
                elif self.board[new_row][new_col] == "#":
                    new_game_grid[row][col] = " "
                    self.players[i] = (-1, -1)
                    players_disappeared += 1
                elif self.board[new_row][new_col] == "E":
                    new_game_grid[row][col] = " "
                    self.players[i] = (-1, -1)
                    players_disappeared += 1
                    players_at_exit += 1

        self.board = new_game_grid

    def get_state(self):
        players_disappeared = 0
        players_at_exit = 0

        for row, col in self.players:
            if self.board[row][col] == '#':
                players_disappeared += 1
            elif self.board[row][col] == 'E':
                players_disappeared += 1
                players_at_exit += 1

        if players_at_exit == len(self.players):
            print("Debug: All robots moved into the exit.")
            return 2  # You win!

        if players_disappeared == len(self.players):
            print("Debug: All robots hit the wall or moved into the exit.")
            return 1  # You lost.

        if players_at_exit > 0 and players_disappeared > 0:
            print("Debug: Some robots moved into the exit, and others hit the wall.")
            return 3  # You could do better!

        print("Debug: Game is not over yet.")
        print('players disappeared', players_disappeared)
        print('players at exit', players_at_exit)
        return 0

    def save_game(self):
        return

    def load_game(self):
        return

    def get_steps(self):
        return self.steps