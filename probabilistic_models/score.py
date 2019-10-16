import grammars

def score(w, composed_bases_dict, simple_bases_dict):
    B, Q = grammars.bases(w)
    S = 0
    if Q in composed_bases_dict:
        S = composed_bases_dict[Q]
    for b in B:
        if b in simple_bases_dict:
            S *= simple_bases_dict[b]
        else:
            S = 0
    return S
