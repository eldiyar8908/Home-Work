import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


data_base = 'hw.db'
connect = create_connection(data_base)


sql_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity DOUBLE(5) NOT NULL DEFAULT 0,
)
'''


def insert_15_products(conn, product_list):
    if len(product_list) > 15 or len(product_list) < 15:
        print('Кол-во должно быть ровно 15!')
    else:
        try:
            for i in product_list:
                sql = '''INSERT INTO products(product_title, price, quantity)
                VALUES (?,?,?)'''
                cursor = conn.cursor()
                cursor.execute(sql, i)
                conn.commit()
        except sqlite3.Error as a:
            print(a)


def update_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as a:
        print(a)


def update_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as a:
        print(a)


def delete_product(conn, product):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (product,))
        conn.commit()
    except sqlite3.Error as a:
        print(a)


def select_all_products(conn):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as a:
        print(a)


def select_products_by_price_limit_100(conn):
    try:
        sql = '''SELECT * FROM products WHERE price <= 100 AND quantity >= 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as a:
        print(a)


def search_by_word(conn, word):
    try:
        sql = """SELECT * FROM products WHERE product_title REGEXP '%?%'"""
        cursor = conn.cursor()
        cursor.execute(sql, (word,))
        rows = cursor.fetchall
        for row in rows:
            print(row)
    except sqlite3.Error as a:
        print(a)
