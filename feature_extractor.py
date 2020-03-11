import helper as hp
import nltk
from nltk.corpus import gazetteers
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

class NERExtractor(object):

    def __init__(self):
        pass

    def get_features(self, index, sentence, postags, chunktags):
        word = sentence[index]
        idxf, idxl = 0, len(sentence) - 1
        prevword = '' if index == idxf else sentence[index - 1]
        nextword = '' if index == idxl else sentence[index + 1]

        return {
            'word': word,
            'prev_word': prevword,
            'next_word': nextword,

            'word_len': len(word),
            'prev_word_len': len(prevword),
            'next_word_len': len(nextword),

            'prefix-1': word[0].lower(),
            'prefix-2': word[:2].lower(),
            'prefix-3': word[:3].lower(),
            'prefix-4': word[:4].lower(),

            'suffix-1': word[-1].lower(),
            'suffix-2': word[-2:].lower(),
            'suffix-3': word[-3:].lower(),
            'suffix-4': word[-4:].lower(),

            'wordshape': hp.get_wordshape(word),
            'prev_wordshape': hp.get_wordshape(prevword),
            'next_wordshape': hp.get_wordshape(nextword),

            'shortwordshape': hp.get_shortwordshape(word),
            'prev_shortwordshape': hp.get_shortwordshape(prevword),
            'next_shortwordshape': hp.get_shortwordshape(nextword),

            'postag': postags[index],
            'prev_postag': '' if index == idxf else postags[index - 1],
            'next_postag': '' if index == idxl else postags[index + 1],

            'chunktag': chunktags[index],
            'prev_chunktag': '' if index == idxf else chunktags[index - 1],
            'next_chunktag': '' if index == idxl else chunktags[index + 1],

            'isupper': word.isupper(),
            'prev_isupper': '' if index == idxf else prevword.isupper(),
            'next_isupper': '' if index == idxl else nextword.isupper(),

            'islower': word.islower(),
            'prev_islower': '' if index == idxf else prevword.islower(),
            'next_islower': '' if index == idxl else nextword.islower(),

            'istitle': word.istitle(),
            'prev_istitle': '' if index == idxf else prevword.istitle(),
            'next_istitle': '' if index == idxl else nextword.istitle(),

            'has_hyphen': '-' in word,
            'has_period': '.' in word,
            'has_comma': ',' in word,

            'allsymbol': hp.get_allsymbol(word),
            'allnumber': hp.get_allnumber(word),
            'allcharacter': hp.get_allcharacter(word),
            'isalnum': word.isalnum(),

            'hasnumber': hp.get_hasnumber(word),
            'hascharacter': hp.get_hascharacter(word),
            'hassymbol': hp.get_hassymbol(word),

            'isgazetteer': word in gazetteers.words(),
            'prev_isgazetteer': prevword in gazetteers.words(),
            'next_isgazetteer': nextword in gazetteers.words(),

            'isstopword': word.lower() in stopwords.words('english'),
            'prev_isstopword': prevword.lower() in stopwords.words('english'),
            'next_isstopword': nextword.lower() in stopwords.words('english'),

            'porterstemmer': PorterStemmer().stem(word),
            'prev_porterstemmer': '' if index == idxf else PorterStemmer().stem(prevword),
            'next_porterstemmer': '' if index == idxl else PorterStemmer().stem(nextword),

            'lemmatize': WordNetLemmatizer().lemmatize(word),
            'prev_lemmatize': '' if index == idxf else WordNetLemmatizer().lemmatize(prevword),
            'next_lemmatize': '' if index == idxl else WordNetLemmatizer().lemmatize(nextword)
        }

if __name__ == '__main__':
    sentence = "My name is Rabin!"
    tokens   = nltk.word_tokenize(sentence)
    postags  = [x[-1] for x in nltk.pos_tag(tokens)]
    chunktag = postags.copy() #todo

    my_obj = NERExtractor()
    for idx in range(0, len(tokens)):
        print(my_obj.get_features(idx, tokens, postags, chunktag))
