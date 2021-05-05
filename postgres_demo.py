import psycopg2 

def create_table():
    # Connect to a database
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432' ")

    # Create a cursor object
    cur = conn.cursor()

    # Write SQL query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#insert("Orange", 10, 15)
#delete("Orange")
update(20, 9, "Apple")
print(view())