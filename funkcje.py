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