CREATE TABLE posts_db (
    post_id SERIAL PRIMARY KEY,
    post_text VARCHAR(5000) NOT NULL,
    author VARCHAR(255),
	url VARCHAR(255),
	platform_id INT,
	date TIMESTAMP
);

CREATE TABLE platforms (
    platform_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE patterns (
    ap_id SERIAL PRIMARY KEY,
    word VARCHAR(255) NOT NULL,
    antisem BOOlEAN
);

CREATE TABLE results (
    result_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL,
    asrating INT,
	antisem BOOlEAN
);


SELECT * FROM posts_db
SELECT * FROM platforms
SELECT * FROM patterns
SELECT * FROM results


