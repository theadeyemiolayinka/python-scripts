import turtle
import pandas
from tim import Tim

screen = turtle.Screen()
tim = turtle.Turtle()
image = "./blank_states_img.gif"
screen.addshape(image)
tim.shape(image)

states_data = pandas.read_csv("./50_states.csv")
state_name = states_data["state"]
state_name_list = state_name.to_list()
score = 0
correct_answer_list = []
while len(correct_answer_list) < 50:
    answer = str(screen.textinput(f"{score}/50 States Correct", "What's another state name?")).capitalize()
    if answer in state_name_list:
        correct_answer_list.append(answer)
        x_cor = int(states_data[states_data.state == answer].x)
        y_cor = int(states_data[states_data.state == answer].y)
        score += 1
        turtle_boy = Tim(answer, x_cor, y_cor)
    elif answer.lower() == "exit":
        # final_list = []
        final_list = [item for item in state_name_list if item not in correct_answer_list]
        # for item in state_name_list:
        #     if item not in correct_answer_list:
        #         final_list.append(item)

        data = pandas.DataFrame(final_list)
        data.to_csv("./states_to_learn.csv")
        break
    else:
        pass



