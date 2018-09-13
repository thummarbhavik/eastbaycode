DROP TABLE IF EXISTS eastbaycode.users;
CREATE TABLE users (
    id INT NOT NULL auto_increment PRIMARY KEY, 
    lastname VARCHAR(255) NOT NULL,
	firstname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE, 
    registered_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
DROP TABLE IF EXISTS eastbaycode.courses;
	CREATE TABLE courses (
	id INT NOT NULL auto_increment PRIMARY KEY,
	title VARCHAR(80),
	professor_id INT,
	startdate DATE,
	enddate DATE,
	FOREIGN KEY (professor_id) REFERENCES users(id)
	);
	
DROP TABLE IF EXISTS eastbaycode.problems;
	CREATE TABLE problems(
	id INT NOT NULL auto_increment PRIMARY KEY,
	title VARCHAR(80),
	creator_id INT,
	version INT,
	content TEXT,
	solution TEXT,
	FOREIGN KEY (creator_id) REFERENCES users(id)
	);
	
DROP TABLE IF EXISTS eastbaycode.examples;
	CREATE TABLE examples(
	id INT NOT NULL auto_increment PRIMARY KEY,
	input TEXT,
	output TEXT,
	problem_id INT,
	FOREIGN KEY (problem_id) REFERENCES problems(id)	
	);
		
DROP TABLE IF EXISTS eastbaycode.testcases;
	CREATE TABLE testcases(
	id INT NOT NULL auto_increment PRIMARY KEY,
	problem_id INT,
	input TEXT,
	output TEXT,
	flags TEXT,
	FOREIGN KEY (problem_id) REFERENCES problems(id)
	);
		
DROP TABLE IF EXISTS eastbaycode.submissions;
	CREATE TABLE submissions(
	id INT NOT NULL auto_increment PRIMARY KEY,
	student_id INT,
	problem_id INT,
	submission TEXT,
	FOREIGN KEY (student_id) REFERENCES users(id),
	FOREIGN KEY (problem_id) REFERENCES problems(id)
	);
	
DROP TABLE IF EXISTS eastbaycode.sub_results;
	CREATE TABLE sub_results(
	id INT NOT NULL auto_increment PRIMARY KEY,
	sub_id INT,
	pass BOOLEAN,
	failed_test_id INT,
	output TEXT,
	FOREIGN KEY (sub_id) REFERENCES submissions(id),
	FOREIGN KEY (failed_test_id) REFERENCES testcases(id)
	);
	
INSERT INTO eastbaycode.users(
	

