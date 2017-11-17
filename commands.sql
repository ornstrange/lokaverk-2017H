create database 1910952789_fatasida;
use 1910952789_fatasida;

CREATE TABLE items (
    iid INT PRIMARY KEY NOT NULL,
    iname VARCHAR(32) NOT NULL,
    kind VARCHAR(32),
    color VARCHAR(16),
    amount INT,
    size FLOAT,
    price INT,
    arrivalDate DATE,
    img VARCHAR(100)
);

CREATE TABLE users (
    uid INT PRIMARY KEY NOT NULL,
    username VARCHAR(32) NOT NULL,
    passwd VARCHAR(32) NOT NULL,
    email VARCHAR(64) NOT NULL,
    isAdmin BOOLEAN,
    fname VARCHAR(32),
    lname VARCHAR(32)
);

CREATE TABLE stock (
    totalPrice INT,
    amtOfItems INT
);

CREATE TABLE cart (
    iid INT NOT NULL,
    uid INT NOT NULL,
    FOREIGN KEY (iid) REFERENCES items(iid),
    FOREIGN KEY (uid) REFERENCES users(uid)
);