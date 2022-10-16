# Day 12: Templating Engines

## Task

Using any templating engine of your choice, make a simple tribute page for the best movie you have watched. Indicate the template engine you used in the readme along with the api URL for where your script is running.

## Code Details

### Abstract

This task was developed with the flask framework of the python programming language, Jinja2 template and TailwindCSS.

- The server-side contains our API [API Link](http://www.omdbapi.com/?apikey=362eab03&t=Forrest%20Gump) which supplies our data to our client-side template.
- When the **/index** endpoint is called, the HTML template is rendered.

### Functions

- Index function
  This function return HTML template and the **dict** data is passed to the client-side.

- Base template
  This HTML contains the neccessary information about my favourite movie like the poster, actors, genre, ratings, date of release, runtime and plot.
