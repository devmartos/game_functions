from function import play_game
from function import get_top_scores



while True:
    selection = input("Que te gustaría? A) Nueva partida, B) Ver la mejor puntuación, or C) Salir ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break