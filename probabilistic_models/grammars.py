from zxcvbn.frequency_lists import FREQUENCY_LISTS

def build_ranked_dict(ordered_list):
    return {word: idx for idx, word in enumerate(ordered_list, 1)}

RANKED_DICTIONARIES = {}

def add_frequency_lists(frequency_lists_):
    for name, lst in frequency_lists_.items():
        RANKED_DICTIONARIES[name] = build_ranked_dict(lst)

add_frequency_lists(FREQUENCY_LISTS)


def base(w) :

    simple_bases = []
    composed_base = ''
    word =''
    for c in w:
        if word == '': word = c
        elif char_type(word[-1]) == char_type(c):
            word += c
        else :
            simple_bases.append(word)
            composed_base += char_type(word[-1]) + str(len(word))
            word = c
    simple_bases.append(word)
    composed_base += char_type(word[-1]) + str(len(word))
    return simple_bases, composed_base

def char_type(c):
    if c.isdigit() : return 'D'
    elif c.isalpha(): return 'L'
    else : return 'S'


def construct_grammar_model(_ranked_dictionaries=RANKED_DICTIONARIES):
    composed_bases_dict = dict()
    simple_bases_dict = dict()
    composed_base = ""
    simple_bases = []
    cb_counter = 0
    sb_counter = 0

    for dictionary_name, ranked_dict in _ranked_dictionaries.items():
        for w in ranked_dict:
            print(w)
            simple_bases, composed_base = bases(w)
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

    for cb in composed_bases_dict:
        composed_bases_dict[cb] /= cb_counter
    for sb in simple_bases_dict:
        simple_bases_dict[sb] /= sb_counter

    return composed_bases_dict, simple_bases_dict

