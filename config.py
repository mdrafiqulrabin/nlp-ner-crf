
# Path and Files
ROOT_PATH = "/Users/mdrafiqulrabin/Desktop/nlp-ner-crf/"
DATA_PATH = "temp/data/raw/"

TRAIN_FILE = ROOT_PATH + DATA_PATH + "train.txt"
DEV_FILE   = ROOT_PATH + DATA_PATH + "dev.txt"
TEST_FILE  = ROOT_PATH + DATA_PATH + "test.txt"

# Model Params
MANUAL_SEED = 42
ALGORITHM  = 'lbfgs'
EPOCH = 100
C1_SCALE = 0.5
C2_SCALE = 0.05
FOLDS = 3
CANDIDATES  = 50

# Model Logs
MODE = "train" #train/test
TEST_LABELED = True
TITLE = "crf"

RESULT_PATH = ROOT_PATH   + "temp/result/"
LOG_PATH    = RESULT_PATH + TITLE + ".log"
MODEL_PATH  = RESULT_PATH + TITLE + ".model"
PREDICT_PATH = RESULT_PATH + "predict.txt"

# Top-k
TOP_K = 5
