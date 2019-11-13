import probabilistic_models.grammar_utils as gru
from zxcvbn_functions.frequency_lists import FREQUENCY_LISTS
import pickle


def build_ranked_dict(ordered_list):
    return {word: idx for idx, word in enumerate(ordered_list, 1)}


RANKED_DICTIONARIES = {}


def add_frequency_lists(frequency_lists_):
    for name, lst in frequency_lists_.items():
        RANKED_DICTIONARIES[name] = build_ranked_dict(lst)


add_frequency_lists(FREQUENCY_LISTS)


def construct_grammar_model(_ranked_dictionaries=RANKED_DICTIONARIES):
    composed_bases_dict = dict()
    simple_bases_dict = dict()
    composed_bases_list = []
    simple_bases_lists = dict()
    composed_base = ""
    simple_bases = []
    cb_counter = 0
    sb_counter = 0

    for dictionary_name, ranked_dict in _ranked_dictionaries.items():
        for w in ranked_dict:
            simple_bases, composed_base = gru.bases(w)
            composed_bases_list.append(composed_base)
            simple_bases_pattern = gru.cut(composed_base)
            for i in range(len(simple_bases)):
                p = simple_bases_pattern[i]
                if p in simple_bases_lists:
                    simple_bases_lists[p].append(simple_bases[i])
                else:
                    simple_bases_lists[p] = [simple_bases[i]]
            cb_counter += 1
            if composed_base in composed_bases_dict:
                composed_bases_dict[composed_base] += 1
            else:
                composed_bases_dict[composed_base] = 1
            for b in simple_bases:
                sb_counter += 1
                if b in simple_bases_dict:
                    simple_bases_dict[b] += 1
                else:
                    simple_bases_dict[b] = 1

    pickle.dump((cb_counter, composed_bases_dict), open("cb_dictionary.p", "wb"))
    pickle.dump((sb_counter, simple_bases_dict), open("sb_dictionary.p", "wb"))
    pickle.dump((composed_bases_list, simple_bases_lists), open("lists.p", "wb"))

    return

