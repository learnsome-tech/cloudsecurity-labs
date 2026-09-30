import psycopg

def find_user(cur, user_id):
    cur.execute("SELECT name FROM users WHERE id = %s" % user_id)
    return cur.fetchone()

def find_by_email(cur, email):
    cur.execute("SELECT id FROM users WHERE email = %s", (email,))
    return cur.fetchone()

def search(cur, term):
    query = "SELECT id FROM users WHERE name = '%s'" % term
    cur.execute(query)
    return cur.fetchall()

def row_count(cur, table):
    # was: cur.execute("SELECT count(*) FROM %s" % table)
    cur.execute(f"SELECT count(*) FROM {table}")
    return cur.fetchone()
