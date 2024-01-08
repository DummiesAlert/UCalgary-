"""Author: Zhuo Xi Hong 
   UCID: 30213715
   Last Modified: Dec/13/2023

Prompt: Write a mini robot game

Sources:  

    - map(): https://www.w3schools.com/python/ref_func_map.asp
        - Changes all things into an iterable without using a loop (yaaaa)
    - enumerate(): https://www.w3schools.com/python/ref_func_enumerate.asp#:~:text=The%20enumerate()%20function%20takes,key%20of%20the%20enumerate%20object.
        - Reads List and Checks Them Values, mostly
    - lists(): https://www.w3schools.com/python/python_lists_methods.asp
        
    Tutorial:
    
        - TA Naman: Helped with managing the gameFile imports and several minor changes.
        
            - def update(self, direction): with directions if else and controls(Around Lines 135-176)
            - def load_game, fixed some loading, but not work.

"""

class Board:
    
    def __init__(self): 
        
        #Define Variables
        self.players = []
        
        #Check If Board Meets The 12 Col and 16 Row
        self.board = [[' ' 
                       
                       for i in range(16)] 
                       for j in range(12)]
        
        self.exit = None #Manage One Exit Coordinate of the Robot
        
        self.robotsExited = 0
        self.robotsCollided = 0
        self.steps = 0
        
        playerPosition = 0
        errorCheck = False

        #Try/Except for 'map.txt' and Create self.board
        try:
            
            with open('map.txt', 'r') as gameFile:
                
                for row, line in enumerate(gameFile):
                    
                    line = line.strip("\n")
                    
                    for col, char in enumerate(line):
                        
                        if char == '#':
                            
                            self.board[row][col] = '#'
                            
                        else:
                            
                            self.board[row][col] = ' '
                            
        except FileNotFoundError:
            
            print("Error Reading Map File!")

        #Try/Except for 'players.txt' and Error Check
        try:
            
            with open('players.txt', 'r') as gameFile:
                
                for line in gameFile:
                    
                    playerPosition += 1
                    line = line.strip("\n")
                    row, col = map(int, line.split(' '))
                    
                    if playerPosition > 4 and not errorCheck: #File Checking
                        
                        print("File Format is Invalid!")
                        errorCheck = True
                        
                    else:
                        
                        self.players.append((row, col))

        except FileNotFoundError:
            
            print("Error Reading Players File!")
        
        #Try/Except for 'exit.txt' and Error Check
        try:
            
            with open('exit.txt', 'r') as gameFile:
                
                line = gameFile.readline()
                line = line.strip("\n")
                row, col = map(int, line.split(' '))
                
                if row < 0 or col < 0 or col >= len(self.board[0]): #Check If on Board
                    
                    print("File Format is Invalid!")   
                                     
                else:
                    
                    self.exit = (row, col)
                    
        except FileNotFoundError:
            
            print("Error Reading Exit File!")

    def get_board(self):
        
        for players in self.players:
            
            #Unpack Tuple in Players
            row, col = players
            self.board[row][col] = 'P'

        if self.exit:
            
            #Clean Up Exit
            exitRow, exitCol = self.exit
            self.board[exitRow][exitCol] = 'E'

        return self.board               

    def update(self, direction):
        
        #List of Where the Players Are
        positionPrev = list(self.players)
        positionAfter = []
        
        #Determine the Length of the Board
        maxRow = len(self.board) - 1
        maxCol = len(self.board[0]) - 1

        #Refresh Game Board
        for playerRow, playerCol in positionPrev:
            
            self.board[playerRow][playerCol] = ' '

        #Position After Moving
        tentPositions = []

        #Create Direction Movement
        for playerRow, playerCol in positionPrev:
            
            if direction == "U": #Moves Player Up and Change the Row and Col of the Players
                
                    newRow, newCol = (playerRow - 1, playerCol) if playerRow > 0 else (0, playerCol) 
                    
            elif direction == "D": #Moves Player Down and Change the Row and Col of the Players
                
                    newRow, newCol = (playerRow + 1, playerCol) if playerRow + 1 < maxRow else (maxRow, playerCol)
                    
            elif direction == "L": #Moves Player Left and Change the Row and Col of the Players
                
                    newRow, newCol = (playerRow, playerCol - 1) if playerCol > 0 else (playerRow, 0)
                    
            elif direction == "R": #Moves Player Right and Change the Row and Col of the Players
                
                    newRow, newCol = (playerRow, playerCol + 1) if playerCol + 1 < maxCol else (playerRow, maxCol)

            #Make the Position to the New Position After Moving
            tentPositions.append((newRow, newCol))

        #Collision Management and Error Checking
        for i, (newRow, newCol) in enumerate(tentPositions): #List After Movement
            
            if (newRow, newCol) == self.exit: #Determine Players Exit Cords
                
                self.robotsExited += 1 #Exit Cords
                
            elif self.board[newRow][newCol] == '#': #Determine Players Collision Cords
                
                self.robotsCollided += 1 #Collision Cords
                
            elif tentPositions.count((newRow, newCol)) > 1:
                
                return #Collision, no return, no movement
            
            else:
                
                positionAfter.append((newRow, newCol)) #Determine Final Cords of the Players

        #Set Player Cords to the Final Cords 
        self.players = positionAfter
        self.steps += 1

    def get_state(self):

        #Find Robots and Player Positions
        if not self.players:
            
            if self.robotsExited:
                
                return 1  #All Escaped?
            
            elif self.robotsCollided:
                
                return 2  #All Died?
            
            elif self.robotsExited and self.robotsCollided:
                
                return 3  #Escaped and Not?
            
        return 0  #Game Not Over
     
    def save_game(self):

        #Save Game
        try:
            
            with open('load.txt', 'w') as gameFile: 
                
                for row in self.board:
                    
                    gameFile.write(''.join(row) + '\n') #Write Board Into load.txt 

                #Game Progress: Robots Exited, Collided and Amount of Steps
                gameFile.write(f"Robots Exited: {self.robotsExited}\nRobots Collided: {self.robotsCollided}\nSteps: {self.steps}\n")

                print(f"Game Saved Successfully to {'load.txt'}!")

        except FileNotFoundError:
            
            print("Error Saving User Data!")

    def load_game(self):
        
        try:
           
            #Start Game
            self.__init__()

            with open('load.txt', 'r') as gameFile:
                lines = gameFile.readlines()

                #Read the Board Info and Strip
                self.board = [list(line.strip('\n')) for line in lines[:-2]]

                #Read Game Info
                self.robotsExited, self.robotsCollided = map(int, lines[-2].split())

                #Read Steps
                self.steps = int(lines[-1])
                #self.steps = float(lines[-2])
                #self.steps = float(lines[-2:-1])

                print(f"Game Loaded Successfully From {'load.txt'}!")

        except FileNotFoundError:
            
            print("Error Loading Game Data")

    #Return Itself and Determine the Steps Used
    def get_steps(self):
        
        return self.steps 