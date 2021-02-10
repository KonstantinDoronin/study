/* Create table */
CREATE TABLE book,
    book id  INT PRIMARY KEY AUTO_INCREMENT,
    title    VARCHAR(50),
    author   VARCHAR(30),
    price    DECIMAL(30),
    amount   INT(10)
);




/* Insert into table */
INSERT INTO book(title, author, price, amount)
VALUES ("Мастер и Маргарита", "Булгаков М.А.", 670.99, 3),
       ("Белая гвардия", "Булгаков М.А.", 540.50,5),
       ("Идиот", "Достоевский Ф.М.", 460.00, 10),
       ("Братья Карамазовы", "Достоевский Ф.М.", 799.01,2);



/* Select basic */
SELECT * FROM book;

SELECT author, title, price
  FROM book;

SELECT title AS Название, author AS Автор
  FROM book;

SELECT title, amount,
       amount * 1.65 AS pack
  FROM book;

/* Math functions */
CEILING(x) - min possible value of x
ROUND(x,k) - round number by k value after point
FLOOR(x) - max possible value of x
POWER(x, y) - involution x in y
SQRT(x) - square root
DEGREES(x) - converts x-value from radians to degrees
RADIANS(x) - converts from degrees to radians
ABS(X) - absolut value of number
PI(x) - welcome pi


SELECT title, author, amount,
       ROUND((price *0.7,2) AS new_price
  FROM book;

SELECT author, title,
       ROUND(IF(author = "Булгаков М.А.", price *1.10, IF(author = "Есенин С.А.", price*1.05, price)), 2) AS new_price
  FROM book;

/* Request conditions */
! cant use column named by AS in WHERE
SELECT author, title, price
  FROM book
 WHERE amount <10;

SELECT title, author, price, amount
  FROM book
 WHERE (500 < price < 600 AND (amount * price > 5000));

SELECT title, author
  FROM book
 WHERE price BETWEEN 540.5 and 800 AND amount IN (2, 3, 5, 7);

SELECT title, author
  FROM book
 WHERE author LIKE "% С.%"
   AND title LIKE "%_%_";

/* Sorting */
FROM -> WHERE -> SELECT -> ORDER BY
ASC - ascending sort
DESC - descenting sort

SELECT    author, title
  FROM    book
 WHERE    amount BETWEEN 2 and 14
 ORDER BY author DESC, title ASC;

SELECT "Донцова Дарья" AS author,
  CONCAT ("Евлампия Романова и ", title) as title,
  price*1.42 as price
    FROM book
ORDER BY price DESC, title DESC;

/* Aggregation functions */
   SELECT amount
     FROM book
 GROUP BY amount;

   SELECT author as Автор,
          COUNT(DISTINCT title) as "Различных книг",
          SUM(amount) as Количество_экземпляров
     FROM book
 GROUP BY author;

   SELECT author,
          MIN(price) as Минимальная_цена,
          MAX(price) as Максимальная_цена,
          AVG(price) as Средня_цена
     FROM book
 GROUP BY author;

   SELECT author,
          ROUND(SUM(price*amount),2) AS Стоимость,
          ROUND((SUM(price*amount)*18/100/(1+18/100)),2) AS НДС,
          ROUND(SUM(price*amount)/(1+18/100),2) AS Стоимость_без_НДС
     FROM book
 GROUP BY author;
   SELECT MIN(price) AS Минимальная_цена,
          MAX(price) AS Максимальная_цена,
          ROUND(AVG(price),2) AS Средняя_цена
     FROM book;

   SELECT ROUND(AVG(price),2) AS Средняя_цена,
          ROUND(SUM(price * amount),2) AS Стоимость
     FROM book
 WHERE amount BETWEEN 5 and 14;

   SELECT author,
          SUM(price * amount) as Стоимость
     FROM book
    WHERE title <> "Идиот"
       OR "Белая гвардия"
    GROUP BY author
   HAVING SUM(price * amount) > 5000
 ORDER BY Стоимость DESC;

   SELECT author,
          COUNT(title) AS Количество_произведений,
          MIN(price) AS Минимальная_цена,
          SUM(amount) AS Число_книг
     FROM book
    WHERE price > 500
          AND amount >1
 GROUP BY author
   HAVING COUNT(title) > 1;

/* Subquery */
  SELECT author, title, ROUND(price,2) as price
    FROM book
   WHERE price <= (
         SELECT AVG(price)
         FROM book)
ORDER BY price DESC

  SELECT author, title, price
    FROM book
   WHERE (price - (SELECT MIN(price) FROM book))< 150
ORDER BY price ASC;

