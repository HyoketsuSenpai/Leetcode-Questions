class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.mat = [[0]*(len(matrix[0]) + 1)]

        for i in range(len(matrix)):
            self.mat.append([0])
            
            for j in range(len(matrix[0])):
                self.mat[i + 1].append(matrix[i][j] + self.mat[i + 1][j] + self.mat[i][j + 1] - self.mat[i][j])

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return  self.mat[row2 + 1][col2 + 1] - self.mat[row2 + 1][col1] - self.mat[row1][col2 + 1] +self.mat[row1][col1]
