# aibuildpack
CFAI Buildpack: Enable Cloud Foundry Artificial Intelligence Project Support
A Hackathon Project at the Cloud Foundry Summit 2019 The Hague
Copyright (c) 2019 DanielWunder, MauriceBrinkmann, SebestyenMiklos


## Usage with example project

1. git clone https://github.com/mauricebrinkmann/aiproject.git
2. cd aiproject
3. cf push ai -b https://github.com/mauricebrinkmann/aibuildpack.git


## General Usage

1. mkdir myAIproject
2. cd myAIproject
3. vi ai.json
```JSON
{
    "data": {
        "my input 1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "my input 2": [0.8, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0],
        "my target": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    },
    "input" : ["my input 1", "my input 2"],
    "target" : "my target"
}
```
3. cf push ai -b https://github.com/mauricebrinkmann/aibuildpack.git
