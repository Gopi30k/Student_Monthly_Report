
03_CREATE_STUDENT_TABLE:create table IF NOT EXISTS Student(sId integer PRIMARY KEY,sName varchar(40) NOT NULL,sDOB Date NOT NULL,sClassNo varchar(3) NOT NULL);

04_CREATE_MARKS_TABLE:create table IF NOT EXISTS Marks (Rid integer primary key ,sId integer,examDate Date NOT NULL,English varchar(3),Tamil varchar(3),Maths varchar(3),Science varchar(3),Social varchar(3),FOREIGN KEY(sId) REFERENCES Student(sId));

05_INSERT_STUDENT_RECORD_1:insert into Student values(1001,'Ashok','1996-01-30','10A');
06_INSERT_STUDENT_RECORD_2:insert into Student values(1002,'Mahesh','1996-11-23','10B');
07_INSERT_STUDENT_RECORD_3:insert into Student values(1003,'Kannan','1997-12-12','10C');
08_INSERT_STUDENT_RECORD_4:insert into Student values(1004,'Mani','1997-05-06','10A');
09_INSERT_STUDENT_RECORD_5:insert into Student values(1005,'Jacob','1996-07-23','10B');
10_INSERT_STUDENT_RECORD_6:insert into Student values(1006,'Surendar','1997-03-11','10C');

11_INSERT_MARKS_RECORD_1:insert into Marks values(1,1001,'2018-01-22','78','89','58','69','78');
12_INSERT_MARKS_RECORD_2:insert into Marks values(2,1001,'2018-02-22','89','76','68','92','95');
13_INSERT_MARKS_RECORD_3:insert into Marks values(3,1001,'2018-03-22','56','89','58','69','56');
14_INSERT_MARKS_RECORD_4:insert into Marks values(4,1001,'2018-04-22','78','89','58','69','78');
15_INSERT_MARKS_RECORD_5:insert into Marks values(5,1002,'2018-01-22','78','89','58','69','75');
16_INSERT_MARKS_RECORD_6:insert into Marks values(6,1002,'2018-02-22','71','89','58','69','70');
17_INSERT_MARKS_RECORD_7:insert into Marks values(7,1002,'2018-03-22','71','89','58','69','75');
18_INSERT_MARKS_RECORD_8:insert into Marks values(8,1002,'2018-04-22','70','89','58','69','72');
19_INSERT_MARKS_RECORD_9:insert into Marks values(9,1003,'2018-01-22','70','89','58','69','76');
20_INSERT_MARKS_RECORD_10:insert into Marks values(10,1003,'2018-02-22','60','45','36','69','73');
21_INSERT_MARKS_RECORD_11:insert into Marks values(11,1003,'2018-03-22','73','89','58','69','77');
22_INSERT_MARKS_RECORD_12:insert into Marks values(12,1003,'2018-04-22','72','89','58','69','74');
23_INSERT_MARKS_RECORD_13:insert into Marks values(13,1004,'2018-01-22','76','89','58','69','72');
24_INSERT_MARKS_RECORD_14:insert into Marks values(14,1004,'2018-02-22','78','89','58','69','72');
25_INSERT_MARKS_RECORD_15:insert into Marks values(15,1004,'2018-03-22','78','89','58','69','83');
26_INSERT_MARKS_RECORD_16:insert into Marks values(16,1004,'2018-04-22','78','89','58','69','58');
27_INSERT_MARKS_RECORD_17:insert into Marks values(17,1005,'2018-01-22','78','89','58','69','79');
28_INSERT_MARKS_RECORD_18:insert into Marks values(18,1005,'2018-02-22','78','89','58','69','73');
29_INSERT_MARKS_RECORD_19:insert into Marks values(19,1005,'2018-03-22','78','89','58','69','76');
30_INSERT_MARKS_RECORD_20:insert into Marks values(20,1005,'2018-04-22','78','89','58','69','70');

32_TASK_EXE_2:select s.sId as Id,s.sName as Name,s.sClassNo as Class,DATE_FORMAT(m.examDate,'%m-%d-%Y') as ExamDate,m.English,m.Tamil,m.Maths,m.Science,m.Social,	(m.English+m.Tamil+m.Maths+m.Science+m.Social) as Total,	dense_rank() over (order by (m.English+m.Tamil+m.Maths+m.Science+m.Social) desc) as Ranking	from Student s join Marks m on m.sId=s.sId where examDate like ;

31_TASK_EXE_1:select monthname(examdate) from marks group by month(examdate );


