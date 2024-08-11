class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic1={}
        dic2={}
        dic3={}
        liste=[0,0]
        for i in range(9):
            for j in range(9):
                if board[i][j] in dic1 and board[i][j] != "." :
                    return False
                if board[j][i] in dic2 and board[j][i] != ".":
                    return False
                if (board[liste[0]][liste[1]] in dic3) and board[liste[0]][liste[1]] != ".":
                    return False
                dic1[board[i][j]]=0
                dic2[board[j][i]]=0
                dic3[board[liste[0]][liste[1]]]=0
                if (liste[0]==2 or liste[0]==5 or liste[0]==8)and (liste[1]==2 or liste[1]==5):
                    liste[0]=liste[0]-2
                    liste[1]=liste[1]+1
                elif (liste[0]==2 or liste[0]==5 or liste[0]==8)and liste[1]==8:
                    liste[0]=liste[0]+1
                    liste[1]=0
                elif liste[1]==2 or liste[1]==5 or liste[1]==8:
                    liste[1]=liste[1]-2
                    liste[0]=liste[0]+1 
                else:  
                    liste[1]=liste[1]+1
            dic1={}
            dic2={}
            dic3={}
        return True   