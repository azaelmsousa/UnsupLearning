# Unsupervised Learning

This is the third project of the Machine Learning subject (MO444) and it approaches unsupervised learning techniques for the clustering of news.

---

## Activities

1. Discover the number of groups present in the data or a reliable range of possible values. Do some experiments in this regard.
2. Analyze the medoids of some groups (for example, 3 groups) and their closest neighbors in the groups. Do they make sense? Are they talking about the same type of documents?
3. Think of possible ways of checking the validity/quality of your clusters.
4. Re-do the best experiment above considering the PCA dimensionality reduction. Consider different energies (variance) to cut and reduce dimensionality. What are the conclusions when using PCA in this problem?
5. Prepare a 4-page (max.) report with all your findings. It is UP TO YOU to convince the reader that you are proficient on Unsupervised Learning Techniques, and the choices it entails.

## Dataset

Health News in Twitter (<https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter#>), from
UCI Machine Learning Repository, is a dataset collected in 2015 using Twitter API.
Dataset Information:

* The health news are from BBC (’bbchealth.txt’), CNN (’cnnhealth.txt’), Fox News (’foxnewshealth.txt’) and Everyday News (’everydayhealth.txt’).
* Each file is related to one Twitter account of a news agency. For example, bbchealth.txt is related to BBC health news. Each line contains tweet id|date and time|tweet. The separator is ’|’.
* There are 13,229 health news (’health.txt’). The bag-of-words features vectors (with 1,203 dimensions) representing each new are also available ’bags.csv’) as well the word2vec vectors (with 128 dimensions, ’word2vec.csv’). You should choose one.
* The data is available at: <https://www.dropbox.com/s/ahkim9u103v0q9i/health-dataset.zip> 

---

## Planning

1. Develop an EDA to understand the basics of the dataset `notebooks\EDA.ipynb`
2. Define metrics for the model evaluation and create a flow for that matter.
    * Elbow: For the defition of the cluster numbers.
    * Silhuette: Identify the coesion of the cluster centroids.
    * Davies Bouldin: To measure the centroids's separation.
    * Scatter plots: Used to visualize the clusters separtions and its bellonging instances.
    * Cosine: Use cosine as a distance metric for the centroids to avoid problems with the vector norm.
    * Kullback Leiber Divergence: A non-euclidian evaluation for the model.
    * References: <http://www.ims.uni-stuttgart.de/institut/mitarbeiter/schulte/theses/phd/algorithm.pdf>
3. Analyze centroids.
    * Number of centroids from 3 to 10.
    * Distance metrics (cosine, euclidian).
    * Clustering measures (mean, median and `point`).
4. Apply PCA as a Dimensionality Reduction.
    * Redo all above experiments.