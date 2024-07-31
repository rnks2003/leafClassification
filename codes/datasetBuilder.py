import numpy as np
import glob as g
import csv

def datasetBuilder():
    dirPath = 'D:/AI043/Leaf Classification/assets/FeatureVector'
    classPath = g.glob(dirPath+'/*')
    
    classes = []
    data = []
    dataset = []
    
    for clss in classPath:
        readPath = clss +'/*'
        
        className = clss.replace(dirPath+'\\','')
        classes.append(className)
        
        featuresPath = g.glob(readPath)
        
        for f in featuresPath:
            featureVector = np.load(f)
            data = featureVector.tolist()
            data[0].append(className)
            #print(len(data[0]))
            dataset.append(data)
    return dataset

set = datasetBuilder()

header = []

for i in range(1,4097):
    header.append("feature "+str(i))
header.append("class")

with open('dataset.csv', 'w') as f:
     
    write = csv.writer(f)
     
    write.writerow(header)
    write.writerows(set)
