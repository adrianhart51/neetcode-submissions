class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Each row in matrix is sorted in non-decreasing order.
        # The first integer of every row is greater than the last integer of the previous row.
        # 1 2 3
        # 4 5 6
        # 7 8 9
        # equal with
        # 1 2 3 4 5 6 7 8 9

        # can do two pointer instead of linear search
        # do two pointer in matrix

        # l m 3
        # r mx 6
        # 7 8 rx

        # how to determine the mid in the matrix
        # need to determine the row and col
        # row
        
        # val
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # idx
        # 0 1 2
        # 3 4 5
        # 6 7 8

        # from top to bottom multiplication
        # from left to right remainder

        # idx matrix
        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2

        # 7 -> 2,1
        # idx -> row, col
        # idx -> idx//m, idx % n

        # [1 ,3 ,5 ,7]
        # [10,11,16,20]
        # [23,30,34,60]

        # [l ,3 ,5 ,7]
        # [10,11,16,20]
        # [23,30,34,r]

        # idx matrix
        # 0,0 0,1 0,2 0,3
        # 1,0 1,1 1,2 1,3
        # 2,0 2,1 2,2 2,3

        def idxSequenceToVal(idx: int, matrix: List[List[int]]) -> int:
            n = len(matrix[0])
            row, col = idx // n, idx % n
            return matrix[row][col]

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = idxSequenceToVal(mid, matrix)
            if mid_val < target:
                # increment left
                left = mid + 1
            elif mid_val > target:
                # decrement right
                right = mid - 1
            else:
                # match return
                return True

        return False
        
        