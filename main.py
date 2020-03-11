import os, pathlib
import config as cf
import helper as hp
import numpy as np
np.random.seed(cf.MANUAL_SEED)
from data_loader import *
from model_handler import *

# Eliminating Warnings
import sys, warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
    os.environ["PYTHONWARNINGS"] = "ignore"

# Create Log File
pathlib.Path(cf.LOG_PATH).parent.mkdir(parents=True, exist_ok=True)
open(cf.LOG_PATH, 'w').close()

# Loading Data and Features
hp.saveLogMsg("\nLoading data...")
my_ner_dataset = NERDataset()
datasets_x, datasets_y = my_ner_dataset.get_raw_dataset()
datasets_x = my_ner_dataset.get_ner_dataset(datasets_x)
train_x, dev_x, test_x = datasets_x
train_y, dev_y, test_y = datasets_y
hp.saveLogMsg("#Train={}, #Dev={}, #Test={}".format(len(train_x), len(dev_x), len(test_x)))

# Finding Labels in Dataset
hp.saveLogMsg("\nFinding labels...")
labels = [each_y for sample_y in train_y for each_y in sample_y]
labels = list(set(labels))
labels.remove('O')
hp.saveLogMsg("#Labels={}\n".format(len(labels)+1))

# Run Model
handler = CRFHandler(labels)
model = None

if cf.MODE == "test" and os.path.exists(cf.MODEL_PATH):
    model = hp.load_model()
    hp.saveLogMsg("\nLoading best model from {}".format(cf.MODEL_PATH))
else:
    model = handler.train(train_x, train_y)
    hp.save_model(model)
    hp.saveLogMsg("\nSaving best model at {}".format(cf.MODEL_PATH))

assert model is not None

if cf.TEST_LABELED:
    acc_score, clf_report = handler.evaluate(model, dev_x, dev_y)
    hp.saveLogMsg('\n[DEV] Accuracy Score: {}'.format(acc_score))
    hp.saveLogMsg('\n[DEV] Classification Report: \n{}'.format(clf_report))
else:
    handler.predict(model, test_x)
    hp.saveLogMsg('\nSaving prediction at {}'.format(cf.PREDICT_PATH))
