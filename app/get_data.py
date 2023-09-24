import requests
import sqlite3

con = sqlite3.connect("./db/hn_sentiment_analysis.db")

API = "https://hacker-news.firebaseio.com/v0"

def get_best_stories():
    try: 
        r = requests.get(f"{API}/topstories.json")
        return r.json()
    except:
        print(f"Unable to get top stories")

def get_story_data(story_id: int):
    try: 
        r = requests.get(f"{API}/item/{story_id}.json")
        return r.json()
    except:
        print(f"Unable to get story #{story_id}")

def get_stories_comments(story_id: int):
    try: 
        r = requests.get(f"{API}/item/{story_id}.json")
        comment_ids = r.json()["kids"]

        comments = []

        for comment_id in comment_ids:
            r = requests.get(f"{API}/item/{comment_id}.json")
            comments.append(r.json())

        return comments
    except:
        print(f"Unable to get comments for story #{story_id}")

def save_story(story):
    try: 
        cur = con.cursor()
        sql_query = "INSERT OR IGNORE INTO story (hn_story_id, title, created) VALUES(?, ?, ?)"
        insert_data = (story["id"], story["title"], story["time"])
        cur.execute(sql_query, insert_data)
        con.commit()
        cur.close()
    except: 
        print(f"Unable to save story #{story['id']}: {story}")

def save_comment(comment):
    try: 
        cur = con.cursor()
        sql_query = "INSERT OR IGNORE INTO comment (hn_comment_id, hn_story_id, contents, created) VALUES(?, ?, ?, ?)"
        insert_data = (comment["id"], comment["parent"], comment["text"], comment["time"])
        cur.execute(sql_query, insert_data)
        con.commit()
        cur.close()
    except:
        print(f"Unable to save comment #{comment['id']}: {comment}")

if __name__ == '__main__':    
    best_stories = get_best_stories()
    for story_id in best_stories:
        print(f'Saving story #{story_id}...')
        story = get_story_data(story_id)
        save_story(story)
        comments = get_stories_comments(story["id"])
        for comment in comments:
            print(f'Saving comment #{comment["id"]}...')
            save_comment(comment)
