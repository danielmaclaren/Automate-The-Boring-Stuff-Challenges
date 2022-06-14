from re import L

board = {'1h': 'bking', 
        '6c': 'wqueen', 
        '2g': 'bbishop', 
        '5h': 'bqueen', 
        '3e': 'wking'} 

count = {}

def isValidChessBoard(board):
    for v in board.values():

        count.setdefault(v, 0)
        count[v] = count[v] + 1

        for v in (v for v in board.values() if not v.startswith(('b', 'w'))):
            print(v, 'is the wrong colour')
            return False

        for v in (v for v in board.values() if not v.endswith(('king', 'queen', 'rook', 'bishop', 'knight', 'pawn'))):
            print(v, 'is the wrong piece')
            return False

    for k in board.keys():
        for k in (k for k in board.keys() if not k.endswith(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'))):
            print(k, 'does not contain the correct letter')
            return False
        
        for k in (k for k in board.keys() if not k.startswith(('1', '2', '3', '4', '5', '6', '7', '8'))):
            print(k, 'does not contain the correct number')
            return False

        for k in (k for k in board.keys() if not len(k) == 2):
            print(k, 'is not the correct length')
            return False

    for k, v in count.items():
        if (k == 'bking'  or k =='wking') and v <= 1:
            print('works 1')
        elif (k == 'bqueen' or k =='wqueen') and v <= 1:
            print('works 2')
        elif (k == 'brook'or k == 'wrook') and v <= 2:
            print('works 3')
        elif (k == 'bknight' or k == 'wknight') and v <= 2:
            print('works 4')
        elif (k == 'bbishop' or k == 'wbishop') and v <= 2:
            print('works 5')
        elif (k == 'bpawn' or k == 'wpawn') and v <= 6:
            print('works 6')
        else: 
            return False

isValidChessBoard(board)