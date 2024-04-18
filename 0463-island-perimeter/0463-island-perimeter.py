class Solution:


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        current_pos_values = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                current_value = 4
                if grid[i][j] is 1:
                    if i - 1 >= 0:
                        current_value = current_value -1 if grid[i - 1][j] is 1 else current_value
                    if i + 1 < len(grid):
                        current_value = current_value -1 if grid[i + 1][j] is 1 else current_value
                    if j - 1 >= 0:
                        current_value = current_value -1 if grid[i][j-1] is 1 else current_value
                    if j + 1 < len(grid[i]):
                        current_value = current_value -1 if grid[i][j+1] is 1 else current_value

                    current_pos_values.append(current_value)

        return reduce(lambda x,y: x+y, current_pos_values)



