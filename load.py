import pandas as pd
import random

df = pd.read_csv('spam.csv', encoding='ISO-8859-1')
df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
df.columns = ['labels', 'data']

param = {}

def message():
    ham_messages = df[df.labels == 'ham'].sample()
    spam_messages = df[df.labels == 'spam'].sample()
    param['ham'] = ham_messages['data'].iloc[0]
    param['spam'] = spam_messages['data'].iloc[0]
    return param