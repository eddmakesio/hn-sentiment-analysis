import sqlite3

con = sqlite3.connect("./db/hn_sentiment_analysis.db")

def evaluate_sentimental_analysis(start_time=0, end_time=0):
    if start_time == 0 and end_time == 0:
        return 0

    cur = con.cursor()
    result = cur.execute("SELECT polarity, subjectivity FROM comment WHERE created > start_time AND created <= end_time")
    return result
