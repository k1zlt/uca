-- Regular Expressions:
-- Write a regular expression to find all the URLs in a string.
DROP TABLE IF EXISTS t;
CREATE TABLE t (s TEXT);
INSERT INTO t (s) VALUES ('Visit us at http://example.com');
INSERT INTO t (s) VALUES ('Check out our website at https://google.com. And this one: http://youtube.com/1234');

SELECT s, 
    REGEXP_MATCHES(s, 'http[s]?:\/\/[a-zA-Z0-9.\/]+', 'g') AS urls
FROM t;
-- Create a regular expression to validate a phone number.
DROP TABLE IF EXISTS t;
CREATE TABLE t (s TEXT);
INSERT INTO t (s) VALUES ('123-456-7890');
INSERT INTO t (s) VALUES ('(123) 456-7890');
INSERT INTO t (s) VALUES ('123.456.7890');
INSERT INTO t (s) VALUES ('1234567890');

SELECT s,
    REGEXP_LIKE(s, '^\(?([0-9]{3})\)?[- ]?([0-9]{3})[- ]?([0-9]{4})$') AS is_valid
FROM t;
-- Write a regular expression to match IP addresses.
DROP TABLE IF EXISTS t;
CREATE TABLE t (s TEXT);
INSERT INTO t (s) VALUES ('0.0.0.0');
INSERT INTO t (s) VALUES ('256.256.256.2222');
INSERT INTO t (s) VALUES ('12.12.12.12');

SELECT s, 
    REGEXP_LIKE(s, '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$') AS is_valid
FROM t;
-- Write a regular expression to match date formats (dd/mm/yyyy or mm/dd/yyyy).
DROP TABLE IF EXISTS t;
CREATE TABLE t (s TEXT);
INSERT INTO t (s) VALUES ('01/01/2020');
INSERT INTO t (s) VALUES ('12/31/2020');
INSERT INTO t (s) VALUES ('31/12/2020');
INSERT INTO t (s) VALUES ('2020/01/01');

SELECT s, 
    REGEXP_LIKE(s, '^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/[0-9]{4}$') AS is_valid
FROM t;
-- Create a regular expression to match HTML tags.
DROP TABLE IF EXISTS t;
CREATE TABLE t (s TEXT);
INSERT INTO t (s) VALUES ('<p>Hello, World!</p>');
INSERT INTO t (s) VALUES ('<div class="container">Content</div>');

SELECT s, 
    REGEXP_REPLACE(s, '<[^>]+>', 'TAG') AS replaced,
    REGEXP_MATCHES(s, '<[^>]+>', 'g') AS tags
FROM t;
-- Create a regular expression to match a time in 24-hour format (e.g., 13:45).
DROP TABLE IF EXISTS t;
CREATE TABLE t (s TEXT);
INSERT INTO t (s) VALUES ('13:45');
INSERT INTO t (s) VALUES ('24:00');
INSERT INTO t (s) VALUES ('12:00 AM');
INSERT INTO t (s) VALUES ('12:00 PM');

SELECT s, 
    REGEXP_LIKE(s, '^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$') AS is_valid
FROM t;
