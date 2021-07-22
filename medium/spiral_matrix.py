'''
Spiral Matrix (https://leetcode.com/problems/spiral-matrix/)
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
[[1,2,3],
 [4,5,6],
 [7,8,9]]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

class Solution:
    def spiralOrder(self, snail_map: List[List[int]]) -> List[int]:
        '''
        Time: O(N): simply traversing the matrix
        Space: O(N): I don't technically use any space but I do replace the elements of the matrix so I would like to add a visited set to avoid mutating the matrix
                    which would make my solution O(N)
        '''
        # first off some edge cases
        if snail_map == [[]]:
            return []
        elif len(snail_map) == 1:
            return snail_map[0]
        n = len(snail_map)
        m = len(snail_map[0])
        deltas = [(1,0), (0,1), (-1,0), (0,-1)] # list of delta (x,y) pairs [right, down, left, up]. This is what I use to keep track of which way I am moving
        d_index = 0 # start off at the first delta which is going right
        result = [] # solution list
        current_x = 0
        current_y = 0
        while(snail_map[current_y][current_x] is not None):
            result.append(snail_map[current_y][current_x]) # append the value I am currently on
            snail_map[current_y][current_x] = None # mutation of the matrix. Can use a visited set instead
            new_x = current_x + deltas[d_index][0] # calculate what the next x,y would be based on what direction I am going in
            new_y = current_y + deltas[d_index][1]
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or snail_map[new_y][new_x] is None:
                # x or y out of bounds or next block is a none
                # need to turn
                d_index = (d_index + 1) % 4 # move my index to the next direction in my deltas list
                current_x += deltas[d_index][0] # move x,y in the new direction
                current_y += deltas[d_index][1]
            else:
                # keep going
                current_x = new_x # new_x and new_y are safe so I will use those as my next x,y
                current_y = new_y

        return result
        
