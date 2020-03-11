import re

def get_allnumber(word):
    word = str(word)
    try:
        if word.isdecimal(): return True
        if word.isdigit(): return True
        if word.isnumeric(): return True
    except:
        pass
    try:
        word = float(word)
        return True
    except:
        pass
    return False

def get_allcharacter(word):
    return all(
        ord(ch) >= ord('a') and ord(ch) <= ord('z')
        for ch in list(word.lower())
    )

def get_allsymbol(word):
    return all(
        not (
                (ord(ch) >= ord('a') and ord(ch) <= ord('z'))
                or (ord(ch) >= ord('0') and ord(ch) <= ord('9'))
        )
        for ch in list(word.lower())
    )

def get_hasnumber(word):
    return any(
        ord(ch) >= ord('0') and ord(ch) <= ord('9')
        for ch in list(word.lower())
    )

def get_hascharacter(word):
    return any(
        ord(ch) >= ord('a') and ord(ch) <= ord('z')
        for ch in list(word.lower())
    )

def get_hassymbol(word):
    return any(
        not (
                (ord(ch) >= ord('a') and ord(ch) <= ord('z'))
                or (ord(ch) >= ord('0') and ord(ch) <= ord('9'))
        )
        for ch in list(word.lower())
    )

def get_wordshape(word):
    word = re.sub('[A-Z]', 'X', word)
    word = re.sub('[a-z]', 'x', word)
    word = re.sub('[0-9]', 'd', word)
    return word

def get_shortwordshape(word):
    word = re.sub('[A-Z]+', 'X', word)
    word = re.sub('[a-z]+', 'x', word)
    word = re.sub('[0-9]+', 'd', word)
    return word
