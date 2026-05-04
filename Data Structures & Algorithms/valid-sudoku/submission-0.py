class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        subbox_dict = defaultdict(set)

        
        for i in range(9):
            for j in range(9):
                curr_num = board[i][j]
                if curr_num == ".":
                    continue
                if curr_num in row_dict[i] or curr_num in column_dict[j] or curr_num in subbox_dict[i//3, j//3]:
                    return False
                row_dict[i].add(curr_num)
                column_dict[j].add(curr_num)
                subbox_dict[i//3, j//3].add(curr_num)

        return True