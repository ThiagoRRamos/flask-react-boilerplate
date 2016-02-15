# flask-react-boilerplate
A boilerplate to start projects using flask and react relatively nicely.

The main idea to this project is to cover most of the boilerplate of creating a new Flask/Reactjs project for me, which includes:

- A basic jinja2 template for extending and creating new html pages with bootstrap and all othe html5 boilerplate already in place
- An easy(ier) way of defining js methods and React components, and calling/rendering them directly from the controllers
- A way of managing js dependencies using Bower, and all the transpiling and reactifying of js files using Gulp
- A basic blueprint system for Flask
- A thin ORM wrapper to deal with MongoDB
- SQLAlchemy configured to use Postgres on Heroku and SQLite on the dev machine
- An User table, and the Flask login, signin and signout views
