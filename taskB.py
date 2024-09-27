from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd

# read data
df = pd.read_csv('data.csv')
X = df['review']

# split data into training and test datasets
x, x_, y, y_ = train_test_split(df['review'], df['sentiment'], test_size=0.2)
y = y.map(lambda d: 1 if d == 'positive' else 0)
y_ = y_.map(lambda d: 1 if d == 'positive' else 0)

# initialize and train bag of words vectorizer
vec = CountVectorizer(binary=True)
vec.fit(X)

# initialize and train binary multinomial NB
model = MultinomialNB()
model.fit(vec.transform(x), y)

# compute metrics for test dataset
print('Precision score - ', precision_score(model.predict(vec.transform(x_)), y_))
print('Recall score - ', recall_score(model.predict(vec.transform(x_)), y_))
print('F1 score - ', f1_score(model.predict(vec.transform(x_)), y_))
