
def attack(r1, c1, r2, c2):
    if r1 == r2 or c1 == c2 :
        return True
    x = r2 - r1
    if c1-c2 == x or c2-c1 == x:
        return True
    else:
        return False

def draw(board, board_size):
    """ [[],[],[]]"""
    # board.sort(key=itemgetter(0,1))
    # x, y = board[-1]
    # board_size = max(x,y)
    # board_size = len(board)

    # print(f'chees board is: {board}')
    # print(f'chess board size is:{board_size}')

    queen = '│ \N{black chess queen} '
    square = '│   '
    line = '│'
    
    for i in range(0,board_size):
        if i == 0:
            print('┌───' + '┬───' * (board_size -1) + '┐')
        else:
            print('├───' + '┼───' * (board_size -1) + '┤')
        for j in range(0,board_size):
            if [i,j]  in board:

                print(queen,sep='',end='')
            if [i,j] not in board:
                print(square,sep='',end='')
        print(line)
    print('└───' + '┴───' * (board_size -1) + '┘')




class queen:
    BOARD = []
    Q_COUNT = 4
    def __init__(self, neighboar):
        self.neighboar = neighboar

        self.row = len(queen.BOARD)
        self.column = -1
        self.locat()
        print(f'>>>queen#{self.row} initiated')

    def locat(self):

        if self.row == 0 :
            self.column = self.column + 1
            queen.BOARD.append([self.row, self.column])
            draw(queen.BOARD,self.Q_COUNT)
            return 1
        
        for i in range(self.column+1,queen.Q_COUNT):
            attack_count = 0
            for x,y in queen.BOARD:
                attack_count += attack(self.row, i, x, y)
            if attack_count == 0:
                queen.BOARD.append([self.row,i])
                self.column = i
                
                print(f'*** queen#{self.row}: in place#{i} i am confortable')
                draw(queen.BOARD,self.Q_COUNT)
                return 1
            else:
                print(f'!!!  queen#{self.row}: in place#{i} i am in attack')

        self.column = -1
        queen.BOARD.pop()
        self.neighboar.locat()
        return self.locat()

print(0)
q0 = queen(None)
print(1)
q1 = queen(q0)
print(2)
q2 = queen(q1)
print(3)
q3 = queen(q2)

print("________________")
draw(queen.BOARD, 4)
print(queen.BOARD)
            


        

