import pyscopg2


def create_table():
    connection = sqlite3.connect('lite.db')
    cur= connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect('lite.db')
    cur= connection.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect('lite.db')
    cur= connection.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = sqlite3.connect('lite.db')
    cur= connection.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    connection.commit()
    connection.close()    

def update(item, quantity, price):
    connection = sqlite3.connect('lite.db')
    cur= connection.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    connection.commit()
    connection.close()    


print(view())
insert("Lukes party",18,23.3)
insert("Petkas party",10,22.3)
print(view())
update("Petkas partyd", 30, 10.2)
print(view())

