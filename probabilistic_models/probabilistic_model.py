from zxcvbn.probabilistic_models import grammars
from zxcvbn.probabilistic_models import score

def probabilistic_model_guesses(password, n, scores=SCORES):
    Q, B = grammars.construct_grammar_model()
    sw = score(password, Q, B)

    rw, i = 0
    while sw <= scores[i] and i<= len(scores) :
        rw += 1/ (score[i]*n)
        i+=1
    return rw

