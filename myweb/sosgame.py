class SOS():
    def __init__(self):
        '''
        to save the position value,
        made a dicitonary with position as keys and O/X as values
        '''
        ''' The table
                             A1   A2     A3    A4    A5     A6
                             B1   B2     B3    B4    B5     B6
                             C1   C2     C3    C4    C5     C6
                             D1   D2     D3    D4    D5     D6
                             E1   E2     E3    E4    E5     E6
                             F1   F2     F3    F4    F5     F6'''
        ''' To save S and Os'''
        self.count = 0 #to find the index of the point we want
        self.p1 = 0 #points of  player1 will be stored here
        self.p2 = 0 #points for player2 will be stored here
        self.positions = {"A1" : " ",
                          "A2" : " ",
                          "A3" : " ",
                          "A4" : " ",
                          "A5" : " ",
                          "A6" : " ",
                          "B1" : " ",
                          "B2" : " ",
                          "B3" : " ",
                          "B4" : " ",
                          "B5" : " ",
                          "B6" : " ",
                          "C1" : " ",
                          "C2" : " ",
                          "C3" : " ",
                          "C4" : " ",
                          "C5" : " ",
                          "C6" : " ",
                          "D1" : " ",
                          "D2" : " ",
                          "D3" : " ",
                          "D4" : " ",
                          "D5" : " ",
                          "D6" : " ",
                          "E1" : " ",
                          "E2" : " ",
                          "E3" : " ",
                          "E4" : " ",
                          "E5" : " ",
                          "E6" : " ",
                          "F1" : " ",
                          "F2" : " ",
                          "F3" : " ",
                          "F4" : " ",
                          "F5" : " ",
                          "F6" : " "
                          }
        self.positions_value = {"A1" : 0,
                                "A2" : 1,
                                "A3" : 2,
                                "A4" : 3,
                                "A5" : 4,
                                "A6" : 5,
                                "B1" : 6,
                                "B2" : 7,
                                "B3" : 8,
                                "B4" : 9,
                                "B5" : 10,
                                "B6" : 11,
                                "C1" : 12,
                                "C2" : 13,
                                "C3" : 14,
                                "C4" : 15,
                                "C5" : 16,
                                "C6" : 17,
                                "D1" : 18,
                                "D2" : 19,
                                "D3" : 20,
                                "D4" : 21,
                                "D5" : 22,
                                "D6" : 23,
                                "E1" : 24,
                                "E2" : 25,
                                "E3" : 26,
                                "E4" : 27,
                                "E5" : 28,
                                "E6" : 29,
                                "F1" : 30,
                                "F2" : 31,
                                "F3" : 32,
                                "F4" : 33,
                                "F5" : 34,
                                "F6" : 35
                                } 

        self.p = list(self.positions.keys())
        
    def basic(self): 
        self.status = self.positions.values()   
        print('''\t %s | %s | %s | %s | %s | %s \n\t --+---+---+---+---+---\n\t %s | %s | %s | %s | %s | %s \n\t --+---+---+---+---+---\n\t %s | %s | %s | %s | %s | %s \n\t --+---+---+---+---+---\n\t %s | %s | %s | %s | %s | %s \n\t --+---+---+---+---+---\n\t %s | %s | %s | %s | %s | %s \n\t --+---+---+---+---+---\n\t %s | %s | %s | %s | %s | %s \n\t --+---+---+---+---+---\n''' 
    % tuple(self.status))
    def ready(self):
        '''
        ready for game with game position info
        '''
        print("**** Welcome to SOS Game! ****")
        self.status = ("A1", "A2", "A3", "A4", "A5", "A6", "B1", "B2", "B3", "B4", "B5", "B6", "C1", "C2", "C3", "C4", "C5", "C6", "D1", "D2", "D3", "D4", "D5", "D6", "E1", "E2", "E3", "E4", "E5", "E6", "F1", "F2", "F3", "F4", "F5", "F6",)
        print('''\t %s | %s | %s | %s | %s | %s \n\t ---+----+----+----+----+---\n\t %s | %s | %s | %s | %s | %s \n\t ---+----+----+----+----+---\n\t %s | %s | %s | %s | %s | %s \n\t ---+----+----+----+----+---\n\t %s | %s | %s | %s | %s | %s \n\t ---+----+----+----+----+---\n\t %s | %s | %s | %s | %s | %s \n\t ---+----+----+----+----+---\n\t %s | %s | %s | %s | %s | %s \n\t ---+----+----+----+----+---\n''' 
    % (self.status))
    def player1(self):
        print("Player 1 take your turn")
        while True:
            point = input("Enter a postion to fill: ").upper()
            letter = input("fill with S or O: ").upper()
            if letter == "S" or letter =="O": #condition where there cant be any other alphabet
                if point in self.positions.keys():
                    if self.positions[str(point)] == " ":
                        self.positions[str(point)] = letter
                        if letter == "S":
                            self.checkS("player1",point)
                        if letter == "O":
                            self.checkO("player1",point)
                        self.basic()
                        break
                    else:
                        print("This position is filled. \nPlease put another position.")
                        continue
                else:
                    print("You put the wrong position.")
                    continue
            else:
                print("you put wrong alphatbet")
                continue 

    def player2(self):
        print("Player 2 take your turn")
        while True:
            point2 = input("Enter a postion to fill: ").upper()
            letter2 = input("fill with S or O: ").upper()
            if letter2 == "S" or letter2 =="O": #condition where there cant be any other alphabet
                if point2 in self.positions.keys():
                    if self.positions[str(point2)] == " ":
                        self.positions[str(point2)] = letter2
                        if letter2 == "S":
                            self.checkS("player2",point2)
                        if letter2 == "O":
                            self.checkO("player2",point2)
                        self.basic()
                        break
                    else:
                        print("This position is filled. \nPlease put another position.")
                        continue
                else:
                    print("You put the wrong position.")
                    continue
            else:
                print("you put wrong alphatbet")
                continue 
            
                

    def play(self):
        print("\n Let's start the game")
        for i in range(1,37):
            print("Player 1 points:",self.p1)
            print("Player 2 points:",self.p2)
            if i%2 == 0:
                self.player2() #players are taking their turns
            else:
                self.player1() #player is taking their turns
        print('player1 points are: ',self.p1)
        print('player2 points are: ',self.p2)
        if self.p1 > self.p2:
            print("Player 1 has won")
        elif self.p2> self.p1:
            print("Player 2 has won")
        else:
            print("Game ended in a tie")

    def checkS(self,player,key):
        index = self.positions_value[key] #taking value
        self.p = list(self.positions.keys())
        #first check row.r
        #row 1                                                          
        if index < 5: #row_right
            a = self.positions[self.p[index+1]]
            b = self.positions[self.p[index+2]]
            if  a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                    print(self.p1)
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move

        if index >1 and index < 6: #row_left
            if self.positions[self.p[index-1]] == "O" and self.positions[self.p[index-2]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 2
        if index > 5 and index < 10: #row_right
            a = self.positions[self.p[index+1]]
            b = self.positions[self.p[index+2]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move

        if index >8 and index < 12: #row_left
            if self.positions[self.p[index-1]] == "O" and self.positions[self.p[index-2]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row3
        if index > 11 and index <16: #row_right
            a = self.positions[self.p[index+1]]
            b = self.positions[self.p[index+2]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move

        if index > 15 and index < 18: #row_left
            if self.positions[self.p[index-1]] == "O" and self.positions[self.p[index-2]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 4
        if index > 17 and index < 22: #row_right
            a = self.positions[self.p[index+1]]
            b = self.positions[self.p[index+2]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move

        if index > 19 and index < 24: #row_left
            if self.positions[self.p[index-1]] == "O" and self.positions[self.p[index-2]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 5
        if index > 24 and index < 28: #row_right
            a = self.positions[self.p[index+1]]
            b = self.positions[self.p[index+2]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move

        if index > 25 and index < 30: #row_left
            if self.positions[self.p[index-1]] == "O" and self.positions[self.p[index-2]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 6
        if index > 29 and index < 34: #row_right
            a = self.positions[self.p[index+1]]
            b = self.positions[self.p[index+2]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move

        if index > 31 and index < 36: #row_left
            if self.positions[self.p[index-1]] == "O" and self.positions[self.p[index-2]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #now we check for down
        if index<6: #0 to 5 
            a = self.positions[self.p[index+6]]
            b = self.positions[self.p[index+12]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index >5 and index <12: #6 -- 11 
            a = self.positions[self.p[index+6]]
            b = self.positions[self.p[index+12]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index >11 and index <18: #12 -- 17 
            a = self.positions[self.p[index+6]]
            b = self.positions[self.p[index+12]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index >17 and index <24: #18 -- 23 
            a = self.positions[self.p[index+6]]
            b = self.positions[self.p[index+12]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #now we check for column up
        if index >11 and index <18: #12 -- 17 
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index-12]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index >17 and index <24: #18 -- 23 
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index-12]]
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index >23 and index <30: #24 -- 29 
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index-12]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #check for diagonal down right
        if index <4:
            a = self.positions[self.p[index+7]]
            b = self.positions[self.p[index+14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>5 and index<10:
            a = self.positions[self.p[index+7]]
            b = self.positions[self.p[index+14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>11 and index <16:
            a = self.positions[self.p[index+7]]
            b = self.positions[self.p[index+14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>17 and index<22:
            a = self.positions[self.p[index+7]]
            b = self.positions[self.p[index+14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #check diagonal left up
        if index>13 and index<18:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index-14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>21 and index<24:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index-14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>25 and index<30:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index-14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>31 and index<36:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index-14]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #check diagonal for right up
        if index>11 and index<16:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index-10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>17 and index<22:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index-10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>23 and index<28:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index-10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>29 and index<34:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index-10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        
        #check for diagonal left down
        if index>1 and index<6:
            a = self.positions[self.p[index+5]]
            b = self.positions[self.p[index+10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>7 and index<12:
            a = self.positions[self.p[index+5]]
            b = self.positions[self.p[index+10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>13 and index<18:
            a = self.positions[self.p[index+5]]
            b = self.positions[self.p[index+10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        if index>19 and index<24:
            a = self.positions[self.p[index+5]]
            b = self.positions[self.p[index+10]] 
            if a == "O" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
                    
        
            
        
    def checkO(self,player,key):
        index = self.positions_value[key] #taking value
        self.p = list(self.positions.keys())
        #row 1                                                          
        if index > 0 and index < 5: #row_check
            if self.positions[self.p[index-1]] == "S" and self.positions[self.p[index+1]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 2
        if index > 6 and index < 11: #row_right
            if self.positions[self.p[index-1]] == "S" and self.positions[self.p[index+1]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row3
        if index > 12 and index <17: #row_right
            if self.positions[self.p[index-1]] == "S" and self.positions[self.p[index+1]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 4
        if index > 18 and index < 23: #row_right
            if self.positions[self.p[index-1]] == "S" and self.positions[self.p[index+1]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 5
        if index > 24 and index < 29: #row_right
            if self.positions[self.p[index-1]] == "S" and self.positions[self.p[index+1]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #row 6
        if index > 30 and index < 35: #row_right
            if self.positions[self.p[index-1]] == "S" and self.positions[self.p[index+1]] == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1 #if it were player two's move
        #now we check column for O
        if index>5 and index <12:
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index+6]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index>11 and index<18:
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index+6]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index>17 and index <24:
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index+6]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index>23 and index <30:
            a = self.positions[self.p[index-6]]
            b = self.positions[self.p[index+6]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
            
        #now we check diagonals  (first row is not imp)
        if index > 6 and index < 11:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index+7]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index > 12 and index < 17:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index+7]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index > 18 and index < 23:
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index+7]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index >24 and index < 29: 
            a = self.positions[self.p[index-7]]
            b = self.positions[self.p[index+7]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        #now check for diagnal right to left
        if index > 6 and index < 11:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index+5]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index > 12 and index < 17:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index+5]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index > 18 and index < 23:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index+5]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
        if index > 24 and index < 29:
            a = self.positions[self.p[index-5]]
            b = self.positions[self.p[index+5]]
            if a == "S" and b == "S":
                if player == "player1":
                    self.p1 = self.p1 + 1 #if it were player one's move
                elif player == "player2":
                    self.p2 = self.p2+ 1
def main():
    a = SOS()
    a.ready()
    c = True
    while c== True:
        answer = input("Do you wanna play? yes or no? ").lower()
        if answer == "yes":
            a.play()
        elif answer == "no":
            print("Bye!")
            break
        else:
            print("input invalid")
main()
