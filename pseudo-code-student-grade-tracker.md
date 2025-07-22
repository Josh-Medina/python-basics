1. Define function get_letter_grade(score)
   - IF score >= 90 → RETURN 'A'
   - ELSE IF score >= 80 → RETURN 'B'
   - ELSE IF score >= 70 → RETURN 'C'
   - ELSE IF score >= 60 → RETURN 'D'
   - ELSE → RETURN 'F'

2. Define function print_summary(student_list)
   - PRINT "Student Summary:"
   - FOR each student in student_list:
     - PRINT student name, score, and letter grade

3. Define function save_to_file(student_list)
   - OPEN "grades.txt" in write mode
   - FOR each student in student_list:
     - WRITE name, score, and grade to file (one per line)
   - CLOSE file

4. Main Program
   - PRINT welcome message
   - CREATE empty list called students
   - WHILE user wants to continue:
     - ASK for student name
     - FORMAT name (capitalize properly)
     - ASK for score
     - CONVERT score to float
     - VALIDATE score (optional)
     - CALL get_letter_grade(score)
     - ADD (name, score, grade) to students list
     - ASK user if they want to add another student

5. AFTER loop ends:
   - CALL print_summary(students)
   - CALL save_to_file(students)
   - PRINT "Student data saved to grades.txt"

END PROGRAM