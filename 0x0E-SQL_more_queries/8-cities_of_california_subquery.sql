-- Lists alll cities of CA in the database
-- Results are ordered by acsending cities.id
SELECT 'id', 'name'
FROM 'cities'
WHERE 'state_id' IN
	(SELECT 'id'
		FROM 'states'
		WHERE 'name' = "Calfornia")
	ORDER BY 'id';
