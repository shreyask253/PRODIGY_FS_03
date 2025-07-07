import sqlite3
import os

# Make sure the 'data' folder exists
os.makedirs('data', exist_ok=True)

conn = sqlite3.connect('data/store.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL,
    image TEXT
)
''')

products = [
    ('T-Shirt', '100% cotton t-shirt', 499.00, 'tshirt.jpg'),
    ('Jeans', 'Comfort fit blue jeans', 899.00, 'jeans.jpg'),
    ('Sneakers', 'Stylish sneakers', 1299.00, 'sneakers.jpg')
]

cursor.executemany('''
INSERT INTO products (name, description, price, image)
VALUES (?, ?, ?, ?)
''', products)

conn.commit()
conn.close()

print("Database created and populated successfully ✅")
