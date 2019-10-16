import grammars
import score

fl = {
    "1":"aaaaa123bb,ccc**azerty".split(","),
    "2":"123jaaj!,888abc320,320lll123".split(",")
}

def build_ranked_dict(ordered_list):
    return {word: idx for idx, word in enumerate(ordered_list, 1)}

RD = {}


def add_frequency_lists(frequency_lists_):
    for name, lst in frequency_lists_.items():
        RD[name] = build_ranked_dict(lst)

add_frequency_lists(fl)

Q,B = grammars.construct_grammar_model()
print(Q,B)

print(score.score("qwerty", Q, B))
print(score.score("abc123", Q, B))
