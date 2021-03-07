CREATE TABLE windspeed (
  id BIGINT NOT NULL AUTO_INCREMENT,
  windspeed FLOAT NOT NULL,
  ts INTEGER NOT NULL,
  insert_dttm TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);

CREATE TABLE winddirection (
  id BIGINT NOT NULL AUTO_INCREMENT,
  winddirection enum('N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW') NOT NULL,
  ts INTEGER NOT NULL,
  insert_dttm TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);

CREATE TABLE temperature (
  id BIGINT NOT NULL AUTO_INCREMENT,
  temperature FLOAT NOT NULL,
  ts INTEGER NOT NULL,
  insert_dttm TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);

CREATE TABLE humidity (
  id BIGINT NOT NULL AUTO_INCREMENT,
  humidity TINYINT(4) NOT NULL,
  ts INTEGER NOT NULL,
  insert_dttm TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);

CREATE TABLE rain (
  id BIGINT NOT NULL AUTO_INCREMENT,
  rain TINYINT(4) NOT NULL,
  ts INTEGER NOT NULL,
  insert_dttm TIMESTAMP NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);
