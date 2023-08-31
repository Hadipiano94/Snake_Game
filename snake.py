from turtle import Turtle


class Snake:

    def __init__(self, length):
        """a snake is a list of square turtle objects (dimentions = 20 * 20)
        that are connected to the head, head is at index 0"""
        self.segments = []
        self.init_poses = []
        for i in range(length):
            self.init_poses.append((i * (-20), 0))
        for position in self.init_poses:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """moving each square to tha previous position of the next square"""
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.segments[0].forward(20)

    def add_seg(self):
        """adding one square to the tail"""
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[len(self.segments) - 1].position())
        self.segments.append(new_segment)
