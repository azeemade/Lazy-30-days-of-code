# Day 12: Templating Engines

## Task

Using any templating engine of your choice and any logger middleware,

- clone a google.com homepage to the best of your abilities which would be accessible on the “/google” endpoint of your application.
- If the search button is clicked, redirect the user to a custom page with the message, “that was 30 days of code”(implement this page anyway you want).
- If the “/logs” route is accessed, a page with a list of all the searches made to the google clone with the response time in front of them would be displayed on the screen. Each entry is separated by a new line.

## Code Details

### Abstract

This task was developed with the flask framework of the python programming language, Jinja2 template and TailwindCSS.
When a search is made, the search query is added to a JSON log along with its timestamp and the user are redirected to a new page. The logs page keep track of all query along with their timestamp.

### Functions

- Home function
  This function responds with the cloned google homepage for the **GET** method. For the **POST** method, the form request is stored and validated then the query along with the timespand are stored in a JSON log. The user is then redirected to the result page.

- Logs function
  This function reads the list objects and are return as logs variable while the record template is rendered.
