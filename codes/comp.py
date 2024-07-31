import numpy as np
import glob as g

path ="/home/ds-lab/Downloads/class/vectors/Anhui_Barberry/"
featureCount = 4096


classVector1 = [2.0]*featureCount
weights1 = [0.0]*featureCount

classVector2 = [2.0]*featureCount
weights2 = [0.0]*featureCount

hybridVector1 = [[]]*2
hybridVector2 = [[]]*2

variationFactor = 0.005

dataset = []

featurePath = g.glob(path+'*')
for data in featurePath:
    print(data)
    featureVector = np.load(data)
    
    for i in range(featureCount):
        if classVector1[i]==2:
            classVector1[i]=featureVector[0][i]
            
        elif classVector1[i]==featureVector[0][i]:
                weights1[i]+=variationFactor
        
        elif classVector1[i]!=featureVector[0][i]:
                weights1[i]-=variationFactor
hybridVector1[0] = classVector1
hybridVector1[1] = weights1

dataset.append(hybridVector1)


path ="/home/ds-lab/Downloads/class/vectors/Big-fruited_Holly/"

featurePath = g.glob(path+'*')
for data in featurePath:
    print(data)
    featureVector = np.load(data)
    
    for i in range(featureCount):
        if classVector2[i]==2:
            classVector2[i]=featureVector[0][i]
            
        elif classVector2[i]==featureVector[0][i]:
            if weights2[i] < 1:
                weights2[i]+=variationFactor
        
        elif classVector2[i]!=featureVector[0][i]:
            if weights2[i] > 0:
                weights2[i]-=variationFactor
hybridVector2[0] = classVector2
hybridVector2[1] = weights2

dataset.append(hybridVector2)

classSep = [0.0]*featureCount
for i in range(featureCount):
    classSep[i] = classVector1[i]*weights1[i]-classVector2[i]*weights2[i]

print(classSep)
