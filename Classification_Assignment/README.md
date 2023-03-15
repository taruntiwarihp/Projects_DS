## Problem Statement.
  * Vehicle Logos (Image Classification) with an imbalanced dataset and wrong annotations.
  
#### We solved the imbalance problem using assigning class weights and wrong annotations using added attention layer as a penalty added to the loss function.

### Overall

| Model Type            | Accuracy           | Precision          | Recall             | F1 Score           | Params             | Latency            |    
|-----------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| ResNet50              | 0.9111111111111111 | 0.8688248385478594 | 0.8947673046951575 | 0.8713540581705433 | 23565404           | 0.2274312973022461 |
| MobileNet             | 0.75               | 0.7426052897235449 | 0.7604792961160813 | 0.7315722419273002 | 2259740            | 0.01093912124633789|
| SWIN                  | 0.8861111111111111 | 0.8214367944147357 | 0.8432166660370441 | 0.822309550392583  | 27540886           | 0.43773937225341797|
| AttentionEfficientNet | 0.7329545454545454 | 0.7092061499486313 | 0.6934227800778768 | 0.6838596462150024 | 11404500           | 0.32543545525345435|
| EfficientNetV2S       | 0.9277777777777778 | 0.8897694604157452 | 0.8874862444977991 | 0.8843419289090997 | 20213356           | 0.2312171459197998 |


<img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/Accuracy.png'> <img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/f1_score.png'>
<img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/precision.png'> <img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/recall.png'>
<img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/train_loss.png'> <img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/val_loss.png'>


* Confusion Matrix
<img src = 'https://github.com/taruntiwarihp/Projects_DS/blob/master/Classification_Assignment/plots/confusion_matrix.png'>

