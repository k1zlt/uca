DROP TABLE IF EXISTS unesco_raw CASCADE;
CREATE TABLE unesco_raw (
    name TEXT, 
    description TEXT, 
    justification TEXT, 
    year INTEGER,
    longitude FLOAT, 
    latitude FLOAT, 
    area_hectares FLOAT,
    category TEXT, 
    category_id INTEGER, 
    state TEXT, 
    state_id INTEGER,
    region TEXT, 
    region_id INTEGER, 
    iso TEXT, 
    iso_id INTEGER
);

DROP TABLE IF EXISTS category CASCADE; 
CREATE TABLE category (
  id SERIAL,
  name VARCHAR(128) UNIQUE,
  PRIMARY KEY(id)
);

DROP TABLE IF EXISTS state CASCADE; 
CREATE TABLE state (
  id SERIAL,
  name VARCHAR(128) UNIQUE,
  PRIMARY KEY(id)
);

DROP TABLE IF EXISTS region CASCADE; 
CREATE TABLE region (
  id SERIAL,
  name VARCHAR(128) UNIQUE,
  PRIMARY KEY(id)
);

DROP TABLE IF EXISTS iso CASCADE; 
CREATE TABLE iso (
  id SERIAL,
  name VARCHAR(128) UNIQUE,
  PRIMARY KEY(id)
);

DROP TABLE IF EXISTS unesco CASCADE;
CREATE TABLE unesco (
    name TEXT,
    year INT,
    category_id INT,
    state_id INT,
    region_id INT,
    iso_id INT,
    FOREIGN KEY (category_id) references category(id) on delete CASCADE,
    FOREIGN KEY (state_id) references state(id) on delete CASCADE,
    FOREIGN KEY (region_id) references region(id) on delete CASCADE,
    FOREIGN KEY (iso_id) references iso(id) on delete CASCADE
);

\copy unesco_raw(name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso) FROM 'whc-sites-2018-small.csv' WITH DELIMITER ',' CSV HEADER;

INSERT INTO category(name) select DISTINCT category from unesco_raw;
INSERT INTO state(name) select DISTINCT state from unesco_raw;
INSERT INTO region(name) select DISTINCT region from unesco_raw;
INSERT INTO iso(name) select DISTINCT iso from unesco_raw;

UPDATE unesco_raw set category_id = (select id from category where unesco_raw.category = category.name);
UPDATE unesco_raw set state_id = (select id from state where unesco_raw.state = state.name);
UPDATE unesco_raw set region_id = (select id from region where unesco_raw.region = region.name);
UPDATE unesco_raw set iso_id = (select id from iso where unesco_raw.iso = iso.name);

INSERT INTO unesco (name, year, category_id, state_id, region_id, iso_id) select name, year, category_id, state_id, region_id, iso_id from unesco_raw;
