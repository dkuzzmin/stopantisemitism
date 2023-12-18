CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    post_text TEXT NOT NULL,
    post_time TIMESTAMP NOT NULL,
    platform_id INTEGER,
    author VARCHAR(255),
    meta_info JSON
);

CREATE TABLE platforms (
    platform_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    url VARCHAR(255),
	country VARCHAR(50)
);

CREATE TABLE patterns (
    pattern_id SERIAL PRIMARY KEY,
    pattern_text VARCHAR(255) NOT NULL,
    severity_level INTEGER,
    category VARCHAR(100),
    context TEXT,
    source VARCHAR(255)
);

CREATE TABLE results (
    result_id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(post_id),
    analysis_result VARCHAR(100) NOT NULL,
    analysis_time TIMESTAMP NOT NULL,
    notes TEXT
);



SELECT * FROM posts
SELECT * FROM platforms
SELECT * FROM patterns
SELECT * FROM results


INSERT INTO patterns (pattern_text, severity_level) VALUES
('Zionist conspiracy', 4),
('Jewish lobby', 3),
('Holocaust hoax', 5),
('Jewish control', 4),
('Stereotypes about Jewish greed', 3),
('Blood libel myths', 5),
('Global Jewish dominance', 4),
('Jewish manipulation of media', 4),
('Jews and world finance', 3),
('Jewish banking conspiracy', 4),
('Protocols of the Elders of Zion', 5),
('Jewish nepotism', 3),
('Dual loyalty accusations', 4),
('Jewish globalist agenda', 4),
('Jews and political influence', 3),
('Jewish favoritism', 2),
('Rothschild conspiracy', 4),
('Jewish scapegoating', 3),
('Anti-Israel as a cover for anti-Semitism', 4),
('Jewish stereotypes in media', 3),
('Jewish world order', 4),
('Jews and the media', 3),
('Jewish control of banks', 4),
('Anti-Zionism equated with anti-Semitism', 3),
('Jewish conspiracy theories', 4),
('Jewish power and influence', 4),
('Jews as scapegoats', 3),
('Jews controlling governments', 4),
('Jews and financial manipulation', 3),
('Jewish control of Hollywood', 4),
('Jews and the slave trade myth', 3),
('Jewish domination in business', 3),
('Jews and usury', 4),
('Jews and global politics', 3),
('Jewish monopolies', 3),
('Jews and the Federal Reserve', 4),
('Jewish control of the press', 4),
('Jews and the spread of communism', 3),
('Jewish influence in politics', 3),
('Jews as global puppet masters', 4),
('Jewish control of the economy', 4),
('Jews corrupting society', 3),
('Jews and moral decay', 3),
('Jews and cultural Marxism', 3),
('Jews as the chosen people', 2),
('Jewish manipulation of history', 3),
('Jews as enemies of Christianity', 4),
('Jewish elitism', 3),
('Jews and the New World Order', 4),
('Jews as warmongers', 3),
('Jewish control of education', 4),
('Jewish media bias', 3),
('Jews spreading atheism', 2),
('Jewish influence in academia', 3),
('Jewish cultural infiltration', 3),
('Jews and political correctness', 3),
('Jews and liberalism', 2),
('Jewish influence in finance', 4),
('Jews controlling foreign policy', 4),
('Jewish influence in the arts', 3),
('Jews and multiculturalism', 2),
('Jews undermining national identity', 4),
('Jewish influence in science', 3),
('Jews and secularism', 2),
('Jews as Bolsheviks', 3),
('Jewish control of social media', 3),
('Jews and immigration policies', 3),
('Jewish influence on government decisions', 4),
('Jews and left-wing politics', 2),
('Jewish promotion of globalism', 3),
('Jews as radicals', 2),
('Jewish influence in economics', 4),
('Jews and the spread of socialism', 3),
('Jewish control of technology', 3),
('Jews in high positions', 3),
('Jewish influence in law', 4),
('Jews and the promotion of LGBT rights', 2),
('Jews in influential roles', 3),
('Jews as masterminds', 4),
('Jews controlling world events', 4),
('Jews and social manipulation', 3),
('Jewish influence in global affairs', 3),
('Jews as orchestrators of chaos', 4),
('Jews as corrupt elites', 4),
('Jewish control of the arts', 3),
('Jews as underminers of tradition', 3),
('Jewish influence in moral debates', 3),

('Jews and the shaping of public opinion', 3),
('Jewish influence in cultural movements', 3),
('Jews as disruptors of society', 3),
('Jewish influence in international relations', 3),
('Jews and the erosion of family values', 3),
('Jews as promoters of secularism', 2),
('Jewish influence in the judiciary', 3),
('Jews and the promotion of diversity', 2),
('Jewish influence in historical narratives', 3),
('Jews as detractors of national interests', 3),
('Jewish influence in the United Nations', 3),
('Jews and the erosion of national sovereignty', 4),
('Jewish control of key industries', 4);



