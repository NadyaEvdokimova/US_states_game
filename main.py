import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
state = turtle.Turtle()
state.hideturtle()
state.penup()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
title = "Guess the State"

are_there_states = True
states_guessed = []

while are_there_states:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in states_guessed]
        missed_states = {
            "States": states_to_learn
        }

        new_table = pandas.DataFrame(missed_states)
        new_table.to_csv("states_to_learn.csv")
        break

    elif answer_state in states:
        title = f"{len(states_guessed)+1}/50 States Correct"
        row = data[data.state == answer_state]
        x_cor = row.x[row.index.item()]
        y_cor = row.y[row.index.item()]
        state.goto(x_cor, y_cor)
        state.write(row.state[row.index.item()])
        states_guessed.append(answer_state)

    if len(states_guessed) == len(states):
        state.color("blue")
        state.goto(0, 0)
        state.write("Congratulations! You've guessed all the States!")
        are_there_states = False
        turtle.mainloop()
