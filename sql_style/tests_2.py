/* Data trasform and load */

CREATE table supply (
 supply_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(50),
 author VARCHAR(30),
  price DECIMAL(8,2),
 amount INT);

INSERT INTO supply (title, author, price, amount)
VALUES ("Лирика", "Пастернак Б.Л.", 518.99, 2),
VALUES ("Черный человек", "Есенин С.А.", 570.2, 6),
VALUES ("Белая гвардия", "Булгаков М.А.", 540.5, 7),
VALUES ("Идиот", "Достоевский Ф.М.", 360.8, 3);


INSERT INTO book (title, author, price, amount)
SELECT title, author, price, amount
  FROM supply
 WHERE author != "Булгаков М.А" AND author != "Достоевский Ф.М.";



