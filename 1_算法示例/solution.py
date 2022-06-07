import operator
from math import log


# 计算信息熵
def calcShannonEnt(dataSet):
    # 样本数
    numEntries = len(dataSet)
    # 创建一个数据字典：key是最后一列的数值（即标签），value是属于该类别的样本个数
    labelCounts = {}
    # 遍历整个数据集，每次取一行
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    # 初始化信息熵
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        # 计算信息熵
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 按给定的特征划分数据，axis是数据集中特征的列号，value是该列下某个特征值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选取当前数据集下最优特征
def chooseBestFeatureToSplit(dataSet):
    # 获取当前数据集的特征个数，最后一列是分类标签
    numFeatures = len(dataSet[0]) - 1
    # 计算当前数据集的信息熵
    baseEntropy = calcShannonEnt(dataSet)
    # 初始化最优信息增益和最优的特征
    bestInfoGain = 0
    bestFeature = -1
    # 遍历每个特征
    for i in range(numFeatures):
        # 获取数据集中当前特征下的所有值
        featList = [example[i] for example in dataSet]
        # 获取当前特征值
        uniqueVals = set(featList)
        # 计算每种划分方式的信息熵
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        # 计算信息增益
        infoGain = baseEntropy - newEntropy
        # 选取最优的信息增益
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

# 返回样本中出现次数最多的类别标签
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1),
                              rse=True)
    return sortedClassCount[0][0]


# 生成决策树
def createTree(dataset, labels):
    # 当前数据集下标签列所有值
    classlist = [buy_computers[-1] for buy_computers in dataset]
    # 当类别完全相同时则停止继续划分，直接返回该类的标签
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    # 没有剩余属性变量可以用来进一步分裂样本
    if len(dataset[0]) == 1:
        return majorityCnt(classlist)
    # 获取最优的分类特征
    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    # 使用字典来存储树信息，在当前数据集选取最优的特征存储在bestFeat中
    myTree = {bestFeatLabel: {}}
    # 删除已经选取的特征
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        # 递归的生成决策树
        myTree[bestFeatLabel][value] = createTree(
            splitDataSet(dataset, bestFeat, value), subLabels)
    return myTree


if __name__ == "__main__":
    # 数据集
    dataset = [['<=30', 'high', 'no', 'fair', 'no'],
               ['<=30', 'high', 'no', 'excellent', 'no'],
               ['31...40', 'high', 'no', 'fair', 'yes'],
               ['>40', 'medium', 'no', 'fair', 'yes'],
               ['>40', 'low', 'yes', 'fair', 'yes'],
               ['>40', 'low', 'yes', 'excellent', 'no'],
               ['31...40', 'low', 'yes', 'excellent', 'yes'],
               ['<=30', 'medium', 'no', 'fair', 'no'],
               ['<=30', 'low', 'yes', 'fair', 'yes'],
               ['>40', 'medium', 'yes', 'fair', 'yes'],
               ['<=30', 'medium', 'yes', 'excellent', 'yes'],
               ['31...40', 'medium', 'no', 'excellent', 'yes'],
               ['31...40', 'high', 'yes', 'fair', 'yes'],
               ['>40', 'medium', 'no', 'excellent', 'no']]
    # 标签
    labels = [
        'age', 'income', 'student', 'credit_rating', 'Class:buy_computer'
    ]
    # 以字典形式输出决策树
    print(createTree(dataset, labels))
