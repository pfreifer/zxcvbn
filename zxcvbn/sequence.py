from zxcvbn import scoring
from zxcvbn import adjacency_graphs
from zxcvbn.frequency_lists import FREQUENCY_LISTS
import re

from zxcvbn.scoring import most_guessable_match_sequence

def build_ranked_dict(ordered_list):
    return {word: idx for idx, word in enumerate(ordered_list, 1)}

RANKED_DICTIONARIES = {}


def add_frequency_lists(frequency_lists_):
    for name, lst in frequency_lists_.items():
        RANKED_DICTIONARIES[name] = build_ranked_dict(lst)

MAX_DELTA = 5

def sequence_match(password, _ranked_dictionaries=RANKED_DICTIONARIES):

    if len(password) == 1:
        return []

    def update(i, j, delta):
        if j - i > 1 or (delta and abs(delta) == 1):
            if 0 < abs(delta) <= MAX_DELTA:
                token = password[i:j + 1]
                if re.compile(r'^[a-z]+$').match(token):
                    sequence_name = 'lower'
                    sequence_space = 26
                elif re.compile(r'^[A-Z]+$').match(token):
                    sequence_name = 'upper'
                    sequence_space = 26
                elif re.compile(r'^\d+$').match(token):
                    sequence_name = 'digits'
                    sequence_space = 10
                else:
                    sequence_name = 'unicode'
                    sequence_space = 26
                result.append({
                    'pattern': 'sequence',
                    'i': i,
                    'j': j,
                    'token': password[i:j + 1],
                    'sequence_name': sequence_name,
                    'sequence_space': sequence_space,
                    'ascending': delta > 0
                })

    result = []
    i = 0
    last_delta = None

    for k in range(1, len(password)):
        delta = ord(password[k]) - ord(password[k - 1])
        if last_delta is None:
            last_delta = delta
        if delta == last_delta:
            continue
        j = k - 1
        update(i, j, last_delta)
        i = j
        last_delta = delta
    update(i, len(password) - 1, last_delta)

    return result



def alternate_sequence_match(password, _ranked_dictionaries=RANKED_DICTIONARIES):
    # Does the same than sequence_match on even and odd index characters.
    if len(password) == 1:
        return []

    even_index_password = ""
    odd_index_password = ""

    for i in range(len(password)):
        if (i%2):
            odd_index_password += password[i]
        else:
            even_index_password += password[i]

    result_even = sequence_match(even_index_password, _ranked_dictionaries)
    result_odd = sequence_match(odd_index_password, _ranked_dictionaries)
    result = []

    for x in result_even:
        x['i'] = 2*x['i']
        x['j'] = 2*x['j']
            
    for x in result_odd:
        x['i'] = 2*x['i']+1
        x['j'] = 2*x['j']+1
        for y in result_even:
            if (abs(x['i'] - y['i']) == 1) and (abs(x['j'] - y['j']) == 1):
                result.append({
                    'pattern': 'alternate_sequence',
                    'i': min(x['i'], y['i']),
                    'j':  max(x['j'], y['j']),
                    'token': password[min(x['i'], y['i']): max(x['j'], y['j'])+1],
                    'sequence_1': x['token'],
                    'sequence_2': y['token'],
                    'sequence_1_name': x['sequence_name'],
                    'sequence_2_name': y['sequence_name'],
                    'ascending_1': x['ascending'],
                    'ascending_2': y['ascending']
                })
    
    return result


if __name__ == '__main__':
    print(alternate_sequence_match("a1b3c5d7e"))
