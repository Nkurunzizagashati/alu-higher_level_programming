-- a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server
-- The result column name should be average
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
