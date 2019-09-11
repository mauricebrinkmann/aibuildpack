# aibuildpack  
  
CFAI Buildpack: Enable Cloud Foundry Artificial Intelligence Project Support  
    A Hackathon Project at the Cloud Foundry Summit 2019 The Hague  
Copyright (c) 2019 DanielWunder, MauriceBrinkmann, SebestyenMiklos  
  
  
## Usage with example project  
```BASH
git clone https://github.com/mauricebrinkmann/aiproject.git
cd aiproject
cf push
```
  
## General Usage  
```BASH
mkdir myAIproject
cd myAIproject
vi ai.json
```
```JSON
{
    "data": {
        "input 1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "input 2": [0.8, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
        "target": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    },
    "input" : ["input 1", "input 2"],
    "target" : "target"
}
```
```BASH
cf push ai -b https://github.com/mauricebrinkmann/aibuildpack.git
```
  
Note: You can change the name of the inputs and the target within the "data" set, as long as you reference those names with the "input" and "target" fields:
```JSON
{
    "data": {
        "factor x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "factor y": [0.8, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
        "factor z": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        "mystical": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    },
    "input" : ["factor x", "factor y", "factor z"],
    "target" : "mystical"
}
```
   
## Test  
  
Assuming that ai.example.com will be the route to the previously pushed AI project using this aibuildpack:
```BASH
# Check the model to equal the pushed ai.json
curl https://ai.example.com/model

# Check the model by predicting some values
curl -X POST -d '{ "input 1": [ 1, 2, 3 ], "input 2": [ 0.4, 0.5, 0.6 ] }' https://ai.example.com
```
Returns:  
```JSON
{
    "prediction": [
        9.999999999999957,
        19.999999999999975,
        29.999999999999996
    ]
}
```
   
```BASH
# Check the model by predicting some other values
curl -X POST -d '{ "input 1": [ 1, 1.5, 3 ], "input 2": [ 0.4, 0.5, 0.7 ] }' https://ai.example.com
```
Returns:  
```JSON
{
    "prediction": [
        9.999999999999957,
        14.999999999999973,
        30.000000000000007
    ]
}
```
