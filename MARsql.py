import sqlite3

##create table
def create_table():
    conn=sqlite3.connect("SHNCMAR.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (first_name TEXT,last_name TEXT, month TEXT,year TEXT,md_name TEXT,med TEXT)")
#,order_date TEXT,dose TEXT,freq TEXT, route TEXT, time_admin TEXT
    conn.commit()
    conn.close()
#insert row to table
def insert(first_name,last_name,month,year,md_name,med):
    #,order_date,dose,freq,route,time_admin
    conn=sqlite3.connect("SHNCMAR.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?,?,?,?)",(first_name,last_name,month,year,md_name,med))
    conn.commit()
    conn.close()

def viewTable():
    conn=sqlite3.connect("SHNCMAR.db")
    cur = conn.cursor()
    cur.execute("SELECT * from store")
    data = cur.fetchall()
    conn.close()
    return data

#retrieve data
def retrieve(first_name):
    conn=sqlite3.connect("SHNCMAR.db")
    cur = conn.cursor()
    cur.execute("SELECT * from store WHERE first_name=?", (first_name,))
    data = cur.fetchall()
    conn.close()
    return data
