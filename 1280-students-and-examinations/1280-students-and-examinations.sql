/* Write your T-SQL query statement below */

select
    s.student_id,
    s.student_name,
    sb.subject_name,
    CASE
        WHEN a.attended_exams IS NULL
        THEN 0
        ELSE a.attended_exams
    END as attended_exams
    
from
    Students s
    CROSS JOIN subjects sb
    LEFT JOIN
    (
        select
            subject_name,
            student_id,
            COUNT(student_id) as attended_exams
        from
            Examinations
        GROUP BY student_id, subject_name
    )a ON a.subject_name = sb.subject_name and a.student_id = s.student_id
ORDER BY
    s.student_id, sb.subject_name




/*



select
    subject_name,
    student_id,
    COUNT(student_id) as attended_exams
from
    Examinations
GROUP BY student_id, subject_name

*/