import probabilistic_models.grammar_utils as gru
from random import choice


def draw(composed_bases_list, simple_bases_lists):
    composed_base = choice(composed_bases_list)
    simple_bases = gru.cut(composed_base)
    word = ""
    for base in simple_bases:
        word += choice(simple_bases_lists[base])
    return word
    

def scores(n, composed_bases_list, simple_bases_lists, composed_bases_dict, simple_bases_dict):
    scores = []
    for i in range(n):
        w = draw(composed_bases_list, simple_bases_lists)
        s = gru.score(w, composed_bases_dict, simple_bases_dict)
        scores.append(s)
    return scores
