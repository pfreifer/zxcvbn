import pickle

import probabilistic_models.grammar_utils as gru
from random import choice


def draw(composed_bases_list, simple_bases_lists):
    composed_base = choice(composed_bases_list)
    simple_bases = gru.cut(composed_base)
    word = ""
    for base in simple_bases:
        word += choice(simple_bases_lists[base])
    return word
    

def scores(n):
    (composed_bases_list, simple_bases_lists) = pickle.load(open("lists.p", "rb"))
    (cb_counter, composed_bases_dict) = pickle.load(open("cb_dictionary.p", "rb"))
    (sb_counter, simple_bases_dict) = pickle.load(open("sb_dictionary.p", "rb"))
    scores = []
    for i in range(n):
        w = draw(composed_bases_list, simple_bases_lists)
        s = gru.score(w, cb_counter, sb_counter, composed_bases_dict, simple_bases_dict)
        scores.append(s)
    pickle.dump(scores, open("scores.p", "wb"))
    return
