from zxcvbn.probabilistic_models import grammars
from zxcvbn.probabilistic_models.grammar_utils import score
import zxcvbn.probabilistic_models.random_set as rs


Q,B,lc,ls = grammars.construct_grammar_model()


SCORES = rs.scores(100000, lc, ls, Q, B)


def probabilistic_model_guesses(password, scores=SCORES):
    Q, B, lc, ls  = grammars.construct_grammar_model()
    score_password = score(password, Q, B)

    len_score = len(scores)
    rank_password = 0
    for i in range(len_score) :
        if scores[i] > score_password :
            rank_password += 1/ (scores[i]*len_score)
    return int(rank_password)


