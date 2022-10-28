import pandas as pd
import numpy as np
import random
import operator
import math
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


def initializeMembershipMatrix():  # initializing the membership matrix
    membership_mat = []
    for i in range(n):
        random_num_list = [random.random() for i in range(k)]
        summation = sum(random_num_list)
        temp_list = [x/summation for x in random_num_list]

        flag = temp_list.index(max(temp_list))
        for j in range(0, len(temp_list)):
            if (j == flag):
                temp_list[j] = 1
            else:
                temp_list[j] = 0

        membership_mat.append(temp_list)
    return membership_mat


def calculateClusterCenter(membership_mat):  # calculating the cluster center
    cluster_mem_val = list(zip(*membership_mat))
    cluster_centers = []
    for j in range(3):
        x = list(cluster_mem_val[j])
        xraised = [p ** m for p in x]
        denominator = sum(xraised)
        temp_num = []
        for i in range(n):
            data_point = list(df.iloc[i])
            prod = [xraised[i] * val for val in data_point]
            temp_num.append(prod)
        numerator = map(sum, list(zip(*temp_num)))
        center = [z/denominator for z in numerator]
        cluster_centers.append(center)
    return cluster_centers


# Updating the membership value
def updateMembershipValue(membership_mat, cluster_centers):
    p = float(2/(m-1))
    for i in range(n):
        x = list(df.iloc[i])
        distances = [np.linalg.norm(
            np.array(list(map(operator.sub, x, cluster_centers[j])))) for j in range(k)]
        for j in range(k):
            den = sum([math.pow(float(distances[j]/distances[c]), p)
                      for c in range(k)])
            membership_mat[i][j] = float(1/den)
    return membership_mat


def getClusters(membership_mat):  # getting the clusters
    cluster_labels = list()
    for i in range(n):
        max_val, idx = max((val, idx)
                           for (idx, val) in enumerate(membership_mat[i]))
        cluster_labels.append(idx)
    return cluster_labels
\
def fuzzyCMeansClustering():  # Third iteration Random vectors from data
    # Membership Matrix
    membership_mat = initializeMembershipMatrix()
    curr = 0
    acc = []
    while curr < MAX_ITR:
        cluster_centers = calculateClusterCenter(membership_mat)
        membership_mat = updateMembershipValue(membership_mat, cluster_centers)
        cluster_labels = getClusters(membership_mat)

        acc.append(cluster_labels)

        if (curr == 0):
            print("Cluster Centers:")
            print(np.array(cluster_centers))
        curr += 1
    print("---------------------------")
    print("Partition matrix:")
    print(np.array(membership_mat))
    #return cluster_labels, cluster_centers
    return cluster_labels, cluster_centers, acc

df_data = pd.read_csv("Iris.csv")
print(df_data.head())

df_data = df_data.drop(['Id'], axis=1)
columns = list(df_data.columns)
features = columns[:len(columns)-1]
class_labels = list(df_data[columns[-1]])
df = df_data[features]

k = 3
MAX_ITR = 100
n = len(df)
print(n)
m = 1.7 #fuzzy-parameter (if its 1 it is same as K-nn)


#Sepal Plot
plt.figure(figsize=(10,10)) #scatter plot of sepal length vs sepal width
plt.scatter(list(df.iloc[:,0]), list(df.iloc[:,1]), marker='o')
plt.axis('equal')
plt.xlabel('Sepal Length', fontsize=16)
plt.ylabel('Sepal Width', fontsize=16)
plt.title('Sepal Plot', fontsize=22)
plt.grid()
plt.show()

#Petal plot
plt.figure(figsize=(10, 10))  # scatter plot of petal length vs sepal width
plt.scatter(list(df.iloc[:, 2]), list(df.iloc[:, 3]), marker='o')
plt.axis('equal')
plt.xlabel('Petal Length', fontsize=16)
plt.ylabel('Petal Width', fontsize=16)
plt.title('Petal Plot', fontsize=22)
plt.grid()
plt.show()

membership_mat = initializeMembershipMatrix()
print(calculateClusterCenter(membership_mat))

labels, centers, acc = fuzzyCMeansClustering()
print(labels)
print(centers)

seto = max(set(labels[0:50]), key=labels[0:50].count)
vers = max(set(labels[50:100]), key=labels[50:100].count)
virg = max(set(labels[100:]), key=labels[100:].count)

s_mean_clus1 = np.array([centers[seto][0],centers[seto][1]])
s_mean_clus2 = np.array([centers[vers][0],centers[vers][1]])
s_mean_clus3 = np.array([centers[virg][0],centers[virg][1]])
print(s_mean_clus1)



values = np.array(labels) #label

#search all 3 species
searchval_seto = seto
searchval_vers = vers
searchval_virg = virg

#index of all 3 species
ii_seto = np.where(values == searchval_seto)[0]
ii_vers = np.where(values == searchval_vers)[0]
ii_virg = np.where(values == searchval_virg)[0]
ind_seto = list(ii_seto)
ind_vers = list(ii_vers)
ind_virg = list(ii_virg)



sepal_df = df_data.iloc[:,0:2]



seto_df = sepal_df[sepal_df.index.isin(ind_seto)]
vers_df = sepal_df[sepal_df.index.isin(ind_vers)]
virg_df = sepal_df[sepal_df.index.isin(ind_virg)]



cov_seto = np.cov(np.transpose(np.array(seto_df)))
cov_vers = np.cov(np.transpose(np.array(vers_df)))
cov_virg = np.cov(np.transpose(np.array(virg_df)))

sepal_df = np.array(sepal_df)



x1 = np.linspace(4,8,150)
x2 = np.linspace(1.5,4.5,150)
X, Y = np.meshgrid(x1,x2)

Z1 = multivariate_normal(s_mean_clus1, cov_seto)
Z2 = multivariate_normal(s_mean_clus2, cov_vers)
Z3 = multivariate_normal(s_mean_clus3, cov_virg)

pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y

plt.figure(figsize=(10,10))
plt.scatter(sepal_df[:,0], sepal_df[:,1], marker='o')
plt.contour(X, Y, Z1.pdf(pos), colors="r" ,alpha = 0.5)
plt.contour(X, Y, Z2.pdf(pos), colors="b" ,alpha = 0.5)
plt.contour(X, Y, Z3.pdf(pos), colors="g" ,alpha = 0.5)
plt.axis('equal')
plt.xlabel('Sepal Length', fontsize=16)
plt.ylabel('Sepal Width', fontsize=16)
plt.title('Final Clusters(Sepal)', fontsize=22)
plt.grid()
plt.show()

p = float(2 / (m - 1))
for i in range(n):
    x = list(df.iloc[i])
    distances = [np.linalg.norm(np.array(list(map(operator.sub, x, centers[j])))) for j in range(k)]
    print(distances)
    for j in range(k):
        den = sum([math.pow(float(distances[j] / distances[c]), p) for c in range(k)])
        membership_mat[i][j] = float(1 / den)