# Netguru

POST /movies:

Request body {'title' : <movie_title>} - The app fetches data from omdbapi.com

GET /movies:

Lists all movies already present in application database.

POST /comments:

Request body { 'movie': <movie_id>, 'comment': <comment_text> }

Comment is saved to application database and returned in
request response.

GET /comments:

Shows a list of all comments present in application database.
Allows filtering comments by associated movie, by passing its ID.

GET /top:

Should return top movies already present in the database ranking based
on a number of comments added to the movie in the
specified date range.
 
Query param format: {'date': <YYYY-MM-DD>}

Movies with the same number of comments should have the same
position in the ranking.