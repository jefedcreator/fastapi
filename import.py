import psycopg2

conn = psycopg2.connect(database="products",
						user='postgres', password='hemid8th',
						host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


sql = '''CREATE TABLE DETAILS(name text NOT NULL,\
sku text,\
price int, category text);'''


cursor.execute(sql)

sql2 = '''COPY details(name,sku,\
price,category)
FROM 'C:/Users/HP/Documents/Development/fast_api/sample-products.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql2)

sql3 = '''select * from details;'''
cursor.execute(sql3)
for i in cursor.fetchall():
	print(i)

conn.commit()
conn.close()
