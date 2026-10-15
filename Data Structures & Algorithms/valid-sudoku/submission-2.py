class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterating through all the sublists of the board list
        # sublist -> row. If a sublist is valid. valid if all the elements in the list are !=
        # columns -> all the i^th element of each sublist. If all i^th element !=, column is correct
        #3x3 : 0//3 = 0, 1//3 = 0.3333 2//3=0.666   6//3 = 2 7//3 = 2.333 8//3 = 2.6666 
        rows = {}
        cols = {}
        boxes = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                element = board[i][j] 
                if element != '.':                            
                    if i not in rows: rows[i] = set()
                    if j not in cols: cols[j] = set()
                    if (i//3,j//3) not in boxes: boxes[(i//3, j//3)] = set()
                    if element not in rows[i] and element not in cols[j] and element not in boxes[(i//3, j//3)]:
                        rows[i].add(element)
                        cols[j].add(element)
                        boxes[(i//3, j//3)].add(element)
                    else:
                        return False
        return True
        