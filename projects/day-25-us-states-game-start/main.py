import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guess_states = []

while len(guess_states) < 50:

    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()
   

    for state in data["state"]:
        if answer_state == state:
            guess_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data["state"] == answer_state]
            t.goto(state_data.x.item(),state_data.y.item())
            t.write(answer_state)


screen.exitonclick()