-- Lists the number of records with the same score
-- Records are ordered by descending order
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
GROUP BT=Y 'score'
ORDER BY 'number' DESC;
