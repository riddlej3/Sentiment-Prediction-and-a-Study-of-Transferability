#######################
# Overview: Application for predicting the score of a text based review.
# Inputs: review4.txt text file beginning with integer score and followed by review text. Ex. '5. What a great hotel stay'
# Notes: As one sees, a lot of text is commented out. If one wishes to run this app using multiple text files, one can remove the comments to print multiple review predictions. Another alternative is to build this into a loop and output a table.
######################

import os
import pandas as pd
from keras.models import load_model
import warnings

os.chdir("/home/ubuntu/Notebooks/capstone2/src")
from app_module import *
from app_module import word_dict

warnings.filterwarnings("ignore")

# To ensure that tf is not overly verbose
tensorflow_quiet()

# path to input data
os.chdir("/home/ubuntu/Notebooks/capstone2/")
# review = pd.read_csv('review.txt', header = None,sep='\t').values[0][0]
# review2 = pd.read_csv('review2.txt', header = None,sep='\t').values[0][0]
# review3 = pd.read_csv('review3.txt', header = None,sep='\t').values[0][0]
review4 = pd.read_csv("review.txt", header=None, sep="\t").values[0][0]


# path to model
os.chdir("/home/ubuntu/Notebooks/data")
model = load_model("first_model_ta2.h5")

# t1 = pd.DataFrame([run_model(review[1:],
#                    int(review[0]),
#                    dictionary=word_dict,
#                    model=model)])
# t2 = pd.DataFrame([run_model(review2[1:],
#                    int(review2[0]),
#                    dictionary=word_dict,
#                    model=model)])
# t3 = pd.DataFrame([run_model(review3[1:],
#                    int(review3[0]),
#                    dictionary=word_dict,
#                   model=model)])
t4 = pd.DataFrame(
    [run_model(review4[1:], int(review4[0]), dictionary=word_dict, model=model)]
)

print(
    "\n\n\n\n\n", t4[["review", "label", "score", "pred", "probability"]], "\n\n\n\n\n"
)