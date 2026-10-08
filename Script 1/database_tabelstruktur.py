#Script #1
#Et script til at definere databasens tabelstruktur –
# hvis I har f.eks. to tabeller så også med en
#fremmednøgle. I skal bruge CREATE TABLE-kommandoen

import sqlite3
conn = sqlite3.connect('webshop.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    stock INTEGER,
    category_id INTEGER, foreign key(category_id) REFERENCES categories(id)
)
""")
cursor.execute("""
create table categories
(
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

conn.commit()
conn.close()

print("Tabellerne er oprettet!")