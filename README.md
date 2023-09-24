# HN Sentiment Analysis

Is HN as negative as it seems?

This project scrapes the best stories of HN, takes the stories comments, and puts it into a sqlite3 database. Using TextBlob, a Python NLP library, we analyze the sentimental polarity and subjectivity of the comment (polarity is between -1 and 1 where -1 is negative and 1 is positive, subjectivity is between 0 and 1 where 0 is not subjective and 1 is very subjective). The sqlite3 schema can be found in `./db/sql/hn_sentimental_analysis.db`. The DB can be setup with `python ./db/scripts/setup_sqlite3.py`. 

This is still a WIP :) 
