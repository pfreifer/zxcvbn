def base(w) :

    B = []
    Q = ''
    word =''
    for c in w:
        if word == '': word = c
        elif char_type(word[-1]) == char_type(c):
            word += c
        else :
            B.append(word)
            Q += char_type(word[-1]) + str(len(word))
            word = c
    B.append(word)
    Q += char_type(word[-1]) + str(len(word))
    return B, Q

def char_type(c):
    if c.isdigit() : return 'D'
    elif c.isalpha(): return 'L'
    else : return 'S'


# if __name__ == '__main__':
#     print(char_type(''))
#     print(base('ahh!!!123aah@@123'))
