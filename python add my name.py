from turtle import Turtle, Screen

FONT_SIZE = 20

FONT = ("Arial", FONT_SIZE, "bold")

yertle = Turtle()

# The turtle starts life in the center of the window
# but let's assume we've been drawing other things
# and now need to return to the center of the window

yertle.penup()
yertle.home()

# By default, the text prints too high unless we roughly
# readjust the baseline, you can confirm text placement
# by doing yertle.dot() after yertle.home() to see center

yertle.sety(-FONT_SIZE/2)

yertle.write("programmerShourya", align="center", font=FONT)

yertle.hideturtle()

screen = Screen()

screen.exitonclick()
