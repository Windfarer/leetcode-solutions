class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid[0])
        h = len(grid)
        result = 0
        x = y = 0
        for x in xrange(w):
            for y in xrange(h):
                if grid[y][x] == 0:
                    n = 0
                else:    
                    n = 4
                    if y-1 >= 0 and grid[y-1][x] == 1:
                        n -= 1
                    if y+1 < h and grid[y+1][x] == 1:
                        n -= 1
                    if x-1 >= 0 and grid[y][x-1] == 1:
                        n -= 1
                    if x+1 < w and grid[y][x+1] == 1:
                        n -= 1
                    result += n
        return result
        
