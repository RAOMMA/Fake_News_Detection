#import libraries
import re
import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import joblib
model=joblib.load('C:/salman/ML/fake news/nlppr.joblib')

stop_words = set(stopwords.words('english'))


import argparse

parser = argparse.ArgumentParser()

#take value with argparser
parser.add_argument('-value',type=str,default="House Dem Aide: We Didn’t Even See Comey’s Letter Until Jason Chaffetz Tweeted It")

args = parser.parse_args()


tweet=args.value


def remove_sp(tweet):
    tweet=re.sub('\[.*?\]',' ',tweet)
    tweet = re.sub('@[^\s]+','',tweet)
    tweet = re.sub('http[^\s]+','',tweet)
    tweet=re.sub('\n',' ',tweet)
    tweet=re.sub('\w*\d\w*',' ',tweet)
    tweet=re.sub('[%s]'%re.escape(string.punctuation)," ",tweet)
    return tweet

ps = PorterStemmer()
def stre(data):
    corpus = []
    for i in range(0, len(data)):
        review = re.sub('[^a-zA-Z0-9]',' ', str(data))
        review = review.lower()
        review = review.split()

        review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
        review = ' '.join(review)
        corpus.append(review)
    return corpus


import pandas as pd

x=remove_sp(tweet)
x=stre(x)




# Convert the string to a Pandas Series
x = pd.Series(x)

from sklearn.feature_extraction.text import TfidfVectorizer
loaded_vectorizer = joblib.load('C:/salman/ML/fake news/tfidf_vectorizer.pkl')
X_new_transformed = loaded_vectorizer.transform(x).toarray() 
tf_x=pd.DataFrame(X_new_transformed)
pre=model.predict(tf_x)[0]
if pre==0:
    print("Reliable")
else:
    print("Unreliable")




