DROP TABLE IF EXISTS album;
CREATE TABLE album (
  id SERIAL,
  title VARCHAR(128) UNIQUE,
  PRIMARY KEY(id)
);

DROP TABLE IF EXISTS track;
CREATE TABLE track (
    id SERIAL,
    title VARCHAR(128),
    len INTEGER, 
    rating INTEGER, 
    count INTEGER,
    album_id INTEGER REFERENCES album(id) ON DELETE CASCADE,
    UNIQUE(title, album_id),
    PRIMARY KEY(id)
);

DROP TABLE IF EXISTS track_raw;
CREATE TABLE track_raw (
    title TEXT, 
    artist TEXT, 
    album TEXT, 
    album_id INTEGER, 
    count INTEGER, 
    rating INTEGER, 
    len INTEGER
);

\copy track_raw(title, artist, album, count, rating, len) from library.csv DELIMITER ',' CSV;

INSERT INTO album(title) SELECT DISTINCT album from track_raw;

UPDATE track_raw set album_id = (select album.id from album where album.title=track_raw.album);

INSERT INTO track (title, len, rating, count, album_id) select title, len, rating, count, album_id from track_raw;