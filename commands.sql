create database 1910952789_fatasida;
use 1910952789_fatasida;

CREATE TABLE items (
    iid INT PRIMARY KEY NOT NULL,
    iname VARCHAR(100) NOT NULL,
    kind VARCHAR(32),
    color VARCHAR(16),
    amount INT,
    price INT,
    new BOOLEAN,
    img VARCHAR(200)
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

delimiter //
CREATE PROCEDURE total (OUT tot INT)
    BEGIN
    SELECT sum(price) INTO tot FROM items;
    END//
delimiter ;

delimiter //
CREATE PROCEDURE totalItems (OUT toti INT)
    BEGIN
    SELECT sum(amount) INTO toti FROM items;
    END//
delimiter ;

delimiter //
CREATE TRIGGER updateStock
BEFORE UPDATE ON items
FOR EACH ROW 
	
END IF;//
delimiter ;

