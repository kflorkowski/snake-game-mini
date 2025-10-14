from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Represents the snake in the game.
    Handles movement, growth, and collision behavior.
    """
    def __init__(self):
        """Create the initial snake and set up the head reference."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Generate the starting snake body with three segments."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.up()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Move the snake forward by shifting each segment."""
        for segment_number in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[segment_number]
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            segment.goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def grow(self):
        """Add a new segment to the snake’s tail when food is eaten."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)

    def reset(self):
        """Reset the snake to its initial length and position."""
        for seg in self.segments:
            seg.goto(1500, 1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        """Change snake direction to UP unless it’s currently moving DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change snake direction to DOWN unless it’s currently moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change snake direction to LEFT unless it’s currently moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change snake direction to RIGHT unless it’s currently moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
