import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
game_on = True
score = 0
correct_answers = []
all_states = data.state.to_list()

while game_on:
    answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="Write the state's name")).title()
    lists = data.state.to_list()
    if answer_state == "Exit":
        break

    if answer_state in lists:
        the_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(the_data.x), int(the_data.y))
        t.write(answer_state)
        if answer_state not in correct_answers:
            correct_answers.append(answer_state)
            score += 1
        if len(correct_answers) == 50:
            game_on = False

states_to_learn = {
    "States to learn": []
}
for i in all_states:
    if i not in correct_answers:
        states_to_learn["States to learn"].append(i)
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
