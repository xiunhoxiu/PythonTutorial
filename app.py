class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # init is short for initialize
        # this is the function/method that get called
        # when we create a new point object.
        # self is a reference to the current object.


    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20) # creating a new object, self will reference that object in memory.
print(point.x)
print(point.y)