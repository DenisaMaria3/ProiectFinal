import pandas
import mysql.connector

from password import parola

# Conectare la baza de date
my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database='adsgrupa2'
)
cursor = my_db.cursor()

#
# cursor.execute('DROP TABLE IF EXISTS reviews')
# cursor.execute('DROP TABLE IF EXISTS orders')
# cursor.execute('DROP TABLE IF EXISTS products')
# cursor.execute('DROP TABLE IF EXISTS customers')
# #
# #
# cursor.execute('''
#     CREATE TABLE customers (
#         customer_id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(100),
#         email VARCHAR(150),
#         country VARCHAR(100),
#         registration_date DATE
#     )
# ''')
# #
# #
# sql_customers = 'INSERT INTO customers (name, email, country, registration_date) VALUES (%s, %s, %s, %s)'
# val_customers = [
#     ('Alice Popescu', 'alice.popescu@example.com', 'Romania', '2022-01-15'),
#     ('Bogdan Ionescu', None, 'Romania', '2022-02-18'),
#     ('Carla Dinu', 'carla.dinu@example.com', 'Bulgaria', '2021-11-20'),
#     ('Daniel Raducanu', 'daniel.raducanu@example.com', 'Hungary', None),
#     ('Elena Marinescu', 'elena.marinescu@example.com', 'Germany', '2022-03-11'),
#     ('Fabian Moldovan', 'fabian.moldovan@example.com', None, '2022-04-10'),
#     ('Georgiana Nastase', 'georgiana.nastase@example.com', 'Romania', '2021-10-30'),
#     ('Horia Georgescu', None, 'France', '2021-09-12'),
#     ('Irina Constantin', 'irina.constantin@example.com', 'Spain', None),
#     ('Janos Horvath', 'janos.horvath@example.com', 'Hungary', '2022-03-02'),
#     ('Andrei Bucur', 'andrei.bucur@example.com', 'Italy', '2022-01-21'),
#     ('Bianca Oltean', 'bianca.oltean@example.com', 'Romania', '2022-02-17'),
#     ('Cristian Neagu', 'cristian.neagu@example.com', 'France', '2022-03-15'),
#     ('Diana Florescu', 'diana.florescu@example.com', 'Germany', '2022-01-29'),
#     ('Emilian Rusu', 'emilian.rusu@example.com', 'Hungary', '2022-02-03'),
#     ('Felicia Popa', 'felicia.popa@example.com', 'Romania', '2022-04-11'),
#     ('Gheorghe Stan', 'gheorghe.stan@example.com', None, '2022-03-10'),
#     ('Helena Moldoveanu', 'helena.moldoveanu@example.com', 'Spain', '2022-01-25'),
#     ('Ioan Serban', 'ioan.serban@example.com', 'France', '2021-12-18'),
#     ('Jocelyn Tudor', 'jocelyn.tudor@example.com', 'Romania', '2022-02-19'),
#     ('Kira Luca', 'kira.luca@example.com', 'Italy', '2022-04-04'),
#     ('Luca Crisan', 'luca.crisan@example.com', 'Bulgaria', '2022-02-22'),
#     ('Marius Pavel', None, 'Germany', '2021-11-19'),
#     ('Natalia Andreescu', 'natalia.andreescu@example.com', 'Hungary', '2021-12-24'),
#     ('Oana Dragomir', 'oana.dragomir@example.com', 'Romania', '2022-03-07'),
#     ('Paul Anton', 'paul.anton@example.com', 'France', '2022-02-08'),
#     ('Raluca Stoica', 'raluca.stoica@example.com', 'Poland', '2022-03-01'),
#     ('Sergiu Enache', 'sergiu.enache@example.com', 'Spain', '2021-10-28'),
#     ('Teodor Albu', 'teodor.albu@example.com', 'Romania', None),
#     ('Ursula Dumitrescu', 'ursula.dumitrescu@example.com', 'Germany', '2021-09-30'),
#     ('Valentin Dragoi', 'valentin.dragoi@example.com', 'Bulgaria', '2022-04-06'),
#     ('Xenia Preda', 'xenia.preda@example.com', 'Romania', '2022-01-11'),
#     ('Yvonne Craciun', 'yvonne.craciun@example.com', 'Italy', '2022-02-26'),
#     ('Zoltan Tarnavski', 'zoltan.tarnavski@example.com', 'Hungary', '2022-03-13'),
#     ('Adriana Radu', 'adriana.radu@example.com', 'Romania', '2022-04-07'),
#     ('Bogdan Iliescu', 'bogdan.iliescu@example.com', 'France', '2021-10-14'),
#     ('Carmina Filip', 'carmina.filip@example.com', 'Spain', None),
#     ('Dumitru Lungu', 'dumitru.lungu@example.com', 'Poland', '2022-03-18'),
#     ('Elvira Maxim', 'elvira.maxim@example.com', 'Italy', '2021-09-25'),
#     ('Florin Iacob', 'florin.iacob@example.com', 'Germany', '2022-01-14'),
#     ('Gabriela Rusu', 'gabriela.rusu@example.com', 'Romania', '2022-03-20'),
#     ('Horia Stanescu', None, 'France', '2021-11-03'),
#     ('Iulia Luca', 'iulia.luca@example.com', 'Hungary', '2022-04-01'),
#     ('Jana Andrei', 'jana.andrei@example.com', 'Romania', '2021-10-08'),
#     ('Katalin Toma', 'katalin.toma@example.com', 'Bulgaria', '2022-02-05'),
#     ('Liviu Mocanu', 'liviu.mocanu@example.com', 'Spain', '2022-03-22'),
#     ('Mircea Banciu', 'mircea.banciu@example.com', 'Romania', '2021-09-15'),
#     ('Nadia Balan', None, 'Italy', '2022-04-05'),
#     ('Octavian Toma', 'octavian.toma@example.com', 'Germany', '2021-11-27'),
#     ('Petre Damian', 'petre.damian@example.com', 'France', '2022-02-09')
# ]
# cursor.executemany(sql_customers, val_customers)
# my_db.commit()
#
#
# cursor.execute('''
#     CREATE TABLE products (
#         product_id INT AUTO_INCREMENT PRIMARY KEY,
#         product_name VARCHAR(100),
#         category VARCHAR(150),
#         stock INT
#     )
# ''')
#
#
# sql_products = 'INSERT INTO products (product_name, category, stock) VALUES (%s, %s, %s)'
# val_products = [
#     ('Laptop', 'Electronics', 50),
#     ('Smartphone', 'Electronics', 150),
#     ('Office Chair', 'Furniture', 30),
#     ('Desk Lamp', 'Furniture', 60),
#     ('Backpack', 'Accessories', 200),
#     ('Wireless Mouse', 'Electronics', 120),
#     ('Keyboard', 'Electronics', 100),
#     ('Monitor', 'Electronics', 80),
#     ('Coffee Table', 'Furniture', 40),
#     ('Desk Organizer', 'Accessories', 300),
#     ('Tablet', 'Electronics', 90),
#     ('Headphones', 'Electronics', 200),
#     ('Smartwatch', 'Electronics', 140),
#     ('Bluetooth Speaker', 'Electronics', 75),
#     ('Camera', 'Electronics', 60),
#     ('Gaming Chair', 'Furniture', 20),
#     ('Bookshelf', 'Furniture', 35),
#     ('Wardrobe', 'Furniture', 25),
#     ('Sofa', 'Furniture', 15),
#     ('Dining Table', 'Furniture', 18),
#     ('Sunglasses', 'Accessories', 250),
#     ('Wallet', 'Accessories', 300),
#     ('Scarf', 'Accessories', 400),
#     (None, 'Accessories', 0),
#     ('Suitcase', 'Accessories', 120),
#     ('Charger', 'Electronics', 180),
#     ('Power Bank', 'Electronics', 130),
#     ('USB Cable', 'Electronics', 400),
#     ('External Hard Drive', 'Electronics', 60),
#     ('Drone', 'Electronics', 25),
#     ('Filing Cabinet', 'Furniture', 28),
#     ('Nightstand', None, 42),
#     ('Bed Frame', 'Furniture', 12),
#     (None, 'Furniture', 0),
#     ('Electric Kettle', 'Appliances', 40),
#     ('Blender', 'Appliances', 35),
#     ('Mixer', 'Appliances', 20),
#     ('Refrigerator', 'Appliances', 10),
#     ('Washing Machine', 'Appliances', 15),
#     ('Air Conditioner', 'Appliances', 5),
#     ('Heater', 'Appliances', 8),
#     ('Toaster', 'Appliances', 20),
#     ('Food Processor', 'Appliances', None),
#     ('Microwave', 'Appliances', 7)
#  ]
# cursor.executemany(sql_products, val_products)
# my_db.commit()
#
#
# cursor.execute('''
#     CREATE TABLE orders (
#         order_id INT AUTO_INCREMENT PRIMARY KEY,
#         customer_id INT,
#         product_id INT,
#         order_date DATE,
#         quantity INT,
#         price DECIMAL(10, 2),
#         FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
#         FOREIGN KEY (product_id) REFERENCES products(product_id)
#     )
# ''')
#
#
# sql_orders = 'INSERT INTO orders (customer_id, product_id, order_date, quantity, price) VALUES (%s, %s, %s, %s, %s)'
# val_orders = [
#     (1, 1, '2022-02-01', 2, 100.00),
#     (2, 2, '2022-03-03', 1, 150.00),
#     (3, 3, None, 5, 200.00),
#     (4, 4, '2022-01-15', 1, 50.00),
#     (5, 5, '2022-02-18', 3, 75.00),
#     (6, 6, '2022-02-20', None, 90.00),
#     (7, 7, '2022-03-21', 4, 80.00),
#     (8, 8, None, 2, 60.00),
#     (9, 9, '2022-01-11', 1, 120.00),
#     (10, 10, '2022-02-22', 1, 110.00),
#     (11, 11, '2022-03-02', None, 140.00),
#     (12, 12, '2022-01-30', 2, 130.00),
#     (13, 13, '2022-04-04', 2, 90.00),
#     (14, 14, '2022-04-10', 5, 200.00),
#     (15, 15, '2022-04-11', 3, 150.00),
#     (16, 16, None, 2, 160.00),
#     (17, 17, '2022-02-15', 4, 170.00),
#     (18, 18, '2022-03-01', None, 80.00),
#     (19, 19, '2022-03-05', 1, 110.00),
#     (20, 20, '2022-04-20', 3, 120.00),
#     (21, 21, '2022-05-10', 2, 130.00),
#     (22, 22, '2022-06-15', 1, 140.00),
#     (23, 23, '2022-06-20', 2, 150.00),
#     (24, 24, '2022-07-01', None, 160.00),
#     (25, 25, '2022-08-10', 5, 170.00),
#     (26, 26, '2022-09-01', 4, 180.00),
#     (27, 27, '2022-09-15', 3, 190.00),
#     (28, 28, '2022-10-01', 2, 200.00),
#     (29, 29, None, 1, 210.00),
#     (30, 30, '2022-10-15', None, 220.00),
#     (31, 31, '2022-10-20', 3, 230.00),
#     (32, 32, '2022-10-25', 2, 240.00),
#     (33, 1, '2022-01-10', 1, 250.00),
#     (34, 2, '2022-01-20', 2, 260.00),
#     (35, 3, '2022-01-25', 3, 270.00),
#     (36, 4, None, 4, 280.00),
#     (37, 5, '2022-02-10', 1, 290.00),
#     (38, 6, '2022-02-11', 1, 300.00),
#     (39, 7, '2022-02-12', None, 310.00),
#     (40, 8, '2022-02-13', 3, 320.00),
#     (41, 9, '2022-02-14', 2, 330.00),
#     (42, 10, '2022-02-15', 5, 340.00),
#     (43, 11, None, 1, 350.00),
#     (44, 12, '2022-03-03', 2, 360.00),
#     (45, 13, '2022-03-04', None, 370.00),
#     (46, 14, '2022-03-05', 3, 380.00),
#     (47, 15, '2022-03-06', 4, 390.00),
#     (48, 16, '2022-03-07', 1, 400.00),
#     (49, 17, None, 2, 410.00),
#     (14, 3, '2022-01-25', 3, 270.00),
#     (7, 4, '2022-01-25', 4, 280.00),
#     (9, 5, '2022-02-10', 1, 290.00),
#     (9, 6, '2022-02-11', 1, 300.00),
#     (25, 7, '2022-02-12', 4, 310.00),
#     (40, 8, '2022-02-13', 3, 320.00),
#     (40, 9, '2022-02-14', 2, 330.00),
#     (12, 10, '2022-02-15', 5, 340.00),
#     (15, 11, '2022-02-15', 1, 350.00),
#     (14, 12, '2022-03-03', 2, 360.00),
#     (15, 13, '2022-03-04', 3, 370.00),
#     (6, 14, '2022-03-05', 3, 380.00),
#     (7, 15, '2022-03-06', 4, 390.00),
#     (15, 16, '2022-03-07', 1, 400.00),
#     (10, 17, '2022-03-07', 2, 410.00)
# ]
#
#
# cursor.executemany(sql_orders, val_orders)
# my_db.commit()
# #
#
# cursor.execute('''
#     CREATE TABLE reviews (
#         review_id INT AUTO_INCREMENT PRIMARY KEY,
#         customer_id INT,
#         product_id INT,
#         rating INT,
#         review_date DATE,
#         FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
#         FOREIGN KEY (product_id) REFERENCES products(product_id)
#     )
# ''')
#
#
# sql_reviews = 'INSERT INTO reviews (customer_id, product_id, rating, review_date) VALUES (%s, %s, %s, %s)'
# val_reviews = [
#     (1, 3, 5, '2022-01-21'),
#     (2, 2, 4, '2022-02-16'),
#     (4, 15, 3, '2021-12-23'),
#     (7, 12, 5, '2022-04-06'),
#     (9, 5, 4, '2021-10-11'),
#     (10, 6, 3, '2021-11-19'),
#     (3, 10, 4, '2022-03-23'),
#     (6, 18, 2, '2022-03-04'),
#     (8, 9, 3, '2022-04-15'),
#     (11, 4, 4, '2022-02-26'),
#     (13, 21, 3, '2021-11-12'),
#     (15, 13, 2, '2021-12-09'),
#     (17, 7, 3, '2022-01-28'),
#     (19, 10, 4, '2022-04-20'),
#     (21, 19, 5, '2022-02-15'),
#     (22, 16, 3, '2021-10-06'),
#     (24, 2, 5, '2021-09-28'),
#     (26, 11, 4, '2022-03-07'),
#     (28, 22, 5, '2022-01-30'),
#     (32, 23, 5, '2021-10-19'),
#     (34, 24, 3, '2022-04-24'),
#     (36, 25, 4, '2022-03-19'),
#     (38, 26, 3, '2022-02-02'),
#     (40, 17, 5, '2022-04-21'),
#     (42, 27, 4, '2022-01-20'),
#     (44, 15, 5, '2021-12-28'),
#     (46, 29, 2, '2021-11-23'),
#     (48, 30, 5, '2022-02-11'),
#     (50, 31, 4, '2022-01-16'),
#     (12, 32, 3, '2022-03-30'),
#     (14, 30, 4, '2021-10-10'),
#     (16, 25, 5, '2021-11-04'),
#     (18, 20, 4, '2022-01-24'),
#     (20, 24, 3, '2021-12-06'),
#     (23, 16, 5, '2022-04-09'),
#     (25, 15, 4, '2022-03-01'),
#     (27, 20, 2, '2021-09-16'),
#     (29, 26, 5, '2022-04-10'),
#     (31, 14, 3, '2022-03-13'),
#     (33, 15, 4, '2022-01-06'),
#     (35, 23, 5, '2021-12-26'),
#     (37, 20, 6, '2021-10-31'),
#     (39, 19, 3, '2022-02-24'),
#     (41, 21, 5, '2022-03-26'),
#     (43, 23, 4, '2022-01-08'),
#     (45, 25, 3, '2021-11-27'),
#     (47, 26, 5, '2022-04-04'),
#     (49, 23, 2, '2021-09-15')
# ]
# cursor.executemany(sql_reviews, val_reviews)
# my_db.commit()
#


query = (
    "SELECT o.order_id, o.customer_id, o.product_id, o.order_date, o.quantity, o.price, "
    "c.name, c.email, c.country, c.registration_date, "
    "p.product_name, p.category, p.stock, "
    "r2.rating AS rating, r2.review_date AS review_date, r2.review_id AS review_id "
    "FROM orders o "
    "JOIN products p ON o.product_id = p.product_id "
    "JOIN customers c ON o.customer_id = c.customer_id "
    "LEFT JOIN reviews r1 ON o.product_id = r1.product_id AND o.customer_id = r1.customer_id "
    "LEFT JOIN reviews r2 ON o.customer_id = r2.customer_id"
)

df_cu_valori_sterse = pandas.read_sql(query, my_db)
df_cu_valori_sterse = df_cu_valori_sterse.dropna().reset_index(drop=True)

# sa inceapa indexul de la 1
df_cu_valori_sterse.index = range(1, len(df_cu_valori_sterse) + 1)

df_cu_valori_sterse.to_csv("QUERY.csv", index=True)
print("1. CSV - corectat")
print(df_cu_valori_sterse)

#ex 2

#a venituri toale lunare
print("")
print("2a. Venituri toale lunare : ")

# convertim data
df_cu_valori_sterse['order_date'] = pandas.to_datetime(df_cu_valori_sterse['order_date'])

df_cu_valori_sterse['an_luna'] = df_cu_valori_sterse['order_date'].dt.to_period('M')

df_cu_valori_sterse['venit_total'] = df_cu_valori_sterse['price'] * df_cu_valori_sterse['quantity']
grupari_venituri_pe_luna = df_cu_valori_sterse.groupby("an_luna")['venit_total'].sum()

# veniturile totale/luna
for luna, venit_total in grupari_venituri_pe_luna.items():
    print(f"\nVeniturile totale pentru luna {luna}: {venit_total}")

print("")

#b cele mai bine vandute prod din fiecare categorie
print("")
print("2b. Cele mai bine vandute produse din fiecare categorie: ")
print("")
# grupare_categorie = df_cu_valori_sterse.groupby("category")
# for nume_categorie, grup_categorie in grupare_categorie:
#     print(f"\n Grupare pe categorie: {nume_categorie}")
#     print(grup_categorie)

grup_produs_pe_categorie = df_cu_valori_sterse.groupby(['category', 'product_name'])['quantity'].sum().reset_index()
print(grup_produs_pe_categorie) #returneaza categorie-produs-cantitate(suma)
print("")
# top produs/categorie : extragem randurile corespunzatoare din gruparea (loc), din indexul randului unde cantitatea e max pt fiecare categorie
top_produse = grup_produs_pe_categorie.loc[grup_produs_pe_categorie.groupby('category')['quantity'].idxmax()]
print(top_produse)
top_produse.to_csv("2b-Analiza produse populare.csv", index=True)

#c suma totala a comenzilor fiecarui client.
print("")
print("2c. Suma totala a comenzilor fiecarui client :")
print("")
df_cu_valori_sterse['valoare_comanda'] = df_cu_valori_sterse['quantity'] * df_cu_valori_sterse['price']

rezultat = df_cu_valori_sterse.groupby(['customer_id', 'name']).agg({
    'valoare_comanda': 'sum'}).reset_index()

print(rezultat[['name', 'valoare_comanda']])
(rezultat[['name', 'valoare_comanda']]).to_csv("2c-Valoarea totala a clientilor.csv", index=True)

#d
print("")
print("2d. Media ratingului/produs :")
print("")
df_medie_rating = df_cu_valori_sterse[["rating","product_name"]]
medii_rating = df_medie_rating.groupby('product_name')['rating'].mean().reset_index()
print(medii_rating)
medii_rating.to_csv("2d-Recenzii si satisfactia clientilot.csv", index=True)
#e
print("")
print("2e. Clientii cu cele mai multe comenzi plasate")
print("")

#creare coloana orders_count care contine nr de comenzi/cliet
top_clienti = df_cu_valori_sterse.groupby(['customer_id', 'name']).size().reset_index(name='orders_count')

# sort descrescator
top_5_clients = top_clienti.sort_values(by='orders_count', ascending=False).head(5)

print(top_5_clients)
top_5_clients.to_csv("2e-Top 5 clienti fideli.csv", index=True)

#ex4
#a
print("")
print("4a. Top 10 clienti dupa numarul de comenzi")
print("")
#top_clienti declarat in 2e
top_10_clients = top_clienti.sort_values(by='orders_count', ascending=False).head(10)
print(top_10_clients)
top_10_clients.to_csv("4a-Top 10 clienti dupa nr de comenzi.csv", index=True)

#b
print("")
print("4b. Produsele cu cele mai multe recenzii")
print("")

#produse_count care contine nr de rating/produs
top_produse_recenzii = df_cu_valori_sterse.groupby(['rating', 'product_name']).size().reset_index(name='produse_count')

# sort descrescator
top_3_produse = top_produse_recenzii.sort_values(by='produse_count', ascending=False).head(3)

print(top_3_produse)
top_3_produse.to_csv("4b-Produsele cu cele mai multe recenzii.csv", index=True)

