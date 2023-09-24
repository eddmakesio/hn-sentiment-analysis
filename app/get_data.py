import requests
import sqlite3


con = sqlite3.connect("./db/hn_sentiment_analysis.db")

API = "https://hacker-news.firebaseio.com/v0"

def get_best_stories():
    r = requests.get(f"{API}/topstories.json")
    return r.json()

def get_story_data(story_id: int):
    r = requests.get(f"{API}/item/{story_id}.json")
    return r.json()

def get_stories_comments(story_id: int):
    r = requests.get(f"{API}/item/{story_id}.json")
    comment_ids = r.json()["kids"]

    comments = []

    for comment_id in comment_ids:
        r = requests.get(f"{API}/item/{comment_id}.json")
        comments.append(r.json())

    return comments

if __name__ == '__main__':
    cur = con.cursor()
    
    best_stories = get_best_stories()
    comments = get_stories_comments(best_stories[0])
    print(comments)
