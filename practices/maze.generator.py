# Import needed libraries
import turtle
import random


# Variables

# Set the two variables, a list with multiple nested lists inside representing each row or column
maze_rows = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]]

maze_columns = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
             [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]]

# Set the turtles to draw the border of the maze
border = turtle.Turtle()

# Turtles to draw the row and column
row_turtle = turtle.Turtle()
column_turtle = turtle.Turtle()


# Functions

# Function to draw the border of the maze
def draw_border():
    border.teleport(0, 0)
    border.speed(15)
    border.hideturtle()
    border.pensize(5)
    border.teleport(50, 0)
    border.forward(250)
    border.left(90)
    border.forward(300)
    border.teleport(0, 0)
    border.forward(300)
    border.right(90)
    border.forward(250)

# Function to setup the row turtle and column turtle with the right settings
def setup_turtles(turtle_type, left_turn):
    turtle_type.speed(15)
    turtle_type.hideturtle()
    turtle_type.pensize(5)
    turtle_type.penup()
    turtle_type.teleport(0, 0)
    turtle_type.left(left_turn)

# Function to use the turtles to draw the inside of the maze
def draw_maze(group, turtle_type, x_cord_value, y_cord_value):
    y_cord = 0
    x_cord = 0
    row_turtle.forward(50)

    for row in group:
        for grid in row:
            if grid == 0:
                turtle_type.penup()
                turtle_type.forward(50)
            if grid == 1:
                turtle_type.pendown()
                turtle_type.forward(50)

        y_cord += y_cord_value
        x_cord += x_cord_value
        turtle_type.teleport(x_cord, y_cord)

# Function to check if the maze is solvable
def is_solvable(row_grid, column_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()
        if x == size - 1 and y == size - 1:
            return True
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and column_grid[x+1][y] == 0:
            stack.append((x + 1, y))
        if y < size - 1 and row_grid[x][y+1] == 0:
            stack.append((x, y + 1))
        if x > 0 and column_grid[x][y] == 0:
            stack.append((x - 1, y))
        if y > 0 and row_grid[x][y] == 0:
            stack.append((x, y - 1))
    return False
       
# Calling the functions
setup_turtles(row_turtle, 0)
setup_turtles(column_turtle, 90)
draw_border()

solvable = is_solvable(maze_rows, maze_columns)

while solvable == False:
    if solvable == True:
        draw_border()
        setup_turtles(row_turtle, 0)
        setup_turtles(column_turtle, 90)
        draw_maze(maze_rows, row_turtle, 0, 50)
        draw_maze(maze_columns, column_turtle, 50, 0)
        print("Solvable")
        break

turtle.done()