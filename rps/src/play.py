import random


def update_weights(weights, sigma, robot_choice, last_play, last_result):
    if not last_result:
        return weights
    else:
        weights[last_result][last_play][robot_choice] = weights[last_result][last_play][
            robot_choice
        ] * (1 - sigma)
    return weights


def play(player_choice, weights, last_result, last_play):
    robot = Robot()
    if not last_result:
        robot_choice = robot.random_predict()
    else:
        robot_choice = robot.mwu(weights[last_result][last_play])
    if robot_choice == player_choice:
        return 0, robot_choice
    elif (
        (robot_choice == "R" and player_choice == "P")
        or (robot_choice == "S" and player_choice == "R")
        or (robot_choice == "P" and player_choice == "S")
    ):
        return 1, robot_choice
    else:
        return -1, robot_choice


class Robot:
    def always_rock(self):
        return "R"

    def random_predict(self):
        output = random.choice(["R", "P", "S"])
        return output

    def mwu(self, weights):
        print(weights)
        weight_list = list(weights.values())
        if sum(weight_list) == 3:
            output = random.choice(["R", "P", "S"])
        elif weight_list[0] == weight_list[1]:
            output = random.choice(["R", "P"])
        elif weight_list[0] == weight_list[2]:
            output = random.choice(["R", "S"])
        elif weight_list[1] == weight_list[2]:
            output = random.choice(["P", "S"])
        else:
            max_index = 0
            for i in range(1, 3):
                if weight_list[i] > weight_list[max_index]:
                    max_index = i
            output = ["R", "P", "S"][max_index]
        return output

    def moral_booster(self, user_input):
        win_map = {"R": "S", "P": "R", "S": "P"}
        return win_map[user_input]

    def sad_times(self, user_input):
        lose_map = {"S": "R", "R": "P", "P": "S"}
        return lose_map[user_input]
