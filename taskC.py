from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

# implement naive bayes
class MulNB:
	def __init__(self, laplace=1, classes=2):
		self.classes = classes
		self.laplace = laplace
		self.prob_c = [0 for i in range(classes)]
		self.prob_x = [{} for i in range(classes)] 
	
	# p(x1 | c) = count(x1 & c) / count(c)
	def fit(self, x, y):
		for i in range(self.classes):
			self.prob_c[i] = x[y == i].sum() / x.sum() # count(any tokens | class i) / count(any tokens)

			for j in range(x.shape[1]):
				self.prob_x[i][j] = (x[y == i][:, j].sum() + self.laplace) / (y[y == i].size + x.shape[1] * self.laplace)
			
	# predict p(x1, x2, ... | c) = ln( p(x1 | c) ) + ln( p(x2 | c) ) + ...
	def predict(self, x):
		x = x.toarray()
		ret = np.zeros((x.shape[0], self.classes))

		for i in range(self.classes):
			for k in range(x.shape[0]):
				for j in range(x.shape[1]):
					if x[k, j] != 0:
						ret[k, i] += np.log(x[k, j]) + np.log(self.prob_x[i][j])

			ret[k, i] += np.log(self.prob_c[i])

		return ret.argmax(axis=1)


if __name__=='__main__':
	vec = CountVectorizer(binary=True)

	# read IMBD data
	df = pd.read_csv('data.csv')[:3000]
	X = df['review']
	Y = df['sentiment'].map(lambda x: 0 if x == 'negative' else 1)

	# train vectorizer
	vec.fit(X)

	# split into train and test data sets
	x, x_, y, y_ = train_test_split(X, Y, test_size=0.2, shuffle=True)

	model = MulNB()
	model.fit(vec.transform(x), y)

	y_pred = model.predict(vec.transform(x_))
	y_true = y_

	# compute metrics for test dataset
	print('Precision score - ', precision_score(y_pred, y_true))
	print('Recall score - ', recall_score(y_pred, y_true))
	print('F1 score - ', f1_score(y_pred, y_true))

