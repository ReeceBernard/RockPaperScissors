from flask import render_template, url_for, flash, redirect
from rps import app
from rps.src.play import play
from rps.src.play import update_weights
import numpy as np

last_play = None
last_result = None
game_state = [0,0,0]
weights = {
        "W": {
            "R": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "P": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "S": {
                "R": 1,
                "P": 1,
                "S": 1
            }
        },
        "L": {
            "R": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "P": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "S": {
                "R": 1,
                "P": 1,
                "S": 1
            }
        },
        "T": {
            "R": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "P": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "S": {
                "R": 1,
                "P": 1,
                "S": 1
            }
        }
    }
@app.route("/")
@app.route("/home")
def home():
    global game_state
    game_state = [0,0,0]
    global weights
    weights = {
        "W": {
            "R": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "P": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "S": {
                "R": 1,
                "P": 1,
                "S": 1
            }
        },
        "L": {
            "R": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "P": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "S": {
                "R": 1,
                "P": 1,
                "S": 1
            }
        },
        "T": {
            "R": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "P": {
                "R": 1,
                "P": 1,
                "S": 1
            },
            "S": {
                "R": 1,
                "P": 1,
                "S": 1
            }
        }
    }
    return render_template('home.html', game_state=game_state, weights=weights, robot_choice="", player_choice="")


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/play_rock")
def play_rock():
    global last_play
    global last_result
    res, robot_choice = play("R", weights, last_result, last_play)
    if res == 1:
        game_state[0] += 1
        update_weights(weights, 0.1, robot_choice, last_play, last_result)
        last_result = "W"
    elif res == -1:
        game_state[1] += 1
        last_result = "L"
    else:
        game_state[2] += 1
        update_weights(weights, 0.05, robot_choice, last_play, last_result)
        last_result = "T"
    last_play = 'R'
    return render_template('home.html', game_state=game_state, weights=weights, robot_choice=robot_choice, player_choice="R")

@app.route("/play_paper")
def play_paper():
    global last_play
    global last_result
    res, robot_choice = play("P", weights, last_result, last_play)
    if res == 1:
        game_state[0] += 1
        update_weights(weights, 0.1, robot_choice, last_play, last_result)
        last_result = "W"
    elif res == -1:
        game_state[1] += 1
        last_result = "L"
    else:
        game_state[2] += 1
        update_weights(weights, 0.05, robot_choice, last_play, last_result)
        last_result = "T"
    last_play = 'P'
    return render_template('home.html', game_state=game_state, weights=weights, robot_choice=robot_choice, player_choice="P")

@app.route("/play_scissors")
def play_scissors():
    global last_play
    global last_result
    res, robot_choice = play("S", weights, last_result, last_play)
    if res == 1:
        game_state[0] += 1
        update_weights(weights, 0.1, robot_choice, last_play, last_result)
        last_result = "W"
    elif res == -1:
        game_state[1] += 1
        last_result = "L"
    else:
        game_state[2] += 1
        update_weights(weights, 0.05, robot_choice, last_play, last_result)
        last_result = "T"
    last_play = 'S'
    print(weights)
    return render_template('home.html', game_state=game_state, weights=weights, robot_choice=robot_choice, player_choice="S")

@app.route("/restart")
def restart():
    return redirect(url_for("home"))