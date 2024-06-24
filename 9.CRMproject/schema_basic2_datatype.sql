CREATE TABLE if not exists items (
    "id" text,
    "name" text,
    "type" text,
    "unitprice" INTEGER);

CREATE TABLE if not exists orderitems (
    "id" text,
    "orderid" text,
    "itemid" text);

CREATE TABLE if not exists orders (
    'id' text,
    'orderat' DATETIME,
    'storeid' text,
    'userid' text);

CREATE TABLE if not exists stores (
    'id' text,
    'name' text,
    'type' text,
    'address' text);

CREATE TABLE if not exists users (
    'id' text,
    'name' text,
    'gender' text,
    'age' INTEGER,
    'birthdate' DATE,
    'address' text);