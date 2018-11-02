import numpy as np
import pandas as pd
import sklearn 
import os


def readBOW(path='../../data/'):

	print(os.listdir(path))

	data = pd.read_csv('%s/bags.csv'%(path), header=None)

	data = sklearn.preprocessing.normalize(data, axis=1)
	return data

def readWord2Vec(path='../../data/'):

	print(os.listdir(path))

	data = pd.read_csv('%s/word2vec.csv'%(path), header=None)

	data = sklearn.preprocessing.normalize(data, axis=1)

	return data

def readNews(path='../../data/'):

	print(os.listdir(path))

	data = pd.read_csv('%s/health.txt'%(path), sep="|", header=None, skiprows=1, encoding='utf8')
	data.columns = ["id", "publish_date", "headline_test"]
	print("Read {} lines".format(data.shape[0]))

	return data