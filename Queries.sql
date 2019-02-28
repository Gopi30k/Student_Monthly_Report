select s.sId as ID,s.sName as Name,s.sClassNo as ClassNo,m.examDate,m.English,m.Tamil,m.Maths,m.Science,m.Social from Student s join Marks m on m.sId=s.sId;
select * from student;