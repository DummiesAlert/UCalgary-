class Board:
    def __init__(self):
        
        self.board = []
        self.players = []
        self.exit = []
        
        try:
            
            with open('map.txt', "r") as map_file:
                
                for line in map_file:
                    
                    row = []
                    
                    for char in line.strip():
                        
                        if char == "#":
                            
                            row.append("#")
                            
                        else:
                            
                            row.append(" ")
                            
                    self.board.append(row)
                    
        except FileNotFoundError:
            
            print("Map file not found")
        
        try:
            
            with open('players.txt', 'r') as players_file:
                
                for line in players_file:
                    
                    player_info = line.strip().split()
                    row = int(player_info[0])
                    col = int(player_info[1])
                    self.players.append((row, col))
                    
        except FileNotFoundError:
            
            print("Players file not found")
        
        try:
            
            with open('exit.txt', 'r') as exit_file:
                
                self.exit = tuple(map(int, exit_file.readline().strip().split()))
        
        except FileNotFoundError:
            
            print("Exit file not found")

    def get_board(self):
        
        # self.board.replace()
        
        return self.board
    
    def update(self, direction):
        
        directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }
        
        for i in range(len(self.players)):
            row, col = self.players[i]
            
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]
            
            if 0 <= new_row < len(self.board) and 0 <= new_col < len(self.board[0]):
                
                if self.board[new_row][new_col] == "#":
                    
                    self.players.pop(i)
                    
                elif (new_row, new_col) in self.players:
                    
                    continue #Remove 
                
                else:
                    
                    self.players[i] = (new_row, new_col)
                    
                    if (new_row, new_col) == self.exit:
                        
                        self.players.pop(i)
                        
            else:
                
                continue #Remove 
    
    def get_state(self):
        
        if len(self.players) == 0:
            
            return 1 if len(self.players) == 0 else 2
        
        elif len(self.players) == 0:
            
            return 2
        
        elif len(self.players) == 0:
            
            return 3
        
        else:
            
            return 0
    
    def save_game(self):
        
        try:
            
            with open("save_game.txt", "w") as save_file:
                
                save_file.write("Board:\n")
                
                for row in self.board:
                    
                    save_file.write("".join(row) + "\n")
                    
                save_file.write("Players:\n")
                
                for player in self.players:
                    
                    save_file.write(f"{player[0]} {player[1]}\n")
                    
                save_file.write("Exit:\n")
                save_file.write(f"{self.exit[0]} {self.exit[1]}\n")
                
        except:
            
            print("Error saving game")
    
    def load_game(self):
        
        try:
            
            with open("save_game.txt", "r") as save_file:
                
                section = ""
                
                for line in save_file:
                    
                    if line.strip() == "Board:":
                        
                        section = "board"
                        
                    elif line.strip() == "Players:":
                        
                        section = "players"
                        
                    elif line.strip() == "Exit:":
                        
                        section = "exit"
                        
                    else:
                        
                        if section == "board":
                            
                            self.board.append(list(line.strip()))
                            
                        elif section == "players":
                            
                            player_info = line.strip().split()
                            row = int(player_info[0])
                            col = int(player_info[1])
                            self.players.append((row, col))
                            
                        elif section == "exit":
                            
                            exit_info = line.strip().split()
                            row = int(exit_info[0])
                            col = int(exit_info[1])
                            self.exit = (row, col)
                            
        except FileNotFoundError:
            
            print("Save game file not found")
    
    def get_steps(self):
        
        return len(self.players)