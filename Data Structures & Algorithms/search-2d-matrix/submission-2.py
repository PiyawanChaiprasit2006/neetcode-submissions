class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        total_len = (len(matrix) * len(matrix[0])) - 1

        left = 0
        right = total_len
        mid = (left + right) //2

        row = mid // len(matrix[0])
        col = mid % len(matrix[0])

        while left <= right:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

            mid = (left + right) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
        
        return False
                

        