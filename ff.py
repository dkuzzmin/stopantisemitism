
import psycopg2

conn = psycopg2.connect(
    dbname = 'qmcjdcgq',
    user = 'qmcjdcgq',
    password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
    host = 'flora.db.elephantsql.com',
    port = '5432' 
)

cur = conn.cursor()


# insert_query = 'INSERT INTO products (name, price) VALUES (%s,%s)'
# data_to_insert = ('iKey', 100)
# cur.execute(insert_query, data_to_insert)

# insert_query = 'INSERT INTO products (name, price) VALUES (%s,%s)'
# data_to_insert = ('iKey', 100)
# cur.execute(insert_query, data_to_insert)

# insert_query = 'INSERT INTO products (name, price) VALUES (%s,%s)'
# data_to_insert = ('iKey', 100)

# cur.execute(insert_query, data_to_insert)
# conn.commit()


cur.execute('SELECT * FROM posts_db')
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close