import numpy as np
import pandas as pd

def hotel_data_cleaning(df):
    hotels = df.drop("reviews.id", axis=1)[df["language"] == "en"]
    hotels["reviews.rating"] = df["reviews.rating"].replace(1.0, 2.0).replace(0.0, 2.0)
    hotels = hotels[["reviews.text", "reviews.rating"]]
    hotels["reviews.rating"] = hotels["reviews.rating"].astype(int)
    hotels.columns = ["text", "ratings_overall"]
    return hotels


def ta_data_cleaning(df):
    df.columns = ["index", "id", "offering_id", "text", "ratings_overall", "language"]
    ta_data = df[df["language"] == "en"]
    ta_data = ta_data[["text", "ratings_overall"]]
    ta_data["ratings_overall"] = ta_data["ratings_overall"].astype(int)
    return ta_data

def balance_df_comb(df,size=19390):
    shuffle_idx = np.random.permutation(df.shape[0]).tolist()
    X = df.loc[shuffle_idx]
    
    idx_2 = X[X['ratings_overall'] == 2].index
    idx_3 = X[X['ratings_overall'] == 3].index
    idx_4 = X[X['ratings_overall'] == 4].index
    idx_5 = X[X['ratings_overall'] == 5].index

    np.random.seed(10)
    sample_idx_2 = np.random.choice(idx_2,replace=False,size=size)
    sample_idx_3 = np.random.choice(idx_3,replace=False,size=size)
    sample_idx_4 = np.random.choice(idx_4,replace=False,size=size)
    sample_idx_5 = np.random.choice(idx_5,replace=False,size=size)

    X = pd.concat([X.loc[sample_idx_2],
           X.loc[sample_idx_3],
           X.loc[sample_idx_4],
           X.loc[sample_idx_5]],axis=0)
    
    y = X['ratings_overall']
    X = X['text']
    return X,y


def balance_df_ta(df):
#     shuffle_idx = np.random.permutation(df.shape[0]).tolist()
#     X = df.loc[shuffle_idx]
    X = df
    
    idx_2 = X[X['ratings_overall'] == 2].index
    idx_3 = X[X['ratings_overall'] == 3].index
    idx_4 = X[X['ratings_overall'] == 4].index
    idx_5 = X[X['ratings_overall'] == 5].index

    np.random.seed(10)
    sample_idx_2 = np.random.choice(idx_2,replace=False,size=19390)
    sample_idx_3 = np.random.choice(idx_3,replace=False,size=19527)
    sample_idx_4 = np.random.choice(idx_4,replace=False,size=30000)
    sample_idx_5 = np.random.choice(idx_5,replace=False,size=30000)

    X = pd.concat([X.loc[sample_idx_2],
           X.loc[sample_idx_3],
           X.loc[sample_idx_4],
           X.loc[sample_idx_5]],axis=0)
    
    y = X['ratings_overall']
    X = X['text']
    return X,y