CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,             -- Identifier User
    login VARCHAR(50) NOT NULL UNIQUE,                      -- Options types (cpf, phone, email ou user)
    passwd VARCHAR(100) NOT NULL,                           -- This is password access account user in base64
    access VARCHAR(10) NOT NULL DEFAULT "standard",         -- This is type access in application   
    INDEX (login)      
)


CREATE TABLE if NOT EXISTS products(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,             -- Identifier Id product unique key for product
    name VARCHAR(30) NOT NULL UNIQUE,                       -- Product's name
    amount INT NOT NULL DEFAULT 0,                          -- Amount products in stock
    price FLOAT NOT NULL DEFAULT 15.0,                      -- Value for unit product
    INDEX (name)
)