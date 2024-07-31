#include <iostream>

using namespace std;

#define featureCount 4096
#define classCount 64

typedef struct{
    float feature;
    float weight;
}hybridVector;

hybridVector classVector[featureCount];

float featureVector[featureCount] = {0};
float dataset[classCount][featureCount];

void init(){
    for(int i=0;i<featureCount;i++){
        classVector[i].weight = 1;
        classVector[i].feature = 2;
    }
}

void weightSet(bool state,float dist,int featureIndex){
    if(state){
        //increment
        if(classVector[featureCount].weight != 1){

        }
    }
    else{
        //decrement
        
    }
}

void vectorCompressor(float featureVector[]){
    for(int i=1; i<featureCount; i++){
        float weight = classVector[i].weight;
        float feature = classVector[i].feature;
        if(feature == 2 || feature == featureVector[i]){
            //first vector and same feature
            //retain feature
            classVector[i].feature = featureVector[i];
            //increment weight
            weightSet(true,0,i);
        }
        else{
            //Calculate feature distance
            float featureDist = feature - featureVector[i];
            //Calculate effective feature
            
            //set weight
            weightSet(false,featureDist,i);
        }

    }
}

int main(){
    init();
    vectorCompressor(featureVector);
}