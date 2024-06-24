SELECT u.id, u.name, o.orderAt, s.name, i.name
FROM users u 
JOIN orders o ON u.id = o.userid
JOIN stores s ON o.storeid = s.id
JOIN orderitems oi ON o.id = oi.orderid
JOIN items I ON oi.itemid = i.id
WHERE u.id = "임의의 uuid"