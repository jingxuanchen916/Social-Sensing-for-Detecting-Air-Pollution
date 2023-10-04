# Social Sensing for Detecting Air Pollution
This repository contains the main files for my bachelor's dissertation project (submitted in April 2022) at The University of Manchester. The project is supervised by Dr Riza Batista-Navarro and co-supervised by Prof Sarah Lindley.

## Project Introduction
This project aims to explore people's attitudes towards air pollution resulting from wildfire events. Two NLP methods, **Named Entity Recognition (NER)** and **Sentiment Analysis**, are employed for mining social media data from Twitter. All models are developed by fine-tuning pre-trained Transformers.

There are two **NER** models designed to identify disease names mentioned in tweets. Pre-trained models are based on a general clinical corpus, and the fine-tuning dataset is an existing annotated tweet corpus with clinical entities. The best model achieves an accuracy of 98.0%.

There are three **Sentiment Analysis** models. One of them determines whether a tweet is relevant to wildfires (91.3% accuracy), while the other two classify relevant tweets as Positive, Neutral, or Negative (88.9% accuracy). The pre-trained models are all built on a general tweet corpora. Since no suitable fine-tuning dataset existed, we manually annotated 1047 tweets related to the *2018 Saddleworth Moor Wildfire* (the case study).

We apply the above models to analyse 11,527 tweets from the case study and 68,680 tweets related to general wildfire events. The final results are visualised on web dashboards created using Tableau.

## File Structure
As this project was implemented on Google Colab, reproducing models or experiments may require changes to file paths and environment configurations. The project's file structure is organised as follows:

**Notebook**

 - [NER.ipynb](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Notebook/NER.ipynb): the construction of NER models, pre-trained models are [biobert_diseases_ner](https://huggingface.co/alvaroalon2/biobert_diseases_ner) and [bert-base-uncased_clinical-ner](https://huggingface.co/samrawal/bert-base-uncased_clinical-ner).

 - [Sentiment.ipynb](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Notebook/Sentiment.ipynb): the construction of Sentiment Analysis models, pre-trained models are [bertweet-base](https://huggingface.co/vinai/bertweet-base), [twitter-roberta-base-sentiment ](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment) and [bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis).
 - [Prediction.ipynb](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Notebook/Prediction.ipynb): predicting unlabelled tweets using fine-tuned NLP models.


**Script**

 - [tweet_collection.py](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Script/tweet_collection.py): collecting tweets via the Twitter API and storing them in MongoDB.
 - [tweet_csv.py](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Script/tweet_csv.py): reading tweets from MongoDB and exporting them to CSV files.


**Data**

 - NER/[medinfo2015.linejson](https://github.com/IBMMRL/medinfo2015/blob/162f6f1dd4f5f162bea02a62d2cb393f3ac605d4/medinfo2015.linejson): the original fine-tuning data for NER models (extracted from [IBMMRL](https://github.com/IBMMRL)/[medinfo2015](https://github.com/IBMMRL/medinfo2015)), containing 1300 tweets and their clinical entities.
 - Sentiment/[annotated_tweets.xlsx](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Data/Sentiment/annotated_tweets.xlsx): the annotated fine-tuning data for Sentiment Analysis models, containing 1047 tweets and their sentiments (irrelevant/positive/neural/negative).
 - [Prediction](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/tree/main/Data/Prediction): unlabelled tweets for prediction, consisting of two sub-folders for the case study and general wildfire events.
	 - Case Study/[saddleworth.csv](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Data/Prediction/Case%20Study/saddleworth.csv): 11,527 tweets that contain the keyword ``saddleworth`` between *22/06/2018* and *21/07/2018*.
	 - [General](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/tree/main/Data/Prediction/General)/[year]_[month]_wildfire_air.csv: 68,680 tweets stored month by month, which contain the keywords ``wildfire`` AND  ``air`` between *01/01/2017* and *31/12/2021*.
 - Air Quality/[Case Study_Tameside Mottram Moor.csv](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Data/Air%20Quality/Case%20Study_Tameside%20Mottram%20Moor.csv): PM10 data monitored by the Tameside Mottram Moor station (the one closest to Saddleworth) between *22/06/2018* and *21/07/2018* (downloaded from [Air Quality in England](https://www.airqualityengland.co.uk)).



**Dashboard**

 - [Case Study.pdf](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Dashboard/Case%20Study.pdf): dashboards for the case study, showing
	 - the number of tweets and air quality measurements over time;
	 - tweets' sentiments linked to clinical entities;
	 - tweets' sentiments and their locations;
	 - the distribution of tweets' sentiments with the most frequent topics.
 - [General.pdf](https://github.com/jingxuanchen916/Social-Sensing-for-Detecting-Air-Pollution/blob/main/Dashboard/General.pdf): dashboards for general wildfire events, showing
	 - the number of tweets over time;
	 - the most frequent clinical entities linked to sentiments;
	 - the distribution of tweets' sentiments and their locations.
