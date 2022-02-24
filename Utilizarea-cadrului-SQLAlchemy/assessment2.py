from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# import sqlite3

# conn = sqlite3.connect('books.db')

engine = create_engine('sqlite:///books.db', echo=True)
meta = MetaData()

books = Table(
    'books', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('year', Integer),
)

meta.create_all(engine)

engine.execute(books.insert(), [
   {'title':'Atomic Habits', 'year' : 2018},
   {'title':'Deep work', 'year' : 2016},
   {'title':'The Power of Habit', 'year' : 2012},
   {'title':'Cracking the code interview', 'year' : 2008},
])

query = books.select()
conn = engine.connect()
result = conn.execute(query)

for row in result:
    print(row)