from classes import AntisemitismAnalyzer 

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




def view_all_patterns(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM patterns")
        rows = cur.fetchall()
        for row in rows:
            print(row)

def insert_post(conn):
    post_text = input("Enter text post: ")
    post_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    platform_id = input("Enter platform ID: ")
    author = input("Enter author of post: ")
    meta_info = ""

    with conn.cursor() as cursor:
        insert_query = """
        INSERT INTO posts (post_text, post_time, platform_id, author) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (post_text, post_time, platform_id, author))
        conn.commit()
    print("Post added")

def delete_post(conn):
    post_id = input("Enter the post ID to delete: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM posts WHERE post_id = %s", (post_id,))
        conn.commit()
        print(f"Post with ID {post_id} deleted")

def insert_platform(conn):


    name = input("Enter platform name: ")
    url = input("Enter platform URL: ")
    country = input("Enter platform country: ")

    with conn.cursor() as cursor:
        insert_query = """
        INSERT INTO platforms (name, url, country) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (name, url, country))
        conn.commit()
    print("Platform added")

def show_analysis_summary_for_platform(conn, platform_id):
    with conn.cursor() as cursor:
        query = """
        SELECT p.name, count(r.post_id) as total_posts, avg(r.analysis_result) as avg_score
        FROM platforms p
        JOIN posts po ON p.platform_id = po.platform_id
        JOIN results r ON po.post_id = r.post_id
        WHERE p.platform_id = %s
        GROUP BY p.name
        """
        
        platform_id_int = int(platform_id)
        cursor.execute(query, (platform_id_int,))
        result = cursor.fetchone()
        if result:
            print(f"Platform: {result[0]}, Total Posts Analyzed: {result[1]}, Average Analysis Score: {result[2]}")
        else:
            print(f"No analysis data found for platform ID: {platform_id}")
        

def insert_pattern(conn):
    pattern_text = input("Enter pattern text: ")
    
    severity_level = input("Enter severity level (1-5): ")
 

    with conn.cursor() as cursor:
        insert_query = """
        INSERT INTO patterns (pattern_text, severity_level) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (pattern_text, severity_level))
        conn.commit()

    print("Pattern added")

def delete_pattern(conn):
    pattern_id = input("Enter the pattern ID to delete: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM patterns WHERE pattern_id = %s", (pattern_id,))
        conn.commit()
        print(f"Pattern with ID {pattern_id} deleted")

def main_menu():
    conn = connect_to_db()
    analyzer = AntisemitismAnalyzer(conn)

    while True:
        print()
        print("""Post Analysis Menu
        1: Add New Post
        2: Delete Post
        3: Analyze Post
        4: Show Platform Statistics
        5: Add New Platform
        6: Show All Patterns
        7: Add New Pattern
        8: Delete Pattern
        9: Exit""")


        choice = input("Enter menu number: ")

        if choice == '1':
            insert_post(conn)
        elif choice == '2':
            delete_post(conn)
        elif choice == '3':
            post_id = input("Enter post id to analyze: ")
            print(analyzer.analyze_post(post_id))
        elif choice == '4':
            platform_id = int(input("Enter platform id: "))
            show_analysis_summary_for_platform(conn, platform_id)
        elif choice == '5':
            insert_platform(conn)
        elif choice == '6':
            view_all_patterns(conn)
        elif choice == '7':
            insert_pattern(conn)
        elif choice == '8':
            delete_pattern(conn)
        elif choice == '9':
            print()
            break
        
        else:
            print("Try again")




    conn.close()


if __name__ == "__main__":
    main_menu()