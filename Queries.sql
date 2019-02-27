select s.sId,s.sName,s.sClassNo,m.examDate,m.English,m.Tamil,m.Maths,m.Science,m.Social from Student s join Marks m on m.sId=s.sId;
select * from student;