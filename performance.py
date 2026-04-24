
SCHOOL PERFORMANCE ANALYSIS DATABASE
   
CREATE TABLE Year_Group (
    year_group_id INTEGER PRIMARY KEY ,
    year_group_name TEXT NOT NULL,
    academic_year TEXT NOT NULL
);

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    date_of_birth DATE,
    year_group_id INTEGER,
    FOREIGN KEY (year_group_id) REFERENCES Year_Group(year_group_id)
);

CREATE TABLE Teachers (
    teacher_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department TEXT
);

CREATE TABLE Subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

CREATE TABLE Exams (
    exam_id INTEGER PRIMARY KEY,
    subject_id INTEGER NOT NULL,
    exam_name TEXT NOT NULL,
    exam_date DATE,
    max_score INTEGER DEFAULT 100,
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

CREATE TABLE Scores (
    score_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    exam_id INTEGER NOT NULL,
    score INTEGER CHECK(score BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (exam_id) REFERENCES Exams(exam_id)
);

CREATE TABLE Attendance (
    attendance_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    student_id INTEGER NOT NULL,
    attendance_date DATE,
    status TEXT CHECK(status IN ('Present', 'Absent')),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

INSERT SAMPLE DATA 

INSERT INTO Year_Group VALUES
(1, 'Year 1', '2024/2025'),
(2, 'Year 2', '2024/2025'),
(3, 'Year 3', '2024/2025');


INSERT INTO Students VALUES
(287,'Ahmed','Hassan','Male','2005-03-18',2),
(154,'Priya','Sharma','Female','2006-07-22',1),
(392,'Kwame','Mensah','Male','2004-11-09',3),
(118,'Sara','Mohammed','Female','2007-02-14',1),
(341,'Rahul','Verma','Male','2006-09-01',3),
(209,'Amina','Diallo','Female','2005-06-27',2),
(375,'Chinedu','Eze','Male','2004-12-03',3),
(162,'Fatou','Camara','Female','2006-04-19',1),
(299,'Yusuf','Abdullah','Male','2005-01-11',2),
(181,'Ananya','Iyer','Female','2007-08-05',1),
(326,'Samuel','Okafor','Male','2006-10-29',3),
(145,'Omar','Khalid','Male','2004-05-16',1),
(388,'Neha','Gupta','Female','2005-07-30',3),
(214,'Ibrahim','Sule','Male','2006-02-09',2),
(359,'Zainab','Abubakar','Female','2007-11-21',3),
(197,'Daniel','Kimani','Male','2004-06-14',1),
(312,'Kunal','Mehta','Male','2005-09-07',3),
(168,'Layla','Farouk','Female','2006-01-25',1),
(284,'Moses','Otieno','Male','2007-03-10',2),
(139,'Rohan','Singh','Male','2004-10-02',1),
(367,'Salma','Youssef','Female','2005-02-28',3),
(223,'Arjun','Patel','Male','2006-12-18',2),
(395,'Emeka','Obi','Male','2004-08-06',3),
(176,'Aisha','Rahman','Female','2005-04-23',1),
(248,'Sanjay','Malhotra','Male','2007-01-15',2),
(331,'Hannah','Bekele','Female','2006-06-09',3),
(158,'Noor','Hamdan','Female','2004-09-27',1),
(279,'Tunde','Adebayo','Male','2005-11-12',2),
(354,'Nikhil','Reddy','Male','2006-03-04',3),
(191,'Mariam','Saleh','Female','2007-05-30',1),
(318,'Vikram','Joshi','Male','2004-02-19',3),
(266,'Abdul','Nasser','Male','2005-08-24',2),
(173,'Fatima','Ali','Female','2006-10-11',1),
(304,'Musa','Lawal','Male','2004-07-08',3),
(142,'Pooja','Nair','Female','2007-09-16',1),
(381,'Rashid','AlFarid','Male','2005-12-05',3),
(257,'Nadia','Yakubu','Female','2006-04-01',2),
(364,'Kareem','Aziz','Male','2004-01-26',3),
(189,'Salma','Nouri','Female','2007-06-13',1),
(347,'James','Otis','Male','2005-03-20',3);


INSERT INTO Teachers VALUES
(1, 'Mellisa', 'Himaaya', 'Molecular Biology'),
(2, 'Shahidi', 'Wilkr', 'Biochemistry'),
(3, 'David', 'Shonekan', 'Physics'),
(4, 'Emma', 'Davis', 'Introduction to Mathematics'),
(5, 'Oladeji', 'Olukoya', 'Chemistry'),
(6, 'Zaire', 'Jones', 'English Literature'),
(7, 'Michael', 'Dixon', 'Genetics');

INSERT INTO Subjects VALUES
(200, 'Molecular Biology ', 1),
(101, 'Biochemistry', 2),
(300, 'Physics', 3),
(100, 'Introduction to Mathematics', 4),
(301, 'Chemistry', 5),
(411, 'English Literature', 6),
(417, 'Genetics', 7);

INSERT INTO Exams VALUES
(1, 200, 'Semester 1', '2026-01-15', 100),
(2, 101, 'Semester 2', '2025-01-20', 100),
(3, 300, 'Semester 1', '2025-01-25', 100),
(4, 100, 'Semester 2', '2025-01-30', 100),
(5, 301, 'Semester 1', '2025-02-05', 100),
(6, 411, 'Semester 2', '2025-02-10', 100),
(7, 417, 'Semester 1', '2025-02-15', 100);

INSERT INTO Scores VALUES
(1,287,3,72),
(2,154,1,81),
(3,392,5,68),
(4,118,1,75),
(5,341,5,82),
(6,209,3,70),
(7,375,5,64),
(8,162,1,79),
(9,299,3,73),
(10,181,1,88),
(11,326,5,91),
(12,145,2,66),
(13,388,5,85),
(14,214,3,69),
(15,359,5,74),
(16,197,1,77),
(17,312,5,83),
(18,168,1,71),
(19,284,3,76),
(20,139,1,84),
(21,367,5,90),
(22,223,3,68),
(23,395,5,72),
(24,176,1,80),
(25,248,3,65),
(26,331,5,88),
(27,158,1,74),
(28,279,3,79),
(29,354,5,86),
(30,191,1,82),
(31,318,5,77),
(32,266,3,69),
(33,173,2,73),
(34,304,5,91),
(35,142,1,78),
(36,381,5,84),
(37,257,3,71),
(38,364,5,67),
(39,189,1,83),
(40,347,5,88);

INSERT INTO Attendance (attendance_id, student_id, attendance_date, status) VALUES
(2,287,'2025-01-11','Present'),
(1,154,'2025-01-11','Present'),
(3,392,'2025-01-11','Absent'),
(1,118,'2025-01-11','Present'),
(3,341,'2025-01-11','Present'),
(2,209,'2025-01-11','Present'),
(3,375,'2025-01-11','Absent'),
(1,162,'2025-01-11','Present'),
(2,299,'2025-01-11','Present'),
(1,181,'2025-01-11','Present'),
(3,326,'2025-01-11','Present'),
(1,145,'2025-01-11','Absent'),
(3,388,'2025-01-11','Present'),
(2,214,'2025-01-11','Present'),
(3,359,'2025-01-11','Absent'),
(1,197,'2025-01-11','Present'),
(3,312,'2025-01-11','Present'),
(1,168,'2025-01-11','Present'),
(2,284,'2025-01-11','Present'),
(1,139,'2025-01-11','Absent'),
(3,367,'2025-01-11','Present'),
(2,223,'2025-01-11','Present'),
(3,395,'2025-01-11','Absent'),
(1,176,'2025-01-11','Present'),
(2,248,'2025-01-11','Present'),
(3,331,'2025-01-11','Present'),
(1,158,'2025-01-11','Absent'),
(2,279,'2025-01-11','Present'),
(3,354,'2025-01-11','Present'),
(1,191,'2025-01-11','Present'),
(3,318,'2025-01-11','Present'),
(2,266,'2025-01-11','Absent'),
(1,173,'2025-01-11','Present'),
(3,304,'2025-01-11','Present'),
(1,142,'2025-01-11','Present'),
(3,381,'2025-01-11','Absent'),
(2,257,'2025-01-11','Present'),
(3,364,'2025-01-11','Present'),
(1,189,'2025-01-11','Present'),
(3,347,'2025-01-11','Present');




PERFORMANCE ANALYSIS QUERIES 
ATTENDANCE ANALYSIS

Attendance per subject vs performance 
SELECT
    sub.subject_name,
    ROUND(AVG(CASE WHEN a.status = 'Present' THEN 1.0 ELSE 0.0 END) * 100,2) AS average_attendance_percentage,
    ROUND(AVG(sc.score), 2) AS average_score
FROM Attendance a
JOIN Students s ON a.student_id = s.student_id
JOIN Scores sc ON s.student_id = sc.student_id
JOIN Exams e ON sc.exam_id = e.exam_id
JOIN Subjects sub ON e.subject_id = sub.subject_id
GROUP BY sub.subject_id
ORDER BY sub.subject_name;

Attendance per year group vs performance 
SELECT
    CASE s.year_group_id
        WHEN 1 THEN 'Year 1'
        WHEN 2 THEN 'Year 2'
        WHEN 3 THEN 'Year 3'
    END AS year_group,
    ROUND(AVG(CASE WHEN a.status = 'Present' THEN 1.0 ELSE 0.0 END ) * 100,2) AS average_attendance_percentage,
    ROUND(AVG(sc.score), 2) AS average_score
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY s.year_group_id
ORDER BY s.year_group_id;

TEACHER PERFORMANCE ANALYSIS
1.Teacher vs attendance vs performance
SELECT
    t.first_name || ' ' || t.last_name AS teacher_name,
    sub.subject_name,
    ROUND(AVG(CASE WHEN a.status = 'Present' THEN 1.0 ELSE 0.0 END) * 100,2) AS average_attendance_percentage,
    ROUND(AVG(sc.score), 2) AS average_student_score
FROM Teachers t
JOIN Subjects sub ON t.teacher_id = sub.teacher_id
JOIN Exams e ON sub.subject_id = e.subject_id
JOIN Scores sc ON e.exam_id = sc.exam_id
JOIN Attendance a ON sc.student_id = a.student_id
GROUP BY t.teacher_id, sub.subject_id
ORDER BY average_student_score DESC;

YEAR GROUP PERFORMANCE ANALYSIS
1.Year group vs attendance vs performance 
 SELECT
    CASE s.year_group_id
        WHEN 1 THEN 'Year 1'
        WHEN 2 THEN 'Year 2'
        WHEN 3 THEN 'Year 3'
    END AS year_group,
    ROUND(AVG(CASE WHEN a.status = 'Present' THEN 1.0 ELSE 0.0 END) * 100,2) AS average_attendance_percentage,
    ROUND(AVG(sc.score), 2) AS average_score
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY s.year_group_id
ORDER BY s.year_group_id;

2.Year group vs Attendance vs subject performance
SELECT
    CASE s.year_group_id
        WHEN 1 THEN 'Year 1'
        WHEN 2 THEN 'Year 2'
        WHEN 3 THEN 'Year 3'
    END AS year_group,
    sub.subject_name,
    ROUND(AVG(CASE WHEN a.status = 'Present' THEN 1.0 ELSE 0.0 END) * 100,2) AS average_attendance_percentage,
    ROUND(AVG(sc.score), 2) AS average_subject_score
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
JOIN Scores sc ON s.student_id = sc.student_id
JOIN Exams e ON sc.exam_id = e.exam_id
JOIN Subjects sub ON e.subject_id = sub.subject_id
GROUP BY s.year_group_id, sub.subject_id
ORDER BY s.year_group_id, sub.subject_name;


STUDENT PERFORMANCE ANALYSIS
1.Student vs average subject scores
SELECT
    s.student_id,
    s.first_name || ' ' || s.last_name AS student_name,
    sub.subject_name,
    ROUND(AVG(sc.score), 2) AS average_subject_score
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
JOIN Exams e ON sc.exam_id = e.exam_id
JOIN Subjects sub ON e.subject_id = sub.subject_id
GROUP BY s.student_id, sub.subject_id
ORDER BY s.student_id, sub.subject_name;

2.Student vs all subjects average score
SELECT
    s.student_id,
    s.first_name || ' ' || s.last_name AS student_name,
    ROUND(AVG(sc.score), 2) AS overall_average_score
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY s.student_id
ORDER BY overall_average_score DESC;

SUBJECT PERFORMANCE ANALYSIS
1.subject vs average scrore per year group
SELECT
    sub.subject_name,
    CASE s.year_group_id
        WHEN 1 THEN 'Year 1'
        WHEN 2 THEN 'Year 2'
        WHEN 3 THEN 'Year 3'
    END AS year_group,
    ROUND(AVG(sc.score), 2) AS average_score
FROM Scores sc
JOIN Students s ON sc.student_id = s.student_id
JOIN Exams e ON sc.exam_id = e.exam_id
JOIN Subjects sub ON e.subject_id = sub.subject_id
GROUP BY sub.subject_id, s.year_group_id
ORDER BY sub.subject_name, s.year_group_id;
`
2.Subject vs average attendance vs average performance
SELECT
    sub.subject_name,
    ROUND(AVG(CASE WHEN a.status = 'Present' THEN 1.0 ELSE 0.0 END) * 100,2) AS average_attendance_percentage,
    ROUND(AVG(sc.score), 2) AS average_subject_score
FROM Subjects sub
JOIN Exams e ON sub.subject_id = e.subject_id
JOIN Scores sc ON e.exam_id = sc.exam_id
JOIN Students s ON sc.student_id = s.student_id
JOIN Attendance a ON s.student_id = a.student_id
GROUP BY sub.subject_id
ORDER BY average_subject_score DESC;
