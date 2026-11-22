-- CREATE DATABASE Employees;

-- USE Employees;
-- CREATE TABLE users
-- (id INT PRIMARY KEY,
-- name VARCHAR(50),
-- email VARCHAR(100));

-- INSERT INTO users(id, name, email)
-- VALUES
-- (1,"Shivam","shivam@test.com"),
-- (2,"Shalini", "shalini@test.com" ),
-- (3, "Shashi", "shashi@test.com");

-- USE Employees;
-- SELECT * FROM users
-- WHERE id = 3;

-- CREATE TABLE products
-- (product_id INT PRIMARY KEY,
-- product_name VARCHAR(50),
-- price INT);

-- CREATE TABLE orders
-- (order_id INT PRIMARY KEY,
-- user_id INT,
-- product_id INT);

-- INSERT INTO products(product_id, product_name, price)
-- VALUES 
-- (101, 'Laptop', 50000),
-- (102, 'Mouse', 1000),
-- (103, 'Keyboard', 2000);

-- INSERT INTO orders(order_id, user_id, product_id)
-- VALUES
-- (1001,1,101),
-- (1002,2,102),
-- (1003,3,103);

-- SELECT*FROM orders;
-- SELECT*FROM products;

-- INSERT INTO users(id, name, email)
-- VALUES
-- (4, 'Shivansh', 'shivansh@test.com');

-- SELECT * FROM users
-- WHERE id=4;

-- UPDATE users
-- SET email = 'shivansh_new@test.com'
-- WHERE id=4;

-- SELECT * FROM users
-- WHERE id =4;

-- SELECT id, email FROM users
-- WHERE id = 4 and email = 'shivansh_new@test.com'

-- INSERT INTO users(id, name, email)
-- VALUES
-- (5, 'Shivam2', 'shivam2@test.com');

-- SELECT * FROM users
-- WHERE id =5 and name = 'Shivam2' and email = 'shivam2@test.com';

-- SELECT* FROM orders
-- WHERE order_id=1002 and user_id=2 and product_id = 102;
-- ALTER TABLE orders
-- ADD status VARCHAR(20);

-- SELECT*FROM orders;

-- UPDATE orders
-- SET status = 'Shipped'
-- WHERE order_id=1002;

-- SELECT*FROM orders
-- WHERE status='Shipped'

SELECT*FROM users;
SELECT*FROM orders;
SELECT*FROM products;

-- SELECT users.name, orders.order_id FROM users
-- INNER JOIN orders
-- ON users.id = orders.user_id






-- SELECT users.name, orders.product_id FROM users
-- INNER JOIN orders
-- ON users.id = orders.user_id;
-- SELECT users.name, orders.order_id FROM users
-- LEFT JOIN orders
-- ON users.id = orders.user_id;

-- SELECT users.name, orders.order_id FROM users
-- RIGHT JOIN orders
-- ON users.id = orders.user_id;

-- SELECT user_id, COUNT(*) AS Number_of_orders_placed FROM orders
-- GROUP BY user_id;

-- INSERT INTO orders(order_id,user_id,product_id,status)
-- VALUES
-- (1004, 1, 104, 'Shipped'),
-- (1005, 1, 105, 'Shipped'),
-- (1006, 2, 106, 'Shipped');

-- SELECT*FROM orders;

-- SELECT user_id, COUNT(*) AS Numbers_of_order_placed FROM orders
-- GROUP BY user_id
-- HAVING COUNT(*)>=2

-- SELECT user_id, COUNT(*) AS Number_of_order_placed FROM orders
-- GROUP BY user_id;
-- WHERE id IN (SELECT user_id FROM orders
-- WHERE product_id>=104);

-- SELECT name FROM users
-- WHERE id IN (
-- SELECT user_id FROM orders)

-- SELECT name FROM users
-- WHERE id IN 
-- (SELECT user_id FROM orders WHERE product_id >=104);

-- SELECT name FROM users
-- WHERE id in (SELECT user_id FROM orders
-- GROUP BY user_id
-- Having COUNT(*)>1 );
-- SELECT name from users WHERE id in 
-- (SELECT user_id from orders
-- WHERE status = 'Shipped'
-- group by user_id
-- );

SELECT USER();


























