import pickle
import random
import pandas as pd
import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from string import punctuation
from nltk.corpus import stopwords

lemm = WordNetLemmatizer()

bot_name = "Disease Predictor"

with open('trained_model.pkl', 'rb') as f:
    vectorizer, lg, svm, mlp, encode = pickle.load(f)

remove = ['also', 'lot', 'really', 'along', 'like', 'feel', 'become', 'experiencing', 'get',
          'often', 'sometimes', 'go', 'making', 'seem', 'causing', 'feeling', 'lately', 'recently', 'quite']

stop = stopwords.words("english")
punctuation = word_tokenize(punctuation)
stop = stop + punctuation + ['.', "'ve", "'m", "'s", "n't"]

def clean_text(text):
    token = word_tokenize(text.lower())
    words = [lemm.lemmatize(word) for word in token if word not in stop]
    words = [word for word in words if word not in remove]
    new_text = " ".join(words)
    return new_text


suggestions = pd.read_excel('./suggestions.xlsx')
suggestions.columns = suggestions.columns.str.strip()
suggestions = suggestions.set_index('Disease')


def predict(text):
    text = [clean_text(text)]
    row_vector = vectorizer.transform(text).toarray()
    p1 = lg.predict(row_vector)
    p2 = svm.predict(row_vector)
    p3 = mlp.predict(row_vector)

    # Ensemble method - combining the thre predictions - choosing the most common predicted class
    if p1 == p2 == p3:
        p = p1
    elif p1 == p2:
        p = p1
    elif p1 == p3:
        p = p1
    elif p2 == p3:
        p = p2
    else:
        p = p2
    disease = encode.inverse_transform(p)
    result = ("According to the disease prediction model, you are suffering from " + disease + ". The suggested steps are - " +
              suggestions.at[disease[0], 'Suggestion'] + " Consult your doctor if your contition worsens.")
    return result[0]


def get_response(msg): 
    return predict(msg)
