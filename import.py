import psycopg2

conn = psycopg2.connect(database="products",
						user='postgres', password='hemid8th',
						host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


# sql = '''CREATE TABLE DETAILS(name text NOT NULL,\
# sku text,\
# price int, category text);'''


# cursor.execute(sql)

sql2 = '''COPY products(name,sku,\
price,category)
FROM 'C:/Users/HP/Documents/Development/fast_api/sample-products.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql2)

sql3 = '''select * from products;'''
cursor.execute(sql3)
for i in cursor.fetchall():
	print(i)

# sql4 = '''ALTER TABLE details
# ADD COLUMN discount INT DEFAULT 0;'''
# cursor.execute(sql4)

# sql5 = '''ALTER TABLE details
# ALTER discount SET DEFAULT 0;'''
# cursor.execute(sql5)

conn.commit()
conn.close()
