# NLP-NER-CRF
Project: 2020SP-COSC6336-Natural Language Processing \
Task: Named-Entity Recognition using Conditional Random Fields (CRF)

- - -

# Library:
- Python 3.7.4
- Scikit-Learn 0.21.2
- seqeval 0.0.12
- sklearn-crfsuite 0.3.6
- IDE: PyCharm 2020.1

- - -

# Final Project Guidelines:

- Your task is to implement a named entity recognizer using Conditional Random Fields (CRFs). Your code should be implemented in Python 3 and you are allowed to use available libraries such as scikit-learn.
- The training and development sets come from WNUT corpus, and test data is from an anonymous social media platform. The format of the data is the same across all three different sets. Each row includes one word and the entity tag which is assigned to that word, and posts are separated with blank lines. The data uses IOB encoding.
- You should use training data for building your model, and development set for fine-tuning the hyper-parameters of the classifier or improving the feature set. You can also use your development set for evaluating and analyzing your model. Test data must only be used for the final evaluation of your model.

# Result and Analysis:

We studied the 'Named-Entity Recognition using Conditional Random Fields (CRF)' in this project. We *adopted* the analysis slightly and implemented the code by ourselves. See below for summary:

<img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/IOB.png" alt="IOB" width="400"/> <img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Table1.png" alt="WNUT" width="400"/> 

<img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/CRF.png" alt="CRF" width="400"/> <img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Table2.png" alt="Features" width="400"/> 

<img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Table3.png" alt="Algorithms" width="400"/> <img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/C1C2.png" alt="C1C2" width="400"/> 

<img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Model1.png" alt="Model1" width="280"/> <img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Model2.png" alt="Model2" width="280"/> <img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Model3.png" alt="Model3" width="280"/>

<img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/Transitions.png" alt="Transitions" width="400"/> <img src="https://github.com/mdrafiqulrabin/nlp-ner-crf/blob/master/result/summary/States.png" alt="States" width="400"/>

- - -

# References:

•	NLTK : https://www.nltk.org/api/nltk.html \
•	CRFsuite : https://sklearn-crfsuite.readthedocs.io/en/latest/tutorial.html \
•	POS-tag: https://www.nltk.org/book/ch05.html \
•	Chunk-tag: http://www.nltk.org/book_1ed/ch07.html \
•	W-NUT : http://noisy-text.github.io/2020/ 

