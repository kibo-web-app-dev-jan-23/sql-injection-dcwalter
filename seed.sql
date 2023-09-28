-- Create students
INSERT INTO students (name) VALUES 
  ('Akron'),
  ('Aminu'),
  ('Anane'),
  ('Awotwe'),
  ('Cherechi'),
  ('Dunu'),
  ('Efe '),
  ('Gbemisola'),
  ('Ikhidie'),
  ('Isioma'),
  ('Kiama'),
  ('Kito'),
  ('Koffi'),
  ('Kumi'),
  ('Malika'),
  ('Mwinyi'),
  ('Njowga'),
  ('Obioma'),
  ('Omawunmi'),
  ('Onyesha'),
  ('Shanny'),
  ('Tamu'),
  ('Wachira'),
  ('Yawo');
  
-- Create assignments
INSERT INTO assignments (name, points) VALUES 
  ('HTML Elements Homework', 10),
  ('SQL Quiz', 10),
  ('CSS Selectors Practice', 10),
  ('Project 1', 30),
  ('Project 2', 50),
  ('SQL Injection Assignment', 50),
  ('Project 3', 60),
  ('Final Exam', 100),
  ('Presentation', 50);

-- Create assignment scores
--  gives a random score for every student / assignment pair
INSERT INTO assignment_scores (student_id, assignment_id, score) 
SELECT students.id, assignments.id, abs(random() % assignments.points) FROM students JOIN assignments;
