from turtle import Turtle

ALIGNMENT = "center"

# Load high score from file
with open("../data.txt") as file:
    HIGHSCORE = int(file.read())


class Scoreboard(Turtle):
    """
    Manages and displays the current score and high score.
    Updates the scoreboard each time the player scores or resets.
    """
    def __init__(self):
        """Initialize the scoreboard and display the initial scores."""
        super().__init__()
        self.score = 0
        with open("../data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()

        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh the displayed score and high score on screen."""
        self.clear()
        self.goto(x=-30, y=280)
        self.write(f"Score: {self.score}", align=ALIGNMENT)
        self.goto(x=30, y=280)
        self.write(f"High Score: {self.highscore}", align=ALIGNMENT)

    def increase_score(self):
        """Increase the current score by 1 and update the display."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """
        Reset the score after collision and update the high score file
        if a new high score has been achieved.
        """
        if self.highscore < self.score:
            self.highscore = self.score
            with open("../data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """
        Display a GAME OVER message in the center of the screen.

        Note:
            This method is not currently used in the game loop,
            but kept for potential future enhancements.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT)

