import nltk
import config as cf
import helper as hp
from feature_extractor import *
from nltk import conlltags2tree, tree2conlltags

class NERDataset(object):

    def __init__(self):
        pass

    # Load raw dataset
    def get_raw_dataset(self):
        datasets_x, datasets_y   = [], []
        data_files = [cf.TRAIN_FILE, cf.DEV_FILE, cf.TEST_FILE]
        for fname in data_files:
            contents = ""
            with open(fname, 'r') as fin:
                contents = fin.read()
            sentences, labels = [], []
            for group in contents.split("\n\n"):
                sentence, label = [], []
                for line in group.split("\n"):
                    line = line.strip()
                    if not line: continue
                    line = line.split()
                    if len(line) > 0:
                        sentence.append(line[0])
                    if len(line) > 1:
                        label.append(line[-1])
                if len(sentence) > 0:
                    sentences.append(sentence)
                    labels.append(label)
            datasets_x.append(sentences)
            datasets_y.append(labels)
        return datasets_x, datasets_y

    # Return postags for sentence
    def get_postag(self, sentence):
        postags = nltk.pos_tag(sentence)
        postags = [x[-1] for x in postags]
        return postags

    # Return chunktag for sentence
    def get_chunktag(self, sentence):
        grammar = r"""
              NP: {<DT|JJ|P.*P.*|NN.*>+}
              PP: {<IN>+}
              VP: {<VB.*>+}
              ADVP: {<RB>+}
          """
        pos_sent = nltk.pos_tag(sentence)
        cp = nltk.RegexpParser(grammar)
        chunk_tree = cp.parse(pos_sent)
        chunk_tags = tree2conlltags(chunk_tree)
        chunk_tags = [ck[-1] for ck in chunk_tags]
        return chunk_tags

    # Add features to data
    def get_ner_dataset(self, data_old_x):
        ner_ext = NERExtractor()
        data_new_x = [[] for _ in range(len(data_old_x))]
        for i in range(len(data_old_x)):
            for sentence in data_old_x[i]:
                feature_x = []
                postags = self.get_postag(sentence)
                chunktags = self.get_chunktag(sentence)
                for idx in range(0, len(sentence)):
                    feature_x.append(ner_ext.get_features(idx, sentence, postags, chunktags))
                data_new_x[i].append(feature_x)
        return data_new_x

if __name__ == '__main__':
    my_obj = NERDataset()
    datasets_x, datasets_y = my_obj.get_raw_dataset()
    print(len(datasets_x))
    datasets_x = [datasets_x[0][:10], datasets_x[1][:10], datasets_x[2][:10]]
    datasets_x = my_obj.get_ner_dataset(datasets_x)
    print(len(datasets_x))
