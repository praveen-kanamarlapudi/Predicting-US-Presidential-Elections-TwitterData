Predicting US Presidential Elections Using Twitter Data
=======================================================

Analysis on current US politics and predicting the next US president using Twitter data, Apache Spark using Python, NLTK, Machine Learning

This analysis helps to predict our future president and can be extended to other political elections prediction systems. These trends would focus on the opinion of people and concern towards their future president, which brings out major problems and issues that people have been facing in a country. Big Data and Machine Learning technologies can be used in real time to help in making decisions based on people’s opinion.

### Dependencies:
0. Apache Spark Cluster setup in AWS
```Use the script file spark-ec2.sh in spark distribution```
0. NLTK
```sudo pip install -U nltk```
0. Numpy
```sudo pip install -U numpy```

### Downloading Twitter Data
You can also download more data with ```streaming.py```, which streams data from the search criteria to
standard out.
Run like
```python streaming.py```


*HOWEVER* The downloader requires you to have Twitter API keys to stream the data, as they are private I am not posting in here. Creating new credentials will take no more than 3 mins.

1. Register your Twitter account with http://dev.twitter.com
2. Log in to dev.twitter.com and go to "My applications" (hover over your avatar)
3. Create a new app (gt-big-data, for instance)
4. Create access tokens in the new app.

Replace tags in `streaming.py`

```
access_token = "<access_token>"
access_token_secret = "<access_token_secret>"
consumer_key = "<consumer_key>"
consumer_secret = "<consumer_secret>"
```

### Usage:
* classifier.py will do sentimental analysis on tweets and classifier tweet based on it's polarity.
The classifer was trained with data source(0.8 million tweets) taken from Standford University.

  ```python classifier.py```

* Data was collected from twitter streaming api
  
  ```python streaming.py```


