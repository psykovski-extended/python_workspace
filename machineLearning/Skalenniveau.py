import numpy as np

np.random.seed(42)

fString = open('D:\\Coding\\MachineLearningWorkspace\\diagnosis.data', 'r')
fFloat = open('D:\\Coding\\MachineLearningWorkspace\\diagnosis.csv', 'w')
for line in fString:
    line = line.replace(',', '.')
    line = line.replace('\t', ',')
    line = line.replace('yes', '1')
    line = line.replace('no', '0')
    line = line.replace('\r\n', '\n')
    fFloat.write(line)
fString.close()
fFloat.close()

fFloat = open('D:\\Coding\\MachineLearningWorkspace\\diagnosis.csv', 'r')
dataset = np.loadtxt(fFloat, delimiter=',')
fFloat.close()

X = dataset[:, 1:6]
Y = dataset[:, 6]
allData = np.arange(0, X.shape[0])
iTesting = np.random.choice(X.shape[0], int(X.shape[0]*0.2), replace=False)
iTraining = np.delete(allData, iTesting)
dataRecords = len(iTraining)
XTrain = X[iTraining, :]
YTrain = Y[iTraining]
