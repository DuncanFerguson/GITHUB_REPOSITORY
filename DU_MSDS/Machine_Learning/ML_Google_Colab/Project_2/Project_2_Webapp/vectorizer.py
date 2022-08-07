import os
from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
cur_dir = os.path.dirname(__file__)
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'stopwords.pkl'), 'rb'))

def preprocessor(text):
  """This preprocessing function removes all the punctuation"""
  # Removing all the punctuation
  text = re.sub('<[^>]*>', '', text)
  emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
  text = (re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')).strip()
  return text

# Note that the tokenizing is set up for a pipeline run. 
def tokenizer_porter(text):
  """Tokenizing and porting"""
  return [porter.stem(word) for word in text.split()]

vect = HashingVectorizer(decode_error='ignore',
                         n_features=2*22,
                         norm='l2',
                         ngram_range=(1,2),
                         preprocessor=preprocessor,
                         tokenizer=tokenizer_porter,
                         stop_words=stop)