import pickle
from src.probabilistic_models.grammar_utils import score
from math import log
from decimal import Decimal

def probabilistic_model_guesses(password):
    scores = pickle.load(open("scores.p", "rb"))
    (Q, B) = pickle.load(open("dictionaries.p", "rb"))
    score_password = score(password, Q, B)
    len_score = len(scores)
    rank_password = 0
    for i in range(len_score) :
        if scores[i] > score_password :
            rank_password += 1/ (scores[i]*len_score)
    return int(rank_password)


def probabilistic_model_result(password):
    guesses = probabilistic_model_guesses(password)
    return {
        "guesses_log10" : log(guesses, 10),
        "guesses" : Decimal(guesses),
        "sequence" : [],
        "password" : password,
        "pattern" : "probabilistic_model"
    }
