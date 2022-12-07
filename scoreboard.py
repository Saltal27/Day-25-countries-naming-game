from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 7, 'normal')


class Scoreboard:

    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1

    def write_country_name(self, country, x, y):
        country_name = Turtle()
        country_name.hideturtle()
        country_name.penup()
        country_name.color("LightGreen")
        country_name.goto(x, y)
        country_name.write(arg=country, align=ALIGNMENT, font=FONT)
