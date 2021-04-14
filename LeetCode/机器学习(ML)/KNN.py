from numpy import *
import operator
import time
import matplotlib.pyplot as plt
from collections import *

"""
1. tile函数：（铺）瓷砖，tile(A, reps): ———–> Construct an array by repeating A the number of times given by reps.
2. argsort函数：根据值的大小排序返回对应元素原来索引位置（从0开始），如[3, 1, 2]排序后为[1,2,3]原来的索引为：[1,2,0]
3. operator.itemgetter(1)：对数组第一维元素进行排序
"""


def kNN(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 计算横纵坐标差
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    print(diffMat)
    # 坐标差平方
    sqDiffMat = diffMat ** 2
    print(sqDiffMat)
    # 坐标差平方和
    sqDistances = sqDiffMat.sum(axis=1)
    # 平方和开根号
    distances = sqDistances ** 0.5
    # 返回从小到大排序后对应的索引
    sortedDistIndicies = distances.argsort()
    print(sqDistances)
    print(sortedDistIndicies)

    classCount = Counter()
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        print(i, sortedDistIndicies[i], voteIlabel)
        # classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        classCount[voteIlabel] +=1
    print(classCount)
    res=classCount.most_common(1)
    print(res[0][0])
    # sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # return sortedClassCount[0][0]
    return res[0][0]


# kNN Example
group = array([[1.0, 1.1], [0.6, 0.6], [0, 0], [0, 0.1], [1.0, 1.0]])
labels = ['B', 'A', 'A', 'A',  'B']

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(group[:2, 0], group[:2, 1], s=70, color='b')
ax.scatter(group[2:5, 0], group[2:5, 1], s=70, color='r')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

res = kNN([0.3, 0.2], group, labels, 3)
print(res)
# out：'B' 说明[0.3,0.2]这个点属于B类
