
class Position:
    def __init__(self, x_pos, y_pos) -> None:
        self.x = x_pos
        self.y = y_pos
    
    def getCoordinates(self):
        return (self.x, self.y)
    
    def updatePosition(self, d_x, d_y):
        self.x += d_x
        self.y += d_y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
