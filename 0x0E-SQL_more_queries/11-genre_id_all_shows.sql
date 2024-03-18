-- Lists all showa contained in the database
-- Dislays NULL for shows without genres
-- Records are ordered by ascending tv_shows.tites and tv_shows_genres.genre_id
SELECT s.'title', g.'genre_id'
FROM 'tv_shows' AS s
	LEFT JOIN 'tv_shows_genres' AS g
	ON s.'id' = g.'show_id'
OEDER BY s.'title', g.'genre_id';
