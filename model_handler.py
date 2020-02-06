import os, nltk, sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import RandomizedSearchCV
import sklearn_crfsuite
from sklearn_crfsuite import metrics
from seqeval.metrics import accuracy_score
import config as cf
import helper as hp

class CRFHandler(object):

    def __init__(self, labels_):
        self.labels = labels_

    def train(self, train_x, train_y):

        # CRF with Fixed Parameters
        crf = sklearn_crfsuite.CRF(
            algorithm=cf.ALGORITHM,
            max_iterations=cf.EPOCH,
            all_possible_states=True,
            all_possible_transitions=True
        )

        # Parameters to Search
        params_space = {
            'c1': scipy.stats.expon(scale=cf.C1_SCALE),
            'c2': scipy.stats.expon(scale=cf.C2_SCALE),
        }

        # Evaluation Metric
        f1_scorer = make_scorer(metrics.flat_f1_score, average='weighted', labels=self.labels)

        # Hyper-parameter Optimization
        rs = RandomizedSearchCV(crf, params_space,
                                cv=cf.FOLDS,
                                verbose=1,
                                n_jobs=-1,
                                n_iter=cf.CANDIDATES,
                                scoring=f1_scorer)
        rs.fit(train_x, train_y)

        # Best Models
        hp.saveLogMsg("\nBest Params: {}".format(rs.best_params_))
        hp.saveLogMsg("Best CV Score: {}".format(rs.best_score_))
        model = rs.best_estimator_
        assert model is not None
        return model

    def evaluate(self, model, dev_x, dev_y):
        # Predict result
        pred_y = model.predict(dev_x)

        # Group B-* and I-* result
        sorted_labels = sorted(
            self.labels,
            key=lambda name: (name[1:], name[0])
        )

        # Classification report
        acc_score = accuracy_score(dev_y, pred_y)
        clf_report = metrics.flat_classification_report(dev_y, pred_y, labels=sorted_labels, digits=4)

        return acc_score, clf_report

    def predict(self, model, test_x):
        os.remove(cf.PREDICT_PATH) if os.path.exists(cf.PREDICT_PATH) else None
        pred_y = model.predict(test_x)
        with open(cf.PREDICT_PATH, 'a') as fout:
            for sent_x, sent_y in zip(test_x, pred_y):
                for word_x, word_y in zip(sent_x, sent_y):
                    fout.write(str(word_x) + "\t" + str(word_y) + "\n")
                fout.write("\n")

if __name__ == '__main__':
    pass