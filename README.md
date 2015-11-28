Predicting US Presidential Elections Using Twitter Data
=======================================================

Analysis on current US politics and predicting the next US president using Twitter data, Apache Spark using Python, NLTK, Machine Learning

This analysis helps to predict our future president and can be extended to other political elections prediction systems. These trends would focus on the opinion of people and concern towards their future president, which brings out major problems and issues that people have been facing in a country. Big Data and Machine Learning technologies can be used in real time to help in making decisions based on people’s opinion.

Dependencies:
=============
0. Apache Spark Cluster setup in AWS
```Use the script file spark-ec2.sh in spark disctribution```
0. NLTK
```sudo pip install -U nltk```
0. Numpy
```sudo pip install -U numpy```


Usage:
======
* classifier.py will do sentimental analysis on tweets and classifier tweet based o it's polairty.
The classifer was trained with data srouce(0.8 million tweets) taken from Standford University.

  ```python classfier.py```

* Data was collected from twitter streaming api
  
  ```python streaming.py```

Accuracy of Sentimental Analysis:
======
* ___Accuracy: 0.777321281841___
* F-measure [negative]: 0.768573868488
* F-measure [positive]: 0.785431512272
* Precision [negative]: 0.783972125436
* Precision [positive]: 0.771384136858
* Recall [negative]: 0.753768844221
* Recall [positive]: 0.8

