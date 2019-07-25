import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import warnings
import re
from nltk.corpus import stopwords
from nltk import word_tokenize


def no_text_index(string):
    return any([item.isalpha() for item in string])


def word_count(string):
    return len(string.split())


def word_count_column(series):
    return [word_count(i) for i in hotels["reviews.text"]]


def sentence_count(string):
    return len(re.split(r"[.!?]", string)[:-1])


def sentence_count_column(series):
    return [sentence_count(i) for i in series]


def remove_stopwords(string):
    swords = set(stopwords.words("english"))
    return " ".join([w for w in word_tokenize(string) if w not in swords])


def clean_text_series(series):
    new_list = []
    for i in hotels["reviews.text"]:
        new_list.append(remove_stopwords(i))
    return new_list


def sample_mean(series):
    return sum(series) / (len(series) - 1)


def bootstrap(series, n):
    list_of_means = []
    for _ in range(n):
        list_of_means.append(
            round(sample_mean(series.sample(len(series), replace=True)), 3)
        )
    return list_of_means


def axisfunc(i):
    if i == 1:
        return 1
    else:
        if i % 4 == 0:
            return 1
        else:
            return 0
