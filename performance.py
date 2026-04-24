
   SCHOOL PERFORMANCE ANALYSIS DATABASE
   
CREATE TABLE Classes (
    class_id INTEGER PRIMARY KEY ,
    class_name TEXT NOT NULL,
    academic_year TEXT NOT NULL
);

CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    date_of_birth DATE,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES Classes(class_id)
);

CREATE TABLE Teachers (
    teacher_id INTEGER PRIMARY,
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
    attendance_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    attendance_date DATE,
    status TEXT CHECK(status IN ('Present', 'Absent')),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

INSERT SAMPLE DATA 

INSERT INTO Classes VALUES
(1, 'Year 1', '2024/2025'),
(2, 'Year 1', '2024/2025'),
(3, 'Year 2', '2024/2025'),
(4, 'Year 3', '2024/2025'),
(5, 'Year 2', '2024/2025'),
(6, 'Year 1', '2024/2025'),
(7, 'Year 1', '2024/2025'),
(8, 'Year 1', '2024/2025'),
(9, 'Year 2', '2024/2025'),
(10, 'Year 3','2024/2025');

INSERT INTO Students VALUES
(101, 'John', 'Doe', 'Male', '2007-05-12', 1),
(102, 'Jane', 'Smith', 'Female', '2006-11-20', 1),
(203, 'Alice', 'Brown', 'Female', '2006-03-18', 2),
(304, 'Bob', 'Davis', 'Male', '2005-09-25', 3),
(205, 'Charlie', 'Miller', 'Male', '2006-07-30', 4),
(106, 'Emily', 'Wilson', 'Female', '2005-12-15', 5),
(107, 'David', 'Taylor', 'Male', '2006-10-10', 6),
(108, 'Sophia', 'Anderson', 'Female', '2005-08-22', 7),
(209, 'Michael', 'Thomas', 'Male', '2006-02-14', 8),
(310, 'Olivia', 'Moore', 'Female', '2005-04-18', 9);

INSERT INTO Teachers VALUES
(1, 'Mark', 'Johnson', 'Molecular Biology'),
(2, 'Lucy', 'Wilson', 'Biochemistry'),
(3, 'David', 'Smith', 'Physics'),
(4, 'Emma', 'Davis', 'Introduction to Mathematics'),
(5, 'James', 'Brown', 'Chemistry')
(6, 'Sarah', 'Miller', 'English Literature'),
(7, 'Robert', 'Taylor', 'Genetics'),;

INSERT INTO Subjects VALUES
(MB1, 'Molecular Biology ', 1),
(BC1, 'Biochemistry', 2),
(PH1, 'Physics', 3),
(IM1, 'Introduction to Mathematics', 4),
(CH1, 'Chemistry', 5),
(EL1, 'English Literature', 6),
(GE1, 'Genetics', 7);

INSERT INTO Exams VALUES
(1, MB1, 'Semester 1', '2026-01-15', 100),
(2, BC1, 'Semester 2', '2025-01-20', 100),
(3, PH1, 'Semester 1', '2025-01-25', 100),
(4, IM1, 'Semester 2', '2025-01-30', 100),
(5, CH1, 'Semester 1', '2025-02-05', 100),
(6, EL1, 'Semester 2', '2025-02-10', 100),
(7, GE1, 'Semester 1', '2025-02-15', 100);

INSERT INTO Scores VALUES
(1, 101, 1, 85),
(2, 102, 1, 90),
(3, 203, 2, 68)
(4, 304, 3, 92),
(5, 205, 4, 80),        
(6, 106, 5, 40),
(7, 107, 6, 78),
(8, 108, 7, 52),
(9, 209, 1, 87),
(10, 310, 2, 51);

INSERT INTO Attendance VALUES
(1, 101, '2025-01-10', 'Present'),
(2, 102, '2025-01-11', 'Present'),
(3, 203, '2025-01-10', 'Absent'),
(4, 304, '2025-01-10', 'Present'),
(5, 205, '2025-01-11', 'Present'),
(6, 106, '2025-01-10', 'Absent'),
(7, 107, '2025-01-11', 'Present'),
(8, 108, '2025-01-10', 'Present'),
(9, 209, '2025-01-11', 'Present'),
(10, 310, '2025-01-10', 'Absent');


/* ---------- PERFORMANCE ANALYSIS QUERIES ---------- */

/* Average score per student */
SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    AVG(sc.score) AS average_score
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY s.student_id;

/* Average score per subject */
SELECT
    sub.subject_name,
    AVG(sc.score) AS average_score
FROM Subjects sub
JOIN Exams e ON sub.subject_id = e.subject_id
JOIN Scores sc ON e.exam_id = sc.exam_id
GROUP BY sub.subject_name;

/* Top performing students */
SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    AVG(sc.score) AS average_score
FROM Students s
JOIN Scores sc ON s.student_id = sc.student_id
GROUP BY s.student_id
HAVING AVG(sc.score) >= 85
ORDER BY average_score DESC;

/* Attendance vs performance */
SELECT
    s.first_name || ' ' || s.last_name AS student_name,
    COUNT(a.attendance_id) AS days_present,
    AVG(sc.score) AS average_score
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
JOIN Scores sc ON s.student_id = sc.student_id
WHERE a.status = 'Present'
GROUP BY s.student_id;