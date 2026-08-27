class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            row_set = set()
            for j in range(cols):
                val = board[i][j]
                if val == ".":
                    continue
                
                if val in row_set:
                    return False

                row_set.add(board[i][j])

        for j in range(cols):
            col_set = set()
            for i in range(rows):
                val = board[i][j]
                if val == ".":
                    continue
                
                if val in col_set:
                    return False
                col_set.add(board[i][j])
        

        for box_r in range(0, rows, 3):
            for box_c in range(0, cols, 3):
                seen = set()

                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        
                        if val in seen:
                            return False
                        
                        seen.add(val)
                        
        return True

