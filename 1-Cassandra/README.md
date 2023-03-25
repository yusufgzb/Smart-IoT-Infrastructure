docker exec -it container_id bash

cqlsh

CREATE KEYSPACE cassandra_tutorial WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

USE cassandra_tutorial;

# Düzenlenecek

CREATE TABLE deneme_tablo ( id int PRIMARY KEY, name text, address text );

INSERT INTO deneme_tablo (id,name, address) VALUES(1,'yusuf', 'adres deneme1');

INSERT INTO deneme_tablo (id,name, address) VALUES(2,'11yusuf', 'adres deneme1');

INSERT INTO deneme_tablo (id,name, address) VALUES(3,'34yusuf', 'adres deneme1');

SELECT * FROM deneme_tablo;

exit

exit
