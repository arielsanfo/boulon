class MAtrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.table: int[self.x][self.y] = []
    
    def is_inversible( self) -> bool:
        if self.det() != 0:
            return True
        return False

    def det(self) -> int:
        result = 0
        for i in range(self.x):
            for j in range(self.y):
                result += self.table[i][j]
        return result