import psycopg2
from datetime import datetime

from textblob import TextBlob

def connect_to_db():
    return psycopg2.connect(
        dbname='qmcjdcgq',
        user='qmcjdcgq',
        password='4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
        host='flora.db.elephantsql.com',
        port='5432'
    )


class AntisemitismAnalyzer:
    def __init__(self, db_conn):
        self.conn = db_conn



    def get_patterns(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT pattern_text FROM patterns")
            return [row[0] for row in cursor.fetchall()]


    def analyze_post(self, post_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT post_text FROM posts WHERE post_id = %s", (post_id,))
            post_text = cursor.fetchone()
            if not post_text:
                print("Post not found.")
                return
            post_text = post_text[0]

        patterns = self.get_patterns()
        blob = TextBlob(post_text.lower())
        words_in_post = blob.words

        # print(words_in_post)
        matches = sum(1 for pattern in patterns if pattern in words_in_post)
        as_score = (matches / len(words_in_post)) * 100 if words_in_post else 0

        self.add_result(post_id, int(as_score))
        return f"Post as score is {as_score}%"




    def add_result(self, post_id, analysis_score):
        """ Add the analysis result to the results table """
        analysis_time = datetime.now()
        with self.conn.cursor() as cursor:
            insert_query = """
            INSERT INTO results (post_id, analysis_result, analysis_time) 
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (post_id, str(analysis_score), analysis_time))
            self.conn.commit()