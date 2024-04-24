-- 1. Write a regular expression to match email addresses.
DROP TABLE IF EXISTS t;
CREATE TABLE t (line TEXT);
\copy t FROM 'mbox-short.txt' with delimiter E'\007';
-- SELECT substring(line, '([^ ]+@[^ ]+)') FROM t;
-- 2. Create a regular expression to extract all the hashtags from a given text.
-- SELECT substring(line, '([^ ]+#[^ ]+)') FROM t;
-- 3. Write a regular expression to find all the URLs in a string.
-- SELECT substring(line, '([^ ]+http[^ ]+)') FROM t;
-- 4. Create a regular expression to validate a phone number.
SELECT substring(line, '([^ ]+\d{3}-\d{3}-\d{4})') FROM t;  
-- 5. Write a regular expression to extract all the words that start with a vowel.

-- 6. Create a regular expression to extract all the numbers from a string.

-- 7. Write a regular expression to match IP addresses.

-- 8. Create a regular expression to validate a password (at least 8 characters, at least one uppercase letter, one lowercase letter, and one number).

-- 9. Write a regular expression to extract all the mentions (starting with '@') from a text.

-- 10. Create a regular expression to extract all the words that end with 'ing'.

-- 11. Write a regular expression to match date formats (dd/mm/yyyy or mm/dd/yyyy).

-- 12. Create a regular expression to match HTML tags.

-- 13. Write a regular expression to extract all the words that contain only vowels.

-- 14. Create a regular expression to extract all the words that contain only consonants.

-- 15. Write a regular expression to extract all the words that are exactly 5 characters long.

-- 16. Create a regular expression to match currency values (e.g., $100.00).

-- 17. Write a regular expression to extract all the words that start and end with the same letter.

-- 18. Create a regular expression to match a hexadecimal color code (e.g., #aabbcc).

-- 19. Write a regular expression to extract all the words that contain a repeated letter (e.g., 'book', 'noon').

-- 20. Create a regular expression to match a time in 24-hour format (e.g., 13:45).

-- 21. Write a regular expression to extract all the words that are palindromes.

-- 22. Create a regular expression to match a string that starts with 'http://' or 'https://'.

-- 23. Write a regular expression to extract all the words that have at least one uppercase letter.

-- 24. Create a regular expression to match a string that contains exactly 3 digits.

-- 25. Write a regular expression to extract all the words that have alternating vowels and consonants (e.g., 'aba', 'mom').

-- 26. Create a regular expression to match a string that contains only letters and spaces.

-- 27. Write a regular expression to extract all the words that contain a double letter (e.g., 'book', 'letter').

-- 28. Create a regular expression to match a string that contains exactly 3 uppercase letters.

-- 29. Write a regular expression to extract all the words that contain the letter 'z'.

-- 30. Create a regular expression to match a string that contains only letters, numbers, and underscores.