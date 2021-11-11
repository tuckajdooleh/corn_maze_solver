class Point:
  def __init__(self, x, y, parent):
    self.x = x
    self.y = y
    self.parent = parent
    self.key = str(x) + "," + str(y)
    self.f = 0
    self.g = 0
    self.h = 0