import numpy as np
import string
import os
import pickle

punctuation = set(string.punctuation)
# ohe = OneHotEncoder()


file = "word_dict_ta.pickle"
os.chdir("/home/ubuntu/Notebooks/capstone/models")
with open(file, "rb") as f:
    word_dict = pickle.load(f)



def lower_rm_punct(review):
    return np.asarray(
        [
            wrd.lower()
            for wrd in "".join(
                [wrd for wrd in review if wrd not in punctuation]
            ).split()
        ]
    )


def my_padding(review, dictionary=None,maxlen=150):
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
    clean_review = lower_rm_punct(review)
    return my_padding(clean_review, maxlen, dictionary)


def review_prep(review, maxlen=150, dictionary=None):
    X = transform(review, maxlen, dictionary).reshape(1, maxlen)
    filler = X.copy()
    filler[:] = 0
    X = np.vstack([filler, X])
    return X


def run_model(review, score, dictionary=None, model=None, maxlen=150):
    X = review_prep(review, maxlen, dictionary)
    y_prediction = model.predict_classes(X)[1] + 2
    print(y_prediction)
    y_probs = model.predict(X)[1]
    print(y_probs)
    return prob_func(y_probs, score, y_prediction)


def prob_func(array, selection, prediction):
    selection = selection - 2
    print("selection:", selection)
    prediction = prediction - 2
    print("prediction:", prediction)
    diff = np.abs(prediction - selection)
    print("difference: ", diff)
    if diff < 2:
        counter = 0
        counter += array[selection]
        if selection != 0:
            counter += array[selection - 1]
        if selection != 3:
            counter += array[selection + 1]
        return (
            "Accurate w/ high probability: {}".format(round(counter, 2)),
            "score: {}".format(selection + 2),
            "pred: {}".format(prediction + 2),
        )
    if diff > 1:
        counter = 0
        counter += array[prediction]
        print("counter1:", counter)
        if prediction != 0:
            counter += array[prediction - 1]
        print("counter2:", counter)
        if prediction != 3:
            counter += array[prediction + 1]
        return (
            "requires review w/ high probability: {}".format(round(counter, 2)),
            "score: {}".format(selection + 2),
            "pred: {}".format(prediction + 2),
        )
