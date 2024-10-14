class Solution:
    def searchMatrix(self, matrix, target) :
      left_row, right_row = 0, len(matrix) - 1

      while left_row <= right_row:
        mid_row = (right_row + left_row) // 2

        if target < matrix[mid_row][0]:
            right_row = mid_row - 1
        elif target > matrix[mid_row][-1]:
           left_row = mid_row = 1
        else: #it may be in this mid row, so do a binary search on this mid row.
           left_element, right_element = 0, len(matrix[mid_row]) - 1

           mid_element = (right_element + left_element) // 2

           if target == matrix[mid_row][mid_element]:
              return True
           elif target < matrix[mid_row][mid_element]:
              right_element = mid_element - 1
           elif target > matrix[mid_row][mid_element]:
              left_element = mid_element + 1

           return False
              
           
           

