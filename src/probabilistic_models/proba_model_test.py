import probabilistic_models.grammar_utils as gru
import probabilistic_models.random_set as rs

from probabilistic_models import grammars
from probabilistic_models.probabilistic_model import probabilistic_model_guesses

fl = {
    "1": "aaaaa123bb,ccc**azerty".split(","),
    "2": "123jaaj!,888abc320,320lll123".split(",")
}


def build_ranked_dict(ordered_list):
    return {word: idx for idx, word in enumerate(ordered_list, 1)}


RD = {}


def add_frequency_lists(frequency_lists_):
    for name, lst in frequency_lists_.items():
        RD[name] = build_ranked_dict(lst)


if __name__ == "__main__":
    add_frequency_lists(fl)

    Q, B, lc, ls = grammars.construct_grammar_model()

    print(gru.score("qwerty", Q, B))
    print(gru.score("abc123", Q, B))

    # print(rs.scores(1000000, lc, ls, Q, B))

    print(probabilistic_model_guesses("password", rs.scores(100000, lc, ls, Q, B)))
