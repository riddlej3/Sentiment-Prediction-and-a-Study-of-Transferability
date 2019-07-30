##########################
# Module Overview: Contains main functions used for creation of app.py.
# Transforms Review Text data, preprocesses data, and inputs data into model
##########################

import numpy as np
import string
import os
import pickle


# punctuation list used to remove punctuation from text
punctuation = set(string.punctuation)
# ohe = OneHotEncoder()

# downloads word_dict (word dictionary of words used in model)
file = "word_dict_ta.pickle"
os.chdir("/home/ubuntu/Notebooks/capstone2/data")
with open(file, "rb") as f:
    word_dict = pickle.load(f)



def _lower_rm_punct(review):
    """
    removes punctuation from review
    """
    return np.asarray(
        [
            wrd.lower()
            for wrd in "".join(
                [wrd for wrd in review if wrd not in punctuation]
            ).split()
        ]
    )


def _my_padding(review, dictionary=None,maxlen=150):
    """
    Overview: Creates maxlen length zeroes vector and imputes word ints onto vector
    Inputs: text review, word_idx dictionary, and maxlen used in creation of model.
    """
    seq = np.zeros(maxlen).astype(str)
    if len(review) > maxlen:
        for i in range(maxlen):
            seq[i] = review[i]
    else:
        for i in range(1, len(review) + 1):
            seq[-i] = review[-i]
    return np.asarray(
        [str(0) if wrd not in dictionary else str(dictionary[wrd]) for wrd in seq]
    ).astype(int)


def transform(review,dictionary=None, maxlen=150):
    """
    combines first two functions in module
    """
    clean_review = _lower_rm_punct(review)
    return _my_padding(clean_review, maxlen, dictionary)


def review_prep(review, maxlen=150, dictionary=None):
    X = transform(review, maxlen, dictionary).reshape(1, maxlen)
    filler = X.copy()
    filler[:] = 0
    X = np.vstack([filler, X])
    return X


def run_model(review, score, dictionary=None, model=None, maxlen=150):
    if score == 1:
        new_score = 2
    else:
        new_score = score
    X = review_prep(review, maxlen, dictionary)
    y_prediction = model.predict_classes(X)[1] + 2
#     print(y_prediction)
    y_probs = model.predict(X)[1]
#     print(y_probs)
    return prob_func(y_probs, new_score, y_prediction,review)


def prob_func(array, selection, prediction,review):
    d = {}
    selection = selection - 2
#     print("selection:", selection)
    prediction = prediction - 2
#     print("prediction:", prediction)
    diff = np.abs(prediction - selection)
#     print("difference: ", diff)
    if diff < 2:
        counter = 0
        counter += array[prediction]
        counter += array[selection]
        if selection == prediction:
            counter = .99
        else:
            counter = counter
        d['review'] = review[:50]
        d['label'] = 'Accurate'
        d['probability'] = round(counter, 2)
        d['score'] = selection + 2
        d['pred'] = prediction + 2
        return d
    
    
    if diff > 1:
        counter = 0
        counter += array[prediction]
        counter += array[1-selection]
        d['review'] = review[:50]
        d['label'] = 'Requires Review'
        d['probability'] = round(counter, 2)
        d['score'] = selection + 2
        d['pred'] = prediction + 2
        return d


def tensorflow_quiet():
    """
    Make Tensorflow less verbose
    """
    try:
        # noinspection PyPackageRequirements
        import os
        from tensorflow import logging
        logging.set_verbosity(logging.ERROR)
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

        # Monkey patching deprecation utils to shut it up! Maybe good idea to disable this once after upgrade
        # noinspection PyUnusedLocal
        def deprecated(date, instructions, warn_once=True):
            def deprecated_wrapper(func):
                return func
            return deprecated_wrapper

        from tensorflow.python.util import deprecation
        deprecation.deprecated = deprecated

    except ImportError:
        pass