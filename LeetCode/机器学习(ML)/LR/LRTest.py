# conding :utf-8
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

x_train = np.array([[1, 2, 3],
                    [1, 3, 4],
                    [2, 1, 2],
                    [4, 5, 6],
                    [3, 5, 3],
                    [1, 7, 2]])

y_train = np.array([3, 3, 3, 2, 2, 2])

x_test = np.array([[2, 2, 2],
                   [3, 2, 6],
                   [1, 7, 4]])


clf = LogisticRegression()
clf.fit(x_train, y_train)

# 返回预测标签
print(clf.predict(x_test))

# 返回预测属于某标签的概率
print(clf.predict_proba(x_test))

# [2 3 2]
# [[0.56651809 0.43348191]
#  [0.15598162 0.84401838]
#  [0.86852502 0.13147498]]
# 分析结果：
# 预测[2,2,2]的标签是2的概率为0.56651809，3的概率为0.43348191
#
# 预测[3,2,6]的标签是2的概率为0.15598162，3的概率为0.84401838
#
# 预测[1,7,4]的标签是2的概率为0.86852502，3的概率为0.13147498
