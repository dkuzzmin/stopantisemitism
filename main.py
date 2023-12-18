import psycopg2


# Function to connect to database
def connect_to_db():
    conn = psycopg2.connect(
    dbname = 'qmcjdcgq',
    user = 'qmcjdcgq',
    password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
    host = 'flora.db.elephantsql.com',
    port = '5432' 
    )  
    return conn

def view_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM patterns")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()



from textblob import TextBlob
import psycopg2

def get_patterns():
    conn = connect_to_db()

    pass

def analyze_post(post_text):
    patterns = get_patterns()
    blob = TextBlob(post_text.lower())
    words_in_post = blob.words

    matches = 0
    for pattern in patterns:
        if pattern in words_in_post:
            matches += 1

    antisemitism_score = (matches / len(words_in_post)) * 100
    return antisemitism_score



conn = connect_to_db()

view_all(conn)

# class patternword (word, anitisem)
#     word = ''
#     antisem = True
#     posts_base


# def  analyze text




# sql online database

# set databases:
# - antisem sequnces
# - pro sequunses
# - main input base of publications (posts)
# - univers in watch list
# ?table of json’s files

# !find main metodology (finding hate speech)

# py-file:
# - connection to db
# - db link one-one
# - functions(features) in exter file (internal modul)
# - sql extract
# - using some external api
# - stat modul python
# - word analisys modul
# - visual module
# - ? class ??? how to use?
# - ? user manager??


# output:
# - dashboard (imafe file?)
# - html file on some server online
# - like telegram channel everyday stats






