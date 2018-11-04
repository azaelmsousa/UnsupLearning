import numpy as np
import pandas as pd
import sklearn
from sklearn.metrics import davies_bouldin_score, calinski_harabaz_score, silhouette_score

def applyAllMetrics(X,y_pred):

	applyDaviesBouldinScore(X,y_pred)
	applyCalinskiScore(X,y_pred)
	applySilhouetteScore(X,y_pred)

def applyDaviesBouldinScore(X,y_pred):

	score_db = davies_bouldin_score(X,y_pred)
	print("Davies Bouldin")
	print(score_db+"\n")

def applyCalinskiScore(X,y_pred):

	score_ch = calinski_harabaz_score(X,y_pred)
	print("Calinski and Harabaz")
	print(score_ch+"\n")

def applySilhouetteScore(X,y_pred):

	score_s = silhouette_score(X,y_pred)
	print("Silhouette Score")
	print(score_s+"\n")