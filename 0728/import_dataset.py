# 1. import dataset
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])
for i in range(len(iris.target)):
    print("Exanple %d: label %s, feeatures %s" %(i, iris.target[i], iris.data[i]))