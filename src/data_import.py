"""
Potentially trash module? 
Needs investigation to see whether or not any function here is being used. If not, trash it.
"""

import os
import numpy as numpy
import pandas as pd
from lists import cols_new

cols_new = cols_new().get_cols_new()


def month_pickling_start(month, year):
    os.rename(
        "/Users/ginariddle/Downloads/listings.csv",
        "/Users/ginariddle/Desktop/g.school/capstone/listings.csv",
    )
    os.rename(
        "/Users/ginariddle/Downloads/listings.csv.gz",
        "/Users/ginariddle/Desktop/g.school/capstone/listings.csv.gz",
    )
    os.rename(
        "/Users/ginariddle/Downloads/reviews.csv.gz",
        "/Users/ginariddle/Desktop/g.school/capstone/reviews.csv.gz",
    )

    listings1 = pd.read_csv("listings.csv.gz")
    listings2 = pd.read_csv("listings.csv")

    listings = (
        listings1.merge(listings2, how="inner", on="id")[cols_new]
        .reset_index()
        .drop(labels="index", axis=1)
        .drop_duplicates()
    )
    listings.to_pickle("listings.pickle")

    reviews = pd.read_csv("reviews.csv.gz").drop_duplicates()
    reviews.to_pickle("reviews.pickle")

    os.remove("/Users/ginariddle/Desktop/g.school/capstone/listings.csv")
    os.remove("/Users/ginariddle/Desktop/g.school/capstone/listings.csv.gz")
    os.remove("/Users/ginariddle/Desktop/g.school/capstone/reviews.csv.gz")


def month_pickling(month, year):

    #     if (((pd.read_csv('/Users/ginariddle/Downloads/listings.csv').columns == pd.read_csv('test_listings.csv').columns).all() == False) or \
    #         ((pd.read_csv('/Users/ginariddle/Downloads/listings.csv.gz').columns == pd.read_csv('test_listings.csv.gz').columns).all()==False) or \
    #         ((pd.read_csv('/Users/ginariddle/Downloads/reviews.csv.gz').columns == pd.read_csv('test_reviews.csv.gz').columns).all()==False)):
    #         return 'column problem'

    os.rename(
        "/Users/ginariddle/Downloads/listings.csv",
        "/Users/ginariddle/Desktop/g.school/capstone/listings.csv",
    )
    os.rename(
        "/Users/ginariddle/Downloads/listings.csv.gz",
        "/Users/ginariddle/Desktop/g.school/capstone/listings.csv.gz",
    )
    os.rename(
        "/Users/ginariddle/Downloads/reviews.csv.gz",
        "/Users/ginariddle/Desktop/g.school/capstone/reviews.csv.gz",
    )

    listings1 = pd.read_csv("listings.csv.gz")
    listings2 = pd.read_csv("listings.csv")

    listings = (
        listings1.merge(listings2, how="inner", on="id")[cols_new]
        .reset_index()
        .drop(labels="index", axis=1)
        .drop_duplicates()
    )
    listings_old = pd.read_pickle("listings.pickle")

    reviews = pd.read_csv("reviews.csv.gz").drop_duplicates()
    reviews_old = pd.read_pickle("reviews.pickle")

    listings = (
        pd.concat([listings_old, listings1], join="inner", axis=0)
        .reset_index()
        .drop(labels="index", axis=1)
        .drop_duplicates()
    )
    listings.to_pickle("listings.pickle")

    reviews = reviews_old.append(reviews).drop_duplicates()
    reviews.to_pickle("reviews.pickle")

    os.remove("/Users/ginariddle/Desktop/g.school/capstone/listings.csv")
    os.remove("/Users/ginariddle/Desktop/g.school/capstone/listings.csv.gz")
    os.remove("/Users/ginariddle/Desktop/g.school/capstone/reviews.csv.gz")
