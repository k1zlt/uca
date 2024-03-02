DROP TABLE if exists country CASCADE;
CREATE TABLE country (
  country_id serial PRIMARY KEY,
  country_name VARCHAR(50) NOT NULL
);

DROP TABLE if exists sport CASCADE;
CREATE TABLE sport (
  sport_id serial PRIMARY KEY,
  sport_name VARCHAR(50) NOT NULL
);

DROP TABLE if exists athlete CASCADE;
CREATE TABLE athlete (
  athlete_id serial PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  country_id INT,
  height INT,
  weight INT,
  age INT,
  FOREIGN KEY (country_id) REFERENCES country(country_id)
);

DROP TABLE if exists SportAthlete CASCADE;
CREATE TABLE SportAthlete (
  sport_id INT,
  athlete_id INT,
  FOREIGN KEY (sport_id) REFERENCES sport(sport_id),
  FOREIGN KEY (athlete_id) REFERENCES athlete(athlete_id)
);