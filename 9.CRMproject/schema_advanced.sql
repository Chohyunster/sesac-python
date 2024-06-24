CREATE TABLE if not exists 'users' (
    'id' text primary key,
    'name' text NOT NULL,
    'gender' text,
    'age' INTEGER,
    'birthdate' DATE,
    'address' text);
    --UNIQUE('name', 'address') 넣어준다.(constraint를 설정하는 과정: 

CREATE TABLE if not exists 'stores' (
    'id' text primary key,
    'name' text NOT NULL,
    'type' text,
    'address' text);

CREATE TABLE if not exists 'orders' (
    'id' text primary key,
    'orderat' DATETIME NOT NULL CHECK (orderat <= CURRENT_TIMESTAMP),
    'storeid' text NOT NULL,
    'userid' text,
    FOREIGN KEY ('storeid') REFERENCES 'stores'('id'), -- 'stores('id')를 "stores.id"라고 쓸 수 있음.
    FOREIGN KEY ('userid') REFERENCES 'users'('id'); --users.id
);

CREATE TABLE if not exists 'items' (
    "id" text primary key,
    "name" text NOT NULL,
    "type" text,
    "unitprice" INTEGER CHECK (unitprice > 0)); --미국달라면 REAL을 통한 소수점 지원

CREATE TABLE if not exists 'orderitems' (
    "id" text primary key,
    "orderid" text NOT NULL,
    "itemid" text
    FOREIGN KEY ('orderid') REFERENCES 'orders'('id'), --orders.id
    FOREIGN KEY ('itemid') REFERENCES 'items'('id'));  --items.id


    --외래키: 주문내역을 삭제했을 때 다른 테이블에서 관련 내용이 자동으로 삭제되도록 해줌. 
    --외래키를 안 쓴다면,,, 
    -- DELETE FROM orders WHERE id = '1234';
    -- DELETE FROM orderitems WHERE orderid = '1234';


