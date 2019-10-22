from zxcvbn.probabilistic_models import grammars
from zxcvbn.probabilistic_models.grammar_utils import score

def probabilistic_model_guesses(password, scores):
    Q, B, lc, ls  = grammars.construct_grammar_model()
    score_password = score(password, Q, B)

    len_score = len(scores)
    rank_password = 0
    for i in range(len_score) :
        if scores[i] > score_password :
            rank_password += 1/ (scores[i]*len_score)
    return int(rank_password)


