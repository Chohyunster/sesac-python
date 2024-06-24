CREATE TABLE if not exists 'users' (
    'id' text primary key,
    'name' text NOT NULL,
    'gender' text,
    'age' INTEGER,
    'birthdate' DATE,
    'address' text
    );

CREATE TABLE if not exists 'stores' (
    'id' text primary key,
    'name' text NOT NULL,
    'type' text,
    'address' text
    );

CREATE TABLE if not exists 'orders' (
    'id' text primary key,
    'orderat' DATETIME NOT NULL,
    'storeid' text NOT NULL,
    'userid' text,
    FOREIGN KEY ('storeid') REFERENCES 'stores'('id'),
    FOREIGN KEY ('userid') REFERENCES 'users'('id')
    );

CREATE TABLE if not exists 'items' (
    "id" text primary key,
    "name" text NOT NULL,
    "type" text,
    "unitprice" INTEGER
    ); 

CREATE TABLE if not exists 'orderitems' (
    "id" text primary key,
    "orderid" text NOT NULL,
    "itemid" text,
    FOREIGN KEY ('orderid') REFERENCES 'orders'('id'),
    FOREIGN KEY ('itemid') REFERENCES 'items'('id')
    );  

