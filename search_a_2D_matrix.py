class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        ind = -1
        while l <= r:
            mid = (l + r) // 2
            if target in matrix[mid]:
                ind = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        if ind == -1:
            return False

        l = 0
        r = len(matrix[ind]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[ind][mid] == target:
                return True
            elif target < matrix[ind][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
