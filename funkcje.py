import sqlite3

def save(author, title, descr, format):
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("INSERT INTO lista(author, title, descr, format) VALUES (?, ?, ?, ?)", (author, title, descr, format))
    conn.commit()
    c.close()
    
def read():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM lista")
    rows = c.fetchall()
    conn.commit()
    c.close()
    return rows

def remove(aut, tit):
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("DELETE FROM lista WHERE author = ? AND title = ?", (aut, tit))
    conn.commit()
    c.close()
    return

def find_ids():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM lista")
    rows = c.fetchall()
    conn.commit()
    c.close()
    id_list = []
    for i in rows:
        id_list.append(i['id'])
    return id_list

def get_book(id):
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM lista WHERE id = ?", (id,))
    book = c.fetchall()
    conn.commit()
    c.close()
    return book[0]

def update(id, author, title, format, descr):
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE lista SET author = ? , title = ? , format = ? , descr = ? WHERE id = ?", (author, title, format, descr, id,))
    conn.commit()
    c.close()
    return

