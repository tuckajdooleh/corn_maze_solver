class Point:
  def __init__(self, x, y, parent):
    self.x = x
    self.y = y
    self.parent = parent
    self.key = str(x) + "," + str(y)