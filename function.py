import datetime
import json
import random


def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        guess = int(input("Escoja el número secreto (entre 1 y 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("Acertaste! el número secreto era : " + str(secret))
            print("Necesitaste " + str(attempts) + " intentos")
            break
        elif guess > secret:
            print("Intenta con algo más pequeño")
        elif guess < secret:
            print("Intenta con algo más grande")


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


