import numpy as np
import pandas as pd
import os


def readBOW(path='../../data/'):

	print(os.listdir(path))

	data = pd.read_csv('%s/bags.csv'%(path), header=None)

	return data

def readWord2Vec(path='../../data/'):

	print(os.listdir(path))

	data = pd.read_csv('%s/word2vec.csv'%(path), header=None)

	return data

def readNews(path='../../data/'):

	print(os.listdir(path))

	data = pd.read_csv('%s/health.txt'%(path), sep="|", header=None, skiprows=1)
	data.columns = ["id", "publish_date", "headline_test"]

	return data