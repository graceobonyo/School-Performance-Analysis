import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# RAW DATA

year_group = pd.DataFrame([
    (1, 'Year 1', '2024/2025'),
    (2, 'Year 2', '2024/2025'),
    (3, 'Year 3', '2024/2025')
], columns=['year_group_id','year_group','academic_year'])

students = pd.DataFrame([
(287,'Ahmed','Hassan','Male','2005-03-18',2),(154,'Priya','Sharma','Female','2006-07-22',1),
(392,'Kwame','Mensah','Male','2004-11-09',3),(118,'Sara','Mohammed','Female','2007-02-14',1),
(341,'Rahul','Verma','Male','2006-09-01',3),(209,'Amina','Diallo','Female','2005-06-27',2),
(375,'Chinedu','Eze','Male','2004-12-03',3),(162,'Fatou','Camara','Female','2006-04-19',1),
(299,'Yusuf','Abdullah','Male','2005-01-11',2),(181,'Ananya','Iyer','Female','2007-08-05',1),
(326,'Samuel','Okafor','Male','2006-10-29',3),(145,'Omar','Khalid','Male','2004-05-16',1),
(388,'Neha','Gupta','Female','2005-07-30',3),(214,'Ibrahim','Sule','Male','2006-02-09',2),
(359,'Zainab','Abubakar','Female','2007-11-21',3),(197,'Daniel','Kimani','Male','2004-06-14',1),
(312,'Kunal','Mehta','Male','2005-09-07',3),(168,'Layla','Farouk','Female','2006-01-25',1),
(284,'Moses','Otieno','Male','2007-03-10',2),(139,'Rohan','Singh','Male','2004-10-02',1),
(367,'Salma','Youssef','Female','2005-02-28',3),(223,'Arjun','Patel','Male','2006-12-18',2),
(395,'Emeka','Obi','Male','2004-08-06',3),(176,'Aisha','Rahman','Female','2005-04-23',1),
(248,'Sanjay','Malhotra','Male','2007-01-15',2),(331,'Hannah','Bekele','Female','2006-06-09',3),
(158,'Noor','Hamdan','Female','2004-09-27',1),(279,'Tunde','Adebayo','Male','2005-11-12',2),
(354,'Nikhil','Reddy','Male','2006-03-04',3),(191,'Mariam','Saleh','Female','2007-05-30',1),
(318,'Vikram','Joshi','Male','2004-02-19',3),(266,'Abdul','Nasser','Male','2005-08-24',2),
(173,'Fatima','Ali','Female','2006-10-11',1),(304,'Musa','Lawal','Male','2004-07-08',3),
(142,'Pooja','Nair','Female','2007-09-16',1),(381,'Rashid','AlFarid','Male','2005-12-05',3),
(257,'Nadia','Yakubu','Female','2006-04-01',2),(364,'Kareem','Aziz','Male','2004-01-26',3),
(189,'Salma','Nouri','Female','2007-06-13',1),(347,'James','Otis','Male','2005-03-20',3)
], columns=['student_id','first_name','last_name','gender','dob','year_group_id'])

teachers = pd.DataFrame([
(1,'Mellisa','Himaaya'),(2,'Shahidi','Wilkr'),(3,'David','Shonekan'),
(4,'Emma','Davis'),(5,'Oladeji','Olukoya'),(6,'Zaire','Jones'),(7,'Michael','Dixon')
], columns=['teacher_id','teacher_first','teacher_last'])

subjects = pd.DataFrame([
(200,'Molecular Biology',1),(101,'Biochemistry',2),(300,'Physics',3),
(100,'Introduction to Mathematics',4),(301,'Chemistry',5),
(411,'English Literature',6),(417,'Genetics',7)
], columns=['subject_id','subject','teacher_id'])

exams = pd.DataFrame([
(1,200,'Semester 1','2026-01-15'),
(2,101,'Semester 2','2025-01-20'),
(3,300,'Semester 1','2025-01-25'),
(4,100,'Semester 2','2025-01-30'),
(5,301,'Semester 1','2025-02-05'),
(6,411,'Semester 2','2025-02-10'),
(7,417,'Semester 1','2025-02-15')
], columns=['exam_id','subject_id','exam','exam_date'])

scores = pd.DataFrame([
(287,3,72),(154,1,81),(392,5,68),(118,1,75),(341,5,82),(209,3,70),
(375,5,64),(162,1,79),(299,3,73),(181,1,88),(326,5,91),(145,2,66),
(388,5,85),(214,3,69),(359,5,74),(197,1,77),(312,5,83),(168,1,71),
(284,3,76),(139,1,84),(367,5,90),(223,3,68),(395,5,72),(176,1,80),
(248,3,65),(331,5,88),(158,1,74),(279,3,79),(354,5,86),(191,1,82),
(318,5,77),(266,3,69),(173,2,73),(304,5,91),(142,1,78),(381,5,84),
(257,3,71),(364,5,67),(189,1,83),(347,5,88)
], columns=['student_id','exam_id','score'])

attendance = pd.DataFrame([
# ======================
# SEPTEMBER 2024
# ======================
(287,'2024-09-16','Present'),(154,'2024-09-16','Present'),(392,'2024-09-16','Absent'),
(118,'2024-09-16','Present'),(341,'2024-09-16','Present'),(209,'2024-09-16','Present'),
(375,'2024-09-16','Absent'),(162,'2024-09-16','Present'),(299,'2024-09-16','Present'),
(181,'2024-09-16','Present'),(326,'2024-09-16','Present'),(145,'2024-09-16','Absent'),
(388,'2024-09-16','Present'),(214,'2024-09-16','Present'),(359,'2024-09-16','Absent'),
(197,'2024-09-16','Present'),(312,'2024-09-16','Present'),(168,'2024-09-16','Present'),
(284,'2024-09-16','Present'),(139,'2024-09-16','Absent'),
(367,'2024-09-16','Present'),(223,'2024-09-16','Present'),(395,'2024-09-16','Absent'),
(176,'2024-09-16','Present'),(248,'2024-09-16','Present'),(331,'2024-09-16','Present'),
(158,'2024-09-16','Absent'),(279,'2024-09-16','Present'),(354,'2024-09-16','Present'),
(191,'2024-09-16','Present'),(318,'2024-09-16','Present'),(266,'2024-09-16','Absent'),
(173,'2024-09-16','Present'),(304,'2024-09-16','Present'),(142,'2024-09-16','Present'),
(381,'2024-09-16','Absent'),(257,'2024-09-16','Present'),(364,'2024-09-16','Present'),
(189,'2024-09-16','Present'),(347,'2024-09-16','Present'),

# ======================
# OCTOBER 2024
# ======================
(287,'2024-10-16','Absent'),(154,'2024-10-16','Present'),(392,'2024-10-16','Present'),
(118,'2024-10-16','Present'),(341,'2024-10-16','Present'),(209,'2024-10-16','Present'),
(375,'2024-10-16','Present'),(162,'2024-10-16','Present'),(299,'2024-10-16','Absent'),
(181,'2024-10-16','Present'),(326,'2024-10-16','Present'),(145,'2024-10-16','Present'),
(388,'2024-10-16','Present'),(214,'2024-10-16','Present'),(359,'2024-10-16','Absent'),
(197,'2024-10-16','Present'),(312,'2024-10-16','Present'),(168,'2024-10-16','Present'),
(284,'2024-10-16','Present'),(139,'2024-10-16','Absent'),
(367,'2024-10-16','Present'),(223,'2024-10-16','Present'),(395,'2024-10-16','Absent'),
(176,'2024-10-16','Present'),(248,'2024-10-16','Present'),(331,'2024-10-16','Present'),
(158,'2024-10-16','Absent'),(279,'2024-10-16','Present'),(354,'2024-10-16','Present'),
(191,'2024-10-16','Present'),(318,'2024-10-16','Present'),(266,'2024-10-16','Absent'),
(173,'2024-10-16','Present'),(304,'2024-10-16','Present'),(142,'2024-10-16','Present'),
(381,'2024-10-16','Absent'),(257,'2024-10-16','Present'),(364,'2024-10-16','Present'),
(189,'2024-10-16','Present'),(347,'2024-10-16','Present'),

# ======================
# NOVEMBER 2024
# ======================
(287,'2024-11-16','Present'),(154,'2024-11-16','Present'),(392,'2024-11-16','Absent'),
(118,'2024-11-16','Present'),(341,'2024-11-16','Absent'),(209,'2024-11-16','Present'),
(375,'2024-11-16','Absent'),(162,'2024-11-16','Present'),(299,'2024-11-16','Present'),
(181,'2024-11-16','Present'),(326,'2024-11-16','Present'),(145,'2024-11-16','Absent'),
(388,'2024-11-16','Present'),(214,'2024-11-16','Present'),(359,'2024-11-16','Absent'),
(197,'2024-11-16','Present'),(312,'2024-11-16','Present'),(168,'2024-11-16','Present'),
(284,'2024-11-16','Present'),(139,'2024-11-16','Absent'),
(367,'2024-11-16','Present'),(223,'2024-11-16','Present'),(395,'2024-11-16','Absent'),
(176,'2024-11-16','Present'),(248,'2024-11-16','Present'),(331,'2024-11-16','Present'),
(158,'2024-11-16','Absent'),(279,'2024-11-16','Present'),(354,'2024-11-16','Present'),
(191,'2024-11-16','Present'),(318,'2024-11-16','Present'),(266,'2024-11-16','Absent'),
(173,'2024-11-16','Present'),(304,'2024-11-16','Present'),(142,'2024-11-16','Present'),
(381,'2024-11-16','Absent'),(257,'2024-11-16','Present'),(364,'2024-11-16','Present'),
(189,'2024-11-16','Present'),(347,'2024-11-16','Present')
],
columns=['student_id','attendance_date','attendance_status'])

# MERGING ALL DATA INTO A SINGLE DATAFRAME FOR ANALYSIS

df = (
    students.merge(year_group, on='year_group_id')
    .merge(scores, on='student_id')
    .merge(exams, on='exam_id')
    .merge(subjects, on='subject_id')
    .merge(teachers, on='teacher_id')
    .merge(attendance, on='student_id')
)

df['student_name'] = df['first_name'] + ' ' + df['last_name']
df['teacher_name'] = df['teacher_first'] + ' ' + df['teacher_last']
df['present'] = (df['attendance_status'] == 'Present').astype(int)
df['attendance_date'] = pd.to_datetime(df['attendance_date'])

#RAW DATA CSV files

year_group.to_csv("year_group.csv", index=False)
students.to_csv("students.csv", index=False)
teachers.to_csv("teachers.csv", index=False)
subjects.to_csv("subjects.csv", index=False)
exams.to_csv("exams.csv", index=False)
scores.to_csv("scores.csv", index=False)
attendance.to_csv("attendance.csv", index=False)


# ANALYSIS CSV files 

df.groupby('subject').agg(
    average_attendance_percentage=('present','mean'),
    average_score=('score','mean')
).mul([100,1]).reset_index().to_csv(
    "analysis_attendance_vs_subject.csv", index=False)

df.groupby('year_group').agg(
    average_attendance_percentage=('present','mean'),
    average_score=('score','mean')
).mul([100,1]).reset_index().to_csv(
    "analysis_attendance_vs_year_group.csv", index=False)

df.groupby(['teacher_name','subject']).agg(
    average_attendance_percentage=('present','mean'),
    average_student_score=('score','mean')
).mul([100,1]).reset_index().to_csv(
    "analysis_teacher_performance.csv", index=False)

df.groupby(['student_id','student_name']).agg(
    overall_average_score=('score','mean')
).reset_index().sort_values(
    'overall_average_score', ascending=False
).to_csv("analysis_student_overall.csv", index=False)

df.groupby(['student_id','student_name','subject']).agg(
    average_subject_score=('score','mean')
).reset_index().to_csv(
    "analysis_student_subject.csv", index=False)

df.groupby(['subject','year_group']).agg(
    average_score=('score','mean')
).reset_index().to_csv(
    "analysis_subject_by_year_group.csv", index=False)

# VISUALISATION
#Attendace per subject vs performance
subject_perf = df.groupby('subject').agg(
    avg_attendance=('present','mean'),
    avg_score=('score','mean')
).reset_index()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
subject_perf['avg_attendance'] *= 100

plt.figure(figsize=(10,6))
sns.barplot(
    data=subject_perf,
    x='subject',
    y='avg_score'
)
plt.title("Average Attendance per Subject vs Performance")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.show()

# Attendance per year group vs performance
year_group_perf = df.groupby('year_group').agg(
    avg_attendance=('present','mean'),
    avg_score=('score','mean')
).reset_index()
year_group_perf['avg_attendance'] *= 100

plt.figure(figsize=(8,5))
sns.barplot(
    data=year_group_perf,
    x='year_group',
    y='avg_score'
)
plt.title("Attendance vs Performance by Year Group")
plt.xlabel("Year Group")
plt.ylabel("Average Score")
plt.show()

# Teacher vs attendance vs performance
teacher_perf = df.groupby(['teacher_name','subject']).agg(
    avg_attendance=('present','mean'),
    avg_score=('score','mean')
).reset_index()
teacher_perf['avg_attendance'] *= 100

plt.figure(figsize=(10,6))
sns.barplot(
    data=teacher_perf,
    y='teacher_name',
    x='avg_score',
    hue='subject'
)
plt.title("Teacher Performance by Subject")
plt.xlabel("Average Student Score")
plt.ylabel("Teacher")
plt.legend(title="Subject")
plt.tight_layout()
plt.show()

#Subject performance per year group
subject_year_perf = df.groupby(['subject','year_group']).agg(
    avg_score=('score','mean')
).reset_index()

plt.figure(figsize=(10,6))
sns.barplot(
    data=subject_year_perf,
    x='subject',
    y='avg_score',
    hue='year_group'
)
plt.title("Subject Performance by Year Group")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Student performance distribution per subject
plt.figure(figsize=(12,6))
sns.boxplot(
    data=df,
    x='subject',
    y='score'
)

plt.title("Student Performance Distribution per Subject")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Attendance vs performance scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=subject_perf,
    x='avg_attendance',
    y='avg_score',
    size='avg_score',
    legend=False
)

plt.title("Attendance vs Performance Correlation")
plt.xlabel("Average Attendance (%)")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()


print("All raw data and ALL analysis CSV files generated successfully.")