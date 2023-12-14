
USE abikpi;
CREATE TABLE applicants (
applicant_id INTEGER PRIMARY KEY,
applicant_name VARCHAR(100),
document_id INTEGER UNIQUE KEY,
gender VARCHAR(10),
quota VARCHAR(100),
applicant_email VARCHAR(100),
applicant_password VARCHAR(100) 
);

USE abikpi;
INSERT INTO applicants
VALUES (1,'Безклинська Валерія Вікторівна', 1, 'Ж', 'Ні', 'bezklinskalera@gmail.com', '1111');



USE abikpi;
DROP TABLE applicants;