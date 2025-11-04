# EG 2nd Turtle racing

import turtle
import random

# functions

def setup_race():
    #Set up the screen, finish line, and turtles.
    screen = turtle.Screen()
    screen.title("Turtle Race!")
    screen.bgcolor("lightblue")

    # Draw finish line
    line = turtle.Turtle()
    line.penup()
    line.goto(250, 200)
    line.right(90)
    line.pendown()
    line.pensize(5)
    line.color("black")
    line.forward(400)
    line.hideturtle()

    # Create turtles
    colors = ["red", "blue", "green", "orange", "purple"]
    turtles = []
    y_positions = [150, 75, 0, -75, -150]

    for i in range(5):
        racer = turtle.Turtle(shape="turtle")
        racer.color(colors[i])
        racer.penup()
        racer.goto(-250, y_positions[i])
        turtles.append(racer)

    return screen, turtles

def race(turtles):
 # Run the turtle race until one turtle crosses the finish line.
    winner = None
    while not winner:
        for racer in turtles:
            distance = random.randint(1, 10)
            racer.forward(distance)
            if racer.xcor() >= 250:  
                winner = racer
                break
    return winner

def announce_winner(winner):
    #Display the winning turtle’s color.
    winning_color = winner.pencolor()
    print(f"The {winning_color} turtle won!")

    # Announce on screen
    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, 0)
    announcer.write(f"The {winning_color} turtle won!")

# Main

def main():
    screen, turtles = setup_race()
    winner = race(turtles)
    announce_winner(winner)
    screen.mainloop()  

main()


