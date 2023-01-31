from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_SHAPE = 'turtle'
TURTLE_COLOR = 'black'
FACE_TURTLE_NORTH = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(TURTLE_SHAPE)
        self.color(TURTLE_COLOR)
        self.goto(STARTING_POSITION)
        self.setheading(FACE_TURTLE_NORTH)

    def move_forward(self):
        new_x = 0
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=new_x, y=new_y)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)

